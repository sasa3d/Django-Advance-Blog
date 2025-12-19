from rest_framework import generics
from .serializers import RegisterSerializer , CustomAuthTokenSerializer
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken


class RegisterAPIView(generics.GenericAPIView):
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
    serializer_class = CustomAuthTokenSerializer
    '''یک ویوی سفارشی برای دریافت توکن احراز هویت'''
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