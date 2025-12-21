from rest_framework import serializers
from ...models import Profile, User  # == from core.accounts.models import User 
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjVE # DVE  <خلاصه شده و مخفف >  DjangoValidationError 

from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=255, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'password','password1']
        
    def validate(self , attrs):
        '''این متد برای اعتبار سنجی فیلدها استفاده میشود'''
        if attrs.get('password') != attrs.get('password1'):
            # اگر رمز عبور با تکرار آن مطابقت نداشت خطا میدهد
            raise serializers.ValidationError(
                {'password Confirmation' :
                'password dosn,t match(دو تا پسوردات هنوز با هم قهرن؛ یکسانشون کن)رمز اولت با رمز کانفرم شدت باهم قهرند!)'}
                )
        try :
            validate_password(attrs.get('password'))
        except DjVE as e: # اگر رمز عبور استانداردهای اعتبار سنجی را نداشت همه ی خطاهای مربوطه را میگیرد و به عنوان یک آبجکت(e) برمیگرداند
            raise serializers.ValidationError({'PassWord' :list(e.messages)})
              #این خطاها را به صورت یک لیست از پیام ها به کلاینت برمیگرداند
            
        return super().validate(attrs)# ادامه ی اعتبار سنجی را به متد والد میسپارد و نتیجه را برمیگرداند
    
    def create(self, validated_data):
        '''این متد برای ساختن یوزر جدید استفاده میشود'''
        validated_data.pop("password1", None) # حذف فیلد تکرار رمز عبور از داده های اعتبارسنجی شده
        # return super().create(validated_data) # ساخت یوزر جدید با داده های اعتبارسنجی شده
        return User.objects.create_user(**validated_data)
    # ساخت یوزر جدید با داده های اعتبارسنجی شده با استفاده از متد (که در مدل اصلی ما نوشته ام)create_user مدل یوزر
      
class CustomAuthTokenSerializer(serializers.Serializer):
    """
    Serializer for user authentication via username and password.
    """
    email = serializers.CharField(
        label=_("Email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        """
        Validate and authenticate the user.
        """
        username = attrs.get('email') # در اینجا ما از ایمیل به عنوان یوزرنیم استفاده میکنیم
        password = attrs.get('password')

        if username and password:
            user = authenticate(
                request=self.context.get('request'),
                username=username,
                password=password
            )
            if not user:
                raise serializers.ValidationError(
                    _("Unable to log in with provided credentials."),
                    code='authorization'
                )
        else:
            raise serializers.ValidationError(
                _('Must include "username" and "password".'),
                code='authorization'
            )

        attrs['user'] = user
        return attrs


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    '''سریالایزر سفارشی برای دریافت جفت توکن JWT'''
    def validate(self, attrs):
        validated_data = super().validate(attrs)
        # میتوانی فیلدهای سفارشی هم اینجا اضافه کنی
        validated_data.update({'user_id': self.user.id, 'email': self.user.email})#به این روش هم میتوانی فیلدهای سفارشی اضافه کنی یا
        # validated_data['email'] = self.user.email #یا به این روش میتوانی فیلدهای سفارشی اضافه کنی
        # validated_data['user_id'] = self.user.id
        # validated_data['test_field'] = 'This is a custom field'
        # print(validated_data)
        return validated_data
    
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True , max_length=255, write_only=True)
    new_password = serializers.CharField(required=True , max_length=255, write_only=True)
    new_password1 = serializers.CharField(required=True , max_length=255, write_only=True)
    
    def validate(self , attrs):
        '''این متد برای اعتبار سنجی فیلدها استفاده میشود'''
        if attrs.get('new_password') != attrs.get('new_password1'):
            # اگر رمز عبور جدید با تکرار آن مطابقت نداشت خطا میدهد
            raise serializers.ValidationError(
                {'new_password Confirmation' :
                'new_password dosn,t match(دو تا پسوردات هنوز با هم قهرن؛ یکسانشون کن)رمز اولت با رمز کانفرم شدت باهم قهرند!)'}
                )
        try :
            validate_password(attrs.get('new_password'))
        except DjVE as e: # اگر رمز عبور استانداردهای اعتبار سنجی را نداشت همه ی خطاهای مربوطه را میگیرد و به عنوان یک آبجکت(e) برمیگرداند
            raise serializers.ValidationError({'new_password':list(e.messages)})
              #این خطاها را به صورت یک لیست از پیام ها به کلاینت برمیگرداند
            
        return super().validate(attrs)# ادامه ی اعتبار سنجی را به متد والد میسپارد و نتیجه را برمیگرداند
    
class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email')
    class Meta:
        model = Profile
        fields = ['id', 'email', 'first_name', 'last_name','image', 'description']
        
        
        