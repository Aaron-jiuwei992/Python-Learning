"""orange URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from shrimp.views import Home, Register, Login, Logout, Question, QuestionPage, Answer, AnswerPage, Comment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name="logout"),
    path('question/', Question.as_view(), name='question'),
    re_path('question/(\d+)', QuestionPage.as_view(), name='question_page'),
    path('answer/', Answer.as_view(), name='answer'),
    re_path('question/(\d+)/answer/(\d+)', AnswerPage.as_view(), name='answer_page'),
    path('comment/', Comment.as_view(), name='comment'),
]
