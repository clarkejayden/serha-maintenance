from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.test, name="test"),
    path("loginpage/", views.loginpage, name="loginpage"),
    path("registerpage/", views.registerpage, name="registerpage"),
    path("report/", views.submit_report, name="submit_report"),
    path("my-reports/", views.user_previous_reports, name="user_previous_reports"),
]