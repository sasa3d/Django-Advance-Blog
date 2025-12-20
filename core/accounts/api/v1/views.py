from rest_framework import generics
from .serializers import RegisterSerializer , CustomAuthTokenSerializer , CustomTokenObtainPairSerializer  # noqa: F401
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views  import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

class RegisterAPIView(generics.GenericAPIView):
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
       