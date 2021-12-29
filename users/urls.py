from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("login/github/", views.github_login, name="github_login"),
    path("login/github/callback/", views.github_callback, name="github_callback"),
    path("login/kakao/", views.kakao_login, name="kakao_login"),
    path("login/kakao/callback/", views.kakao_callback, name="kakao_callback"),
    path("logout/", views.log_out, name="logout"),
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("verify/<str:key>", views.complete_verification, name="complete_verification"),
    path("update-profile/", views.UpdateProfileView.as_view(), name="update"),
    path("update-password/", views.UpdatePasswordView.as_view(), name="password"),
    path("<int:pk>/", views.UserProfileView.as_view(), name="profile"),
    path("switch-hosting/", views.switch_hosting, name="switch-hosting"),
]
