from rest_framework import generics
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):#زمان post کردن باید object مان را بسازیم پس:
        serializer = RegisterSerializer(data=request.data)  # ==self.get_serializer(data=request.data)  #ابتدا serializer را با داده های ورودی مقدار دهی میکنیم
        if serializer.is_valid():
          serializer.save()
          data = {
              "email": serializer.validated_data['email']
                  }
          return Response(data, status=status.HTTP_201_CREATED)
       