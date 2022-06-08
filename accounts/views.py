from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import login,logout
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK,HTTP_404_NOT_FOUND,HTTP_400_BAD_REQUEST,HTTP_201_CREATED
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from.models import User,Profile
from.serializers import SigninSerializer, SignupSerializer,ProfileSerializer,UserDetailsSerializer
from .permission import IsAdminUser,IsStaffUser
from .auth_backend import PasswordlessAuthBackend

# Create your views here.


class SignupView(CreateAPIView):
    serializer_class=SignupSerializer

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success"},status=HTTP_201_CREATED)
        return Response({"status": "failure", "data": serializer.errors})


class LoginView(APIView):
    serializer_class=SigninSerializer
    def post(self,request):
        email=request.data.get('email')
        phone=request.data.get('phone')
        if email and phone:
            try:
                user=PasswordlessAuthBackend.authenticate(self,email=email,phone=phone)
            except:
                  return Response({"status": "User doesn't exits"}, status=HTTP_400_BAD_REQUEST)
            token, created = Token.objects.get_or_create(user=user)
            if user:
                login(request,user)
                return Response({"status": "success"}, status=HTTP_200_OK)
            return Response({"status": "Not found"}, status=HTTP_404_NOT_FOUND)
        return Response({"status": "failed"}, status=HTTP_400_BAD_REQUEST)


class StudentProfileView(RetrieveUpdateAPIView):
    serializer_class=ProfileSerializer
    queryset=Profile.objects.filter()

    def retrieve(self,request,pk):
        if self.request.user.user_type == 'is_student':
            queryset=get_object_or_404(Profile,pk=pk)
        else:
            return Response({"status": "you don't have a permissions"}, status=HTTP_400_BAD_REQUEST)
        serializer = ProfileSerializer(queryset)
        return Response(serializer.data)

    def update(self, request,pk):
        profile = Profile.objects.get(pk=pk)
        serializer = ProfileSerializer(profile,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class UserDetailsView(ListAPIView):

    serializer_class=UserDetailsSerializer

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'is_student':
            queryset = User.objects.get(id = user.id)
        elif user.user_type == 'is_staff':
            queryset = User.objects.filter(user_type = 'is_student')
        elif user.user_type == 'is_admin':
            queryset = User.objects.all()
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserDetailsSerializer(queryset, many=True)
        return Response(serializer.data)


class UserDetailsEditView(RetrieveUpdateDestroyAPIView):

    serializer_class=UserDetailsSerializer
    permission_classes = [IsStaffUser | IsAdminUser]
    queryset=User.objects.all()


    def retrieve(self,request,pk):
        if self.request.user.id == pk:
            user = User.objects.get(pk=pk)
        else:
            try:
                if self.request.user.user_type == 'is_admin':
                    try:
                        user = User.objects.get(user_type = 'is_staff',pk=pk)
                    except: 
                        user = User.objects.get(user_type = 'is_student',pk=pk)
                elif self.request.user.user_type == 'is_staff':
                    user = User.objects.get(user_type = 'is_student',pk=pk) 
            except:
                return Response({"status": "User doesn't exits or you don't have a permissions"}, status=HTTP_400_BAD_REQUEST)
        serializer = UserDetailsSerializer(user)
        return Response(serializer.data)
