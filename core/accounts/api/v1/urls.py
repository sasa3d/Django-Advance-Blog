from rest_framework_simplejwt.views import (
TokenObtainPairView,
TokenRefreshView,
TokenVerifyView,
)
from django.urls import path  # include رو وقتی واقعاً لازم داشتی اضافه کن  # noqa: F401
from .views import CustomAuthToken , RegisterAPIView ,CustomDiscardAuthToken
# from rest_framework.authtoken.views import obtain_auth_token # handle token authentication
''' obtain_auth_token view خودش یک view هست که وقتی صدا زده بشه با دریافت یوزرنیم و پسورد توکن احراز هویت را برمیگرداند
    obtain_auth_token is a built-in view provided by Django REST Framework for handling token-based authentication.
'''


app_name = "accounts_api_v1"  # اختیاری اما مفید برای namespace

urlpatterns = [
    # Registration
    path("register/", RegisterAPIView.as_view(), name="register"),
   
     # Login
    # path("token/login/", obtain_auth_token, name="token-login"),  # مسیر برای دریافت توکن احراز هویت
    path("token/login/", CustomAuthToken.as_view(), name="token-login"),  # مسیر برای دریافت توکن احراز هویت با ویوی سفارشی
  
    # Logout
    path("token/logout/", CustomDiscardAuthToken.as_view(), name="token-logout"),  # مسیر برای حذف توکن احراز هویت با ویوی سفارشی
   
    # JWT Token endpoints    
    path('jwt/create/', TokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('jwt/verify', TokenVerifyView.as_view(), name='jwt-verify'),
]
