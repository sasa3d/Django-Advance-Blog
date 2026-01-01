from rest_framework.generics import GenericAPIView , RetrieveUpdateAPIView , RetrieveAPIView  # noqa: F401
from django.utils.translation import gettext_lazy as _  # noqa: F401
from .serializers import RegisterSerializer , CustomAuthTokenSerializer ,ProfileSerializer,\
    CustomTokenObtainPairSerializer , ChangePasswordSerializer  # noqa: F401 
    
from rest_framework.response import Response
from rest_framework import status 

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views  import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model # from ...models import User
from ...models import Profile
from django.shortcuts import get_object_or_404
# from django.core.mail import send_mail
from mail_templated import send_mail  # noqa: F401
from mail_templated import EmailMessage
from ..utils import EmailThread

# import for JWT
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed



User = get_user_model()  # استفاده از مدل یوزر سفارشی اگر وجود داشته باشد

class RegisterAPIView(GenericAPIView):
    '''ویوی ثبت نام کاربر جدید'''
     
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):#زمان post کردن باید object مان را بسازیم پس:
        serializer = RegisterSerializer(data=request.data)  # ==self.get_serializer(data=request.data)  #ابتدا serializer را با داده های ورودی مقدار دهی میکنیم
        if serializer.is_valid():
            serializer.save()
            data = {
                "email":f"{serializer.validated_data['email']} ایمیل کاربری مورد نظر شما با موفقیت ایجاد شد"
            }
            return Response(data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class CustomAuthToken(ObtainAuthToken):
    '''یک ویوی سفارشی برای دریافت توکن احراز هویت'''
    serializer_class = CustomAuthTokenSerializer
            # منطق سفارشی برای احراز هویت و بازگرداندن توکن
    def post(self, request, *args, **kwargs):
        # میتونی اینجا serializer سفارشی خودت رو هم تعریف کنی اگر خواستی
        serializer = self.serializer_class(data=request.data , 
                                        context={'request': request})  
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
    # میتوانی فیلدها(خواسته ها(داده های)) سفارشی هم اینجا تعریف کنی 
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
        
        
"""چون میخایم یک متد حذف (نابودی) برای  توکن  بنویسیم که آن را discard نماید اگر بخاهیم که از کلاس جنریک استفاده کنیم به سریالایزر نیازمند میشویم  و نداریم درنتیجه از یک کلاسی ارثبری میکنیم که نیازی به سریالایزر  نداشته باشد. 
سوال: چه کلاس به سریالایزر  نیازی ندارد؟ جواب :APIView 
پس از  APIView  استفاده میکنیم 
"""
class CustomDiscardAuthToken(APIView):
    '''یک ویوی سفارشی برای حذف توکن احراز هویت'''
    permission_classes = [IsAuthenticated]  # فقط کاربران احراز هویت شده میتوانند توکن خود را حذف کنند
    def post(self, request, *args, **kwargs):
        # حذف توکن احراز هویت کاربر
        try:
            request.user.auth_token.delete() # حذف توکن مرتبط با کاربر احراز هویت شده
        except (AttributeError, Token.DoesNotExist):
            pass
        return Response({"detail": "Token deleted successfully."}, status=status.HTTP_204_OK)

class CustomTokenObtainPairView(TokenObtainPairView):
    '''ویوی سفارشی برای دریافت جفت توکن JWT'''
    # میتوانی اینجا سریالایزر سفارشی خودت رو هم تعریف کنی اگر خواستی
    serializer_class = CustomTokenObtainPairSerializer
       
class ChangePasswordAPIView(GenericAPIView): # from generics
    # Source - https://stackoverflow.com/a/38846554
        '''ویوی تغییر رمز عبور کاربر'''
        """
        An endpoint for changing password.
        """
        model = User
        permission_classes = (IsAuthenticated,)
        serializer_class = ChangePasswordSerializer

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def put(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password.پسورد جدیدت با پسورد قدیمت باهم غریبه هستن همچنان"]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'status': 'success دوتا پسوردها باهم آشنا  و یکی شدن تبریک',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }

                return Response(response)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileAPIView(RetrieveUpdateAPIView): #from generics
    '''ویوی نمایش و به‌روزرسانی پروفایل کاربر'''
    serializer_class = ProfileSerializer  # استفاده از همان سریالایزر ثبت نام برای نمایش و به‌روزرسانی پروفایل
    permission_classes = [IsAuthenticated]  # فقط کاربران احراز هویت شده میتوانند پروفایل خود را مشاهده و ویرایش کنند
    queryset = Profile.objects.all()
    
    def get_object(self): # بازگرداندن پروفایل کاربر احراز هویت شده بدون lookup- Id
        qs =  self.get_queryset() 
        obj = get_object_or_404(qs , user=self.request.user)
        return obj
        
    
class TestEmailSend(GenericAPIView): # from generics 
    '''  این کلاس برای تست ایمیل میباشد  '''
    serializer_class = None  # <--- این خط رو اضافه کن تا Swagger بفهمه خبری از سریلایزر نیست
    
    def get(self, request, *args, **kwargs):
        self.email = "KaramAli@gmail.com"
        user_obj = get_object_or_404(User , email=self.email)
        token = self.get_tokens_for_user(user_obj)
        
        email_obj = EmailMessage( 'email/hello.tpl',   # 1. آدرس تمپلیت
                # {'name': 'Saber'}, 
                {'token': token } ,      # 2. کانتکست (داده‌های ارسالی به تمپلیت)
                'admin@admin.com',                   # 3. فرستنده (فقط یک استرینگ ساده)
                # to=['sabermodirian@gmail.com']       # 4. گیرنده (لیستی از استرینگ‌ها)
                to=[self.email]
            )
        # TODO: Add more useful commands here.
        EmailThread(email_obj).start()
        
        return Response('Email Sent!!!')

    def get_tokens_for_user(self,user):
        if not user.is_active:
         raise AuthenticationFailed("User is not active")

        refresh = RefreshToken.for_user(user)

        return  str(refresh.access_token)