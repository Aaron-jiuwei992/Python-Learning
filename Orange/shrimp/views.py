from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .error import ErrorCode, MESSAGE
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .import utils as UTILS
import pypinyin
from pypinyin import pinyin
from . import models
import time


# Create your views here.
class Home(View):
    def get(self, request):
        """
        接口描述：该接口实现首页随机显示5条回答。
        """
        # 获取user对象，通过render返回给前端渲染
        userid = request.session.get('userid', '')
        user = models.User.objects.get(id=userid) if userid else None

        # 获取权重最高的前5条回答（权重的计算与点赞，评论，收藏数有关）
        answers = models.Answer.objects.order_by('-weight')[:5]
        try:
            # 若评论不为空，则遍历每个回答，得到每个回答的评论数量和评论内容
            for answer in answers:
                comments = models.Comment.objects.filter(answer_id=answer.id)
                answer.comment_length = comments.count()
                answer.comments = comments.order_by('-ct')[:5]
        except:
            answers = None
        return render(request, 'shrimp/index.html', {'user': user, 'answers': answers})


class Register(View):
    def get(self, request):
        return render(request, 'shrimp/register.html')

    def post(self, request):
        username = request.POST.get('username')
        secret_key = request.POST.get('secret_key')
        register_type = int(request.POST.get('register_type', -1))
        nickname = request.POST.get('nickname', '')
        response = {'code': ErrorCode.sucess, 'message': MESSAGE[ErrorCode.sucess]}

        if not username or not nickname or not secret_key or not (register_type in {0, 1})\
                or (register_type == 0 and not UTILS.phone_valid(username)) \
                or (register_type == 1 and not UTILS.email_valid(username)):
            response['code'] = ErrorCode.invalid_arguments
            response['message'] = MESSAGE[ErrorCode.invalid_arguments]
        else:
            # 手机号验证码方式注册
            if register_type == 0:
                phone_number = username
                # 判断手机号是否有效
                if not UTILS.phone_valid(phone_number):
                    response['code'] = ErrorCode.invalid_arguments
                    response['message'] = MESSAGE[ErrorCode.invalid_arguments]
                else:
                    # 判断验证码是否有效
                    sms = UTILS.get_sms_captcha()
                    ct = time.time()
                    pass
            else:
                # 邮箱和密码方式注册
                try:
                    # 判断用户是否已经是注册用户
                    models.User.objects.get(email=username)
                    response['code'] = ErrorCode.user_exists
                    response['message'] = MESSAGE[ErrorCode.user_exists]
                except:
                    # (核心代码部分)通过用户昵称生成url_token
                    pinyins = pinyin(nickname, style=pypinyin.Style.NORMAL)
                    url_token = ""
                    for _ in pinyins:
                        url_token += "".join(_)
                    try:
                        # 将新生成的url_token和数据库中的比较，先判断是否是已存在的url_token
                        token = models.UrlToken.objects.get(url_token=url_token)

                        # 如果已存在，则数量递增1
                        amount = token.amount + 1
                        token.amount = amount
                        url_token = url_token + str(amount)
                    except:
                        # 如果是不存在的url_token，则在数据库中新增一个
                        models.UrlToken.objects.create(url_token=url_token)

                    user = models.User.objects.create_user(username, secret_key, url_token=url_token, nickname=nickname)
                    user.save()
        return JsonResponse(response)


class Login(View):
    def get(self, request):
        return render(request, 'shrimp/login.html')

    def post(self, request):
        username = request.POST.get('username', '')
        secret_key = request.POST.get('secret_key', '')
        # 注意要将验证类型转换为数值类型
        veri_type = int(request.POST.get('veri_type', -1))

        response = {'code': ErrorCode.sucess, 'message': MESSAGE[ErrorCode.sucess]}

        # 验证用户输入的参数的合法性
        if not username or not secret_key or not (veri_type in {0, 1}) \
                or (veri_type == 0 and not UTILS.phone_valid(username)) \
                or (veri_type == 1 and not UTILS.email_valid(username)):
            response['code'] = ErrorCode.invalid_arguments
            response['message'] = MESSAGE[ErrorCode.invalid_arguments]
        else:
            # 判断用户以哪种方式进行登陆
            # 用户以手机号和验证码的方式进行登陆
            if veri_type == 0:
                pass

            # 用户以邮箱和密码的方式进行登陆
            else:
                # 将用户输入的邮箱和密码与数据库中的数据进行比较,此处调用authenticate函数验证
                user = authenticate(username=username, password=secret_key)
                # 判断用户是否为真，不为真则参数无效
                if not user:
                    response['code'] = ErrorCode.invalid_arguments
                    response['message'] = MESSAGE[ErrorCode.invalid_arguments]
                else:
                    request.session['userid'] = user.id
                    request.session['nickname'] = user.nickname
                    request.session['url_token'] = user.url_token
                    # 为当前用户创建登陆会话
                    login(request, user)
        return JsonResponse(response)


class Question(LoginRequiredMixin, View):
    # 如果用户未登录，则通过此行代码跳转到登陆界面
    login_url = 'login/'

    def post(self, request):
        userid = request.session.get('userid', '')
        nickname = request.session.get('nickname', '')
        title = request.POST.get('title', '')
        description = request.POST.get('description', '')
        classfication = request.POST.get('classfication', '')

        response = {'code': ErrorCode.sucess, 'message': MESSAGE[ErrorCode.sucess]}

        if not userid or not nickname or not title or not description or not classfication:
            response['code'] = ErrorCode.invalid_arguments
            response['message'] = MESSAGE[ErrorCode.invalid_arguments]
        else:
            question = models.Question.objects.create(userid=userid, nickname=nickname, title=title, description=description,
                                                      classfication=classfication)
            response['data'] = {'question_id': question.id}
        return JsonResponse(response)


