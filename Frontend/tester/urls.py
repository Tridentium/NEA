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
    path("settestsettings/", views.settestsettings, name="settestsettings"),
    path("answerquestion/", views.answerquestion, name="answerquestion"),
    path("registeraccount/", views.registeraccount, name="registeraccount"),
    path("loginaccount/", views.loginaccount, name="loginaccount"),
    path("newquestion/", views.newquestion, name="newquestion"),
    path("test/question/<int:selected_length>/", views.question, name="question"),
    path("test/answer/", views.answer, name="answer"),
]