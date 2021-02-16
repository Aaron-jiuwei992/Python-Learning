from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
import pypinyin
from pypinyin import pinyin
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail, send_mass_mail
from django.views import View
from .error import ErrorCode,MESSAGE
from . import utils as UTILS
from . import models


class Home(View):
    def get(self, request):
        try:
            user_id = request.session.get('userid')
            user = models.User.objects.get(pk=user_id)

        except:
            user = None

        answers = models.Answer.objects.order_by("-weight")[:5]
        for answer in answers:
            qs = models.Comment.objects.filter(answer_id=answer.id)
            answer.comments_length = qs.count()
            answer.comments = qs.order_by('-ct')[:5]

        return render(request,'shrimp/index.html',{'user':user, 'answers':answers})


# Create your views here.
class Register(View):
    def get(self, request):
        return render(request,'shrimp/register.html')

    def post(self, request):
        username = request.POST.get('username')
        secret_key = request.POST.get('secret_key')
        register_type = int(request.POST.get('register_type', -1))
        nickname = request.POST.get('nickname', '')
        response = {"code":ErrorCode.sucess, "message":MESSAGE[ErrorCode.sucess]}

        # 判断输入的账号，密码，以及注册类型是否合法
        if not username or not nickname or not secret_key or not register_type in {0,1} or \
        (register_type==0 and not UTILS.phone_valid(username)) or \
        (register_type==1 and not UTILS.email_valid(username)):

            response['code'] = ErrorCode.invalid_arguments
            response['message'] = MESSAGE[ErrorCode.invalid_arguments]
        # 手机验证码方式进行注册
        else:
            if register_type==0:
                pass
            # 由于一开始已经有判断secret_key的取值范围，所以这里不用elif，直接else就行
            # 邮箱方式进行注册
            else:
                try:
                    # 判断是否有这个用户，有的话返回已存在
                    models.User.objects.get(email=username)
                    response['code'] = ErrorCode.user_exists
                    response['message'] = MESSAGE[ErrorCode.user_exists]
                except:
                    pinyins = pinyin(nickname, style=pypinyin.Style.NORMAL)
                    url_token = ""
                    for _ in pinyins:
                        url_token += "".join(_)
                    try:
                        token = models.UrlToken.objects.get(url_token=url_token)
                        amount = token.amount+1
                        token.amount = amount
                        token.save()
                        url_token = url_token + str(amount)
                    except:
                        models.UrlToken.objects.create(url_token=url_token)

                    user = models.User.objects.create_user(username,secret_key, url_token=url_token, username =nickname)
                    user.save()

        return JsonResponse(response)




class Login(View):

    def get(self,request):
        return  render(request,'shrimp/login.html')

    def post(self, request):
        username = request.POST.get("username", "")
        secret_key = request.POST.get('secret_key', "")
        veri_type = int(request.POST.get('veri_type', -1))
        response = {"code": ErrorCode.sucess, "message": MESSAGE[ErrorCode.sucess]}

        # 判断输入的账号，密码，以及注册类型是否合法
        if not username or not secret_key or not veri_type in {0, 1} or \
        (veri_type == 0 and not UTILS.phone_valid(username)) or \
        (veri_type == 1 and not UTILS.email_valid(username)):
            response['code'] = ErrorCode.invalid_arguments
            response['message'] = MESSAGE[ErrorCode.invalid_arguments]
        else:
            if veri_type == 0:
               pass
            # 邮箱登录方式
            else:
                user = authenticate(username=username, password=secret_key)
                # 判断user是否有效，如果无效则表示认证失败
                if not user:
                    response['code'] = ErrorCode.invalid_arguments
                    response['message'] = MESSAGE[ErrorCode.invalid_arguments]
                else:
                    request.session["userid"] = user.id
                    request.session['nickname'] = user.username
                    request.session['url_token'] = user.url_token
                    login(request, user)

        return JsonResponse(response)



class Question(LoginRequiredMixin,View):
    login_url = "login/"

    def post(self, request):
        userid = request.session.get('userid')
        username = request.POST.get('username', '')
        title = request.POST.get('title', '')

        description = request.POST.get('description','')
        classfication = request.POST.get('classfication','')
        response = {"code": ErrorCode.sucess, "message": MESSAGE[ErrorCode.sucess]}

        if  not username or not title or not classfication:
            response = {"code": ErrorCode.invalid_arguments,  "message": MESSAGE[ErrorCode.invalid_arguments]}
        else:
            question_ = models.Question.objects.create(userid=userid,username=username,title=title,description=description,classification=classfication)
            response['data'] = {"question_id":question_.id}

        return JsonResponse(response)


