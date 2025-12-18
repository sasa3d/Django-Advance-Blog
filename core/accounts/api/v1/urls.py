from django.urls import path  # include رو وقتی واقعاً لازم داشتی اضافه کن  # noqa: F401
from . import views

from rest_framework.authtoken.views import obtain_auth_token # handle token authentication

    



app_name = "accounts_api_v1"  # اختیاری اما مفید برای namespace

urlpatterns = [
    # Registration
    path("register/", views.RegisterAPIView.as_view(), name="register"),
    path("token/login/", obtain_auth_token, name="token-login"),  # مسیر برای دریافت توکن احراز هویت
    # Login
   
]
