from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.utils import timezone


# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("请填入邮箱！")
        if not password:
            raise ValueError("请填入密码!")

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    phone_number = models.IntegerField(unique=True, null=True, verbose_name='手机号')
    nickname = models.CharField(max_length=32, null=True, unique=True, db_index=True, verbose_name='昵称')
    email = models.CharField(max_length=32, null=True, unique=True, verbose_name='邮箱')
    secret_key = models.CharField(max_length=30, null=False, verbose_name='密码')
    slogan = models.CharField(max_length=25, null=True, verbose_name='一句话简介')
    sex = models.IntegerField(default=0, verbose_name='性别')
    brief_introduction = models.CharField(max_length=100, null=True, unique=True, verbose_name='用户简介')
    url_token = models.CharField(max_length=30, null=False, unique=True, verbose_name='用户的唯一标识')
    avatar_url = models.CharField(max_length=100, null=True, unique=True, verbose_name='用户的头像')
    last_login = models.DateTimeField(auto_now_add=True, verbose_name='上次登陆时间')
    ct = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    is_staff = models.BooleanField(
        default=False,
        help_text='Designates whether the user can log into this admin site.',
    )
    is_active = models.BooleanField(
        default=True,
        help_text=
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.',
    )
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    # 将email作为username字段
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class UrlToken(models.Model):
    url_token = models.CharField(max_length=100, unique=True, verbose_name='用户的唯一标识')
    amount = models.IntegerField(default=0, verbose_name='相同url_token的数量')


class Question(models.Model):
    nickname = models.CharField(max_length=20, null=False, db_index=True, default='匿名', unique=True, verbose_name='用户昵称')
    userid = models.IntegerField(null=False, verbose_name='用户id')
    title = models.CharField(max_length=100, null=False, db_index=True, verbose_name='问题标题')
    description = models.CharField(max_length=500, null=False, db_index=True, verbose_name='问题描述')
    classfication = models.CharField(max_length=200, null=False, db_index=True, verbose_name='问题类别')
    status = models.IntegerField(null=False, default=1, verbose_name='问题的审核状态，0表示已审核，1表示未审核')
    modify_time = models.DateTimeField(auto_now_add=True, null=False, verbose_name='问题修改时间')
    ct = models.DateTimeField(auto_now_add=True, null=False, verbose_name='提问时间')


class Answer(models.Model):
    userid = models.BigIntegerField(null=False, verbose_name='回答者在User表中的id')
    nickname = models.CharField(max_length=20, null=False, default='匿名', verbose_name='回答者昵称')
    avatar_url = models.CharField(max_length=200, null=False, verbose_name='回答者头像')
    slogan = models.CharField(max_length=25, null=True, verbose_name='回答者简介')
    url_token = models.CharField(max_length=100, verbose_name='用户的唯一标识')
    question_id = models.IntegerField(null=False, auto_created=True, verbose_name='回答的问题id')
    question_title = models.CharField(max_length=200, null=False, verbose_name="回答的问题标题")

    content = models.CharField(max_length=500, null=False, verbose_name='回答内容')
    status = models.IntegerField(null=False, default=1, verbose_name='回答的审核状态，0表示已审核，1表示未审核')
    weight = models.IntegerField(default=1, verbose_name="权重")
    modify_time = models.DateTimeField(auto_now_add=True, verbose_name='回答被修改的时间')
    ct = models.DateTimeField(auto_now_add=True, verbose_name='回答创建时间')


class Comment(models.Model):
    userid = models.BigIntegerField(null=False, verbose_name='评论者在User表中的id')
    nickname = models.CharField(max_length=20, null=False, default='匿名', verbose_name='评论者昵称')
    avatar_url = models.CharField(max_length=200, null=False, verbose_name='评论者头像')

    other_userid = models.BigIntegerField(null=False, verbose_name='回复者在User表中的id')
    other_nickname = models.CharField(max_length=20, null=False, default='匿名', verbose_name='回复者昵称')
    other_avatar_url = models.CharField(max_length=200, null=False, verbose_name='回复者头像')

    answer_id = models.IntegerField(null=False, verbose_name='回答的id')
    comment = models.CharField(max_length=500, null=False, verbose_name='评论的内容')
    comment_id = models.IntegerField(null=True, verbose_name='评论/回复的id')

    url_token = models.CharField(max_length=30, null=True, verbose_name="评论者url_token")
    other_url_token = models.CharField(max_length=30, null=True, verbose_name="回复者url_token")

    modify_time = models.DateTimeField(auto_now=True, verbose_name="评论修改时间")
    ct = models.DateTimeField(auto_now_add=True, verbose_name="评论创建时间")






