class QuestionPage(View):
    """
    接口描述：提问成功后跳转到问题页面，问题页面显示某一个问题的详细内容和相对应的回答
    """
    def get(self, request, question_id):
        try:
            question_obj = models.Question.objects.get(id=question_id)
            answers = models.Answer.objects.filter(question_id=question_id)
            userid = request.session.get('userid')
            user = models.User.objects.get(id=userid) if userid else None
        except:
            response = {'code': ErrorCode.invalid_arguments, 'message': MESSAGE[ErrorCode.invalid_arguments]}
            return JsonResponse(response)

        return render(request, 'shrimp/question.html', {'user': user, 'question_obj': question_obj, 'answers': answers})


class Logout(LoginRequiredMixin, View):
    login_url = 'login/'

    def post(self, request):
        response = {'code': ErrorCode.sucess, 'message': MESSAGE[ErrorCode.sucess]}
        logout(request)
        return JsonResponse(response)


class Answer(LoginRequiredMixin, View):
    # 如果用户未登录，则通过此行代码跳转到登陆界面
    login_url = 'login/'

    def post(self, request):
        userid = request.session.get('userid', '')
        nickname = request.session.get('nickname', '')

        avatar_url = request.POST.get('avatar_url', '')
        slogan = request.POST.get('slogan', '')
        url_token = request.session.get('url_token', '')
        question_id = request.POST.get('question_id', '')
        question_title = request.POST.get('question_title', '')
        content = request.POST.get('content', '')

        response = {'code': ErrorCode.sucess, 'message': MESSAGE[ErrorCode.sucess]}
        if not userid or not nickname or not url_token or not question_id or not question_title or not content:
            response['code'] = ErrorCode.invalid_arguments
            response['message'] = MESSAGE[ErrorCode.invalid_arguments]
        else:
            try:
                # 通过问题id获取问题对象，借此判断问题id是否为数据库中的有效id
                # （只有有效id时，才创建该问题的回答）
                models.Question.objects.get(id=question_id)
                # 上面代码不发生异常时创建回答对象
                answer_obj = models.Answer.objects.create(userid=userid, nickname=nickname, avatar_url=avatar_url,
                                                          slogan=slogan, url_token=url_token, question_id=question_id, question_title=question_title,
                                                          content=content)
                # 这里将问题的id和回答的id响应给前端
                response['data'] = {'question_id': question_id, 'answer_id': answer_obj.id}
            except Exception as e:
                print(e)
                response['code'] = ErrorCode.invalid_arguments
                response['message'] = MESSAGE[ErrorCode.invalid_arguments]
        return JsonResponse(response)


class AnswerPage(View):
    """
    接口描述：回答成功后跳转到回答页面，回答页面显示某一个问题的回答
    """
    def get(self, request, question_id, answer_id):
        # 通过问题id和回答id获取对应的问题对象和回答对象
        try:
            question = models.Question.objects.get(id=question_id)
            answer = models.Answer.objects.get(id=answer_id)

            userid = request.session.get('userid', '')
            user = models.User.objects.get(id=userid) if userid else None

        except:
            # 回答页面可以没有回答，此时发生异常，将问题和回答问题设置为None值
            question = answer = None

        return render(request, 'shrimp/answer.html', {'user': user, 'question': question, 'answer': answer})


class Comment(LoginRequiredMixin, View):
    # 如果用户未登录，则通过此行代码跳转到登陆界面
    login_url = 'login/'

    def post(self, request):
        userid = request.session.get('userid')
        nickname = request.session.get('nickname', '')
        url_token = request.session.get('url_token', '')
        avatar_url = request.POST.get('avatar_url', '')

        answer_id = request.POST.get('answer_id', '')
        comment = request.POST.get('comment', '')

        # 非必选字段
        comment_id = request.POST.get('comment_id', -1)
        other_userid = request.session.get('userid', -1)
        other_nickname = request.session.get('nickname', '')
        other_url_token = request.session.get('url_token', '')
        other_avatar_url = request.POST.get('avatar_url', '')

        response = {'code': ErrorCode.sucess, 'message': MESSAGE[ErrorCode.sucess]}
        if not userid or not nickname or not url_token:
            response['code'] = ErrorCode.user_not_login
            response['message'] = MESSAGE[ErrorCode.user_not_login]
        elif not answer_id or not comment:
            response['code'] = ErrorCode.invalid_arguments
            response['message'] = MESSAGE[ErrorCode.invalid_arguments]
        else:
            try:
                answer_obj = models.Answer.objects.get(id=answer_id)
                comment_obj = models.Comment.objects.create(userid=userid, nickname=nickname, url_token=url_token,
                                                            avatar_url=avatar_url, answer_id=answer_id, comment=comment,
                                                            comment_id=comment_id, other_userid=other_userid,
                                                            other_nickname=other_nickname, other_url_token=other_url_token,
                                                            other_avatar_url=other_avatar_url)
                # 计算评论的权重，使得回答按权重显示
                weight = UTILS.calc_weight(commnet=1)
                answer_obj.weight += weight

                answer_obj.save()
                response['data'] = {'comment_id': comment_obj.id}

            except Exception as e:
                print(e)
                response['code'] = ErrorCode.invalid_arguments
                response['message'] = MESSAGE[ErrorCode.invalid_arguments]

        return JsonResponse(response)







