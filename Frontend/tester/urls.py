from django.urls import path

from . import views

app_name = "tester"
urlpatterns = [
    path("", views.index, name = "index"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("account/", views.profile, name="profile"),
    path("students/", views.studentdata, name="studentdata"),
    path("test/testsettings/", views.testsettings, name="testsettings"),
    path("test/question/", views.question, name="question"),
    path("test/answer/", views.answer, name="answer"),
]