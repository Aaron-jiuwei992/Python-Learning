# Generated by Django 3.1.5 on 2021-03-02 08:16

import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import shrimp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.IntegerField(auto_created=True, verbose_name='问题id')),
                ('userid', models.BigIntegerField(auto_created=True, unique=True, verbose_name='回答者在User表中的id')),
                ('nickname', models.CharField(default='匿名', max_length=20, verbose_name='回答者昵称')),
                ('avatar_url', models.CharField(max_length=200, verbose_name='回答者头像')),
                ('slogan', models.CharField(max_length=25, null=True, verbose_name='回答者简介')),
                ('url_token', models.CharField(max_length=100, unique=True, verbose_name='用户的唯一标识')),
                ('question_title', models.CharField(max_length=200, verbose_name='回答的问题标题')),
                ('content', models.CharField(max_length=500, verbose_name='回答内容')),
                ('status', models.IntegerField(default=1, verbose_name='问题审核状态，0表示已审核，1表示未审核')),
                ('weight', models.IntegerField(default=1, verbose_name='权重')),
                ('modify_time', models.DateTimeField(auto_now_add=True, verbose_name='回答被修改的时间')),
                ('ct', models.DateTimeField(auto_now_add=True, verbose_name='回答创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(auto_created=True, unique=True, verbose_name='用户id')),
                ('nickname', models.CharField(db_index=True, default='匿名', max_length=20, unique=True, verbose_name='用户昵称')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='问题标题')),
                ('description', models.CharField(db_index=True, max_length=500, verbose_name='问题描述')),
                ('classfication', models.CharField(db_index=True, max_length=200, verbose_name='问题类别')),
                ('modify_time', models.DateTimeField(auto_now_add=True, verbose_name='问题修改时间')),
                ('ct', models.DateTimeField(auto_now_add=True, verbose_name='提问时间')),
            ],
        ),
        migrations.CreateModel(
            name='UrlToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_token', models.CharField(max_length=100, unique=True, verbose_name='用户的唯一标识')),
                ('amount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('phone_number', models.IntegerField(null=True, unique=True, verbose_name='手机号')),
                ('nickname', models.CharField(db_index=True, max_length=32, null=True, unique=True, verbose_name='昵称')),
                ('email', models.CharField(max_length=32, null=True, unique=True, verbose_name='邮箱')),
                ('secret_key', models.CharField(max_length=30, verbose_name='密码')),
                ('slogan', models.CharField(max_length=25, null=True, verbose_name='一句话简介')),
                ('sex', models.IntegerField(default=0, verbose_name='性别')),
                ('brief_introduction', models.CharField(max_length=100, null=True, unique=True, verbose_name='用户简介')),
                ('url_token', models.CharField(max_length=30, unique=True, verbose_name='用户的唯一标识')),
                ('avatar_url', models.CharField(max_length=100, null=True, unique=True, verbose_name='用户的头像')),
                ('last_login', models.DateTimeField(auto_now_add=True, verbose_name='上次登陆时间')),
                ('ct', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', shrimp.models.UserManager()),
            ],
        ),
    ]
