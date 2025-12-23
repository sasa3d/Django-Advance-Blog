
from django.urls import path  # include رو وقتی واقعاً لازم داشتی اضافه کن  # noqa: F401
from ..views import ProfileAPIView
''' obtain_auth_token view خودش یک view هست که وقتی صدا زده بشه با دریافت یوزرنیم و پسورد توکن احراز هویت را برمیگرداند
    obtain_auth_token is a built-in view provided by Django REST Framework for handling token-based authentication.
'''

urlpatterns = [
   
    
    path('',ProfileAPIView.as_view(),name='profile'),  # استفاده مجدد از ویوی ثبت نام برای نمایش و به‌روزرسانی پروفایل کاربر
]