class Logout(LoginRequiredMixin,View):
    login_url = "login/"

    def post(self, request):
        response = {"code": ErrorCode.sucess, "message": MESSAGE[ErrorCode.sucess]}
        logout(request)
        return JsonResponse(response)


class QuestionPage(View):
    def get(self,request,question_id):
        try:
            question_obj = models.Question.objects.get(id=question_id)
            answers = models.Answer.objects.filter(question_id=question_id)
            try:
                userid = request.session.get('userid')
                user = models.User.objects.get(pk=userid)
            except:
                user = None
        except:
            response = {"code": ErrorCode.invalid_arguments, "message": MESSAGE[ErrorCode.invalid_arguments]}
            return JsonResponse(response)

        return render(request,"shrimp/question.html",
                      {"question_obj":question_obj, "user": user, "answers":answers})


class Answer(LoginRequiredMixin, View):
    login_url = "login/"

    def post(self,request):
        userid = request.session.get('userid')
        nickname = request.session.get('nickname')

        avatar_url= request.POST.get('avatar_url','')
        slogan = request.POST.get('slogan','')

        url_token = request.POST.get('url_token','')
        question_id = request.POST.get('question_id','')
        question_title = request.POST.get('question_title','')
        content = request.POST.get('content', '')
        response = {"code": ErrorCode.sucess, "message": MESSAGE[ErrorCode.sucess]}


        if not question_id or not content or not url_token or not question_title:
            response["code"]= ErrorCode.invalid_arguments
            response["message"] = MESSAGE[ErrorCode.invalid_arguments]

        else:
            try:
                models.Question.objects.get(pk=question_id)
                answer_obj = models.Answer.objects.create(userid=userid, nickname=nickname, question_id=question_id,
                                                          question_title=question_title, content=content, avatar_url = avatar_url,
                                                          slogan=slogan)
                response["data"] = {'question_id': question_id, 'answer_id': answer_obj.id}

            except Exception as e:
                print(e)
                response["code"] = ErrorCode.invalid_arguments
                response["message"] = MESSAGE[ErrorCode.invalid_arguments]



        return JsonResponse(response)

class AnswerPage(View):
        def get(self, request, question_id, answer_id):
            try:
                question = models.Question.objects.get(pk=question_id)
                answer = models.Question.objects.get(pk=answer_id)
            except:
                question = answer = None

            try:
                user_id = request.session.get('userid')
                user = models.User.objects.get(pk=user_id)
            except:
                user = None

            return render(request, 'shrimp/answer.html', {"user": user, "question": question,
                                                            "answer": answer})


class Comment(LoginRequiredMixin, View):
    login_url = "login/"

    def post(self, request):
        user_id = request.session.get('userid')
        nickname = request.session.get('nickname')
        url_token = request.session.get('url_token')

        answer_id = request.POST.get('answer_id')
        comment = request.POST.get("comment")

        # 非必传的字段
        comment_id = request.POST.get("comment_id", -1)
        other_userid = request.POST.get("other_userid", -1)
        other_nickname = request.POST.get("other_nickname", "")
        other_url_token = request.POST.get("other_url_token")

        response = {"code": ErrorCode.sucess, "message": MESSAGE[ErrorCode.sucess]}

        if not user_id:
            response["code"] = ErrorCode.user_not_login
            response["message"] = MESSAGE[ErrorCode.user_not_login]
        elif not answer_id or not comment:
            response["code"] = ErrorCode.invalid_arguments
            response["message"] = MESSAGE[ErrorCode.invalid_arguments]
        else:
            try:
                answer_model = models.Answer.objects.get(id=answer_id)
                weight = UTILS.calc_weight(comments=1)
                answer_model.weight += weight

                comment_model = models.Comment.objects.create(answer_id=answer_id,
                                                              comment=comment, comment_id=comment_id,
                                                              user_id=user_id, other_userid=other_userid,
                                                              url_token=url_token,
                                                              other_url_token=other_url_token, nickname=nickname,
                                                              other_nickname=other_nickname)

                answer_model.save()
                response['data'] = {'comment_id': comment_model.id}

            except Exception as e:
                print(e)
                response['code'] = ErrorCode.invalid_arguments
                response['message'] = MESSAGE[ErrorCode.invalid_arguments]

        return JsonResponse(response)