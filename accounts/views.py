import email
from urllib import response
from django.shortcuts import render
from.models import User,Profile
from .serializers import SigninSerializer,SignupSerializer,AdminSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,logout
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView,UpdateAPIView,ListAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from rest_framework.status import HTTP_200_OK,HTTP_404_NOT_FOUND,HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework.authtoken.models import Token
# Create your views here.
class SignupView(CreateAPIView):
    serializer_class=SignupSerializer
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success"})
        return Response({"status": "failure", "data": serializer.errors})
class SigninView(APIView):
    serializer_class=SigninSerializer
    queryset=User.objects.all()
    def post(self,request):
        email=request.data.get('email')
        phone=request.data.get('phone')
        if email and phone:
            user=User.objects.get(email=email,phone=phone)
            if user:
                token,created = Token.objects.get_or_create(user=user)
                login(request,user)
                return Response({"status": "success"}, status=HTTP_200_OK)
            elif user and user.is_student==True:
                token,created = Token.objects.get_or_create(user=user)
                login(request,user)
                return Response({"status": "studentlogin-success",'user':request.user.id}, status=HTTP_200_OK)
            return Response({"status": "success"}, status=HTTP_404_NOT_FOUND)
        return Response({"status": "success"}, status=HTTP_400_BAD_REQUEST)
class AdminEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = AdminSerializer
    permission_classes = [IsAdminUser]
    def get(self,request,pk): 
        try:
            queryset = User.objects.get(pk=pk,is_staff=True)
        except:
            return Response({"status": "success"}, status=HTTP_400_BAD_REQUEST)
        serializer = AdminSerializer(queryset)
        return Response({'data':serializer.data})
class AdminView(ListAPIView):
    serializer_class=AdminSerializer
    permission_classes=[IsAdminUser]
    queryset=User.objects.all()
    def list(self, request, format=None):
        queryset= User.objects.filter(is_staff=True)   
        serializer = AdminSerializer(queryset, many=True)
        return Response(serializer.data)


