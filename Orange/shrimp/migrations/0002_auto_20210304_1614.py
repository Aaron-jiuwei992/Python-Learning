# Generated by Django 3.1.5 on 2021-03-04 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shrimp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_id', models.IntegerField(auto_created=True, verbose_name='回答的id')),
                ('other_userid', models.BigIntegerField(auto_created=True, unique=True, verbose_name='回复者在User表中的id')),
                ('userid', models.BigIntegerField(auto_created=True, unique=True, verbose_name='评论者在User表中的id')),
                ('nickname', models.CharField(default='匿名', max_length=20, verbose_name='评论者昵称')),
                ('avatar_url', models.CharField(max_length=200, verbose_name='评论者头像')),
                ('other_nickname', models.CharField(default='匿名', max_length=20, verbose_name='回复者昵称')),
                ('other_avatar_url', models.CharField(max_length=200, verbose_name='回复者头像')),
                ('comment', models.CharField(max_length=500, verbose_name='评论的内容')),
                ('comment_id', models.IntegerField(null=True, verbose_name='评论/回复的id')),
                ('url_token', models.CharField(max_length=30, null=True, verbose_name='评论者url_token')),
                ('other_url_token', models.CharField(max_length=30, null=True, verbose_name='回复者url_token')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='评论修改时间')),
                ('ct', models.DateTimeField(auto_now_add=True, verbose_name='评论创建时间')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='status',
            field=models.IntegerField(default=1, verbose_name='问题的审核状态，0表示已审核，1表示未审核'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question_id',
            field=models.IntegerField(auto_created=True, verbose_name='回答的问题id'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='status',
            field=models.IntegerField(default=1, verbose_name='回答的审核状态，0表示已审核，1表示未审核'),
        ),
        migrations.AlterField(
            model_name='urltoken',
            name='amount',
            field=models.IntegerField(default=0, verbose_name='相同url_token的数量'),
        ),
    ]
