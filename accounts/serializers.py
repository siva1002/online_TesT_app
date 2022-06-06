
from rest_framework import serializers
from .models import User,Profile
from django.shortcuts import get_list_or_404
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.permissions import BasePermission,IsAdminUser
class IsStaffUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)



status_choice={
    ('is_student','is_student'),
    ('is_staff','is_staff'),
    ('is_admin','is_admin')
}


class SignupSerializer(serializers.Serializer):
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=10)
    register_number = serializers.CharField(max_length=15)
    date_of_birth = serializers.DateField()
    user_type = serializers.ChoiceField(
        choices = status_choice,
        default='1'
    )
    first_name = serializers.CharField(max_length=15)
    last_name = serializers.CharField(max_length=15)
    full_name =serializers.CharField(max_length=30)
    standard = serializers.IntegerField()
    section = serializers.CharField(max_length=2)
    address = serializers.CharField(max_length=45)

    def create(self, validated_data):
        email = validated_data.pop("email")
        phone = validated_data.pop("phone")
        register_number = validated_data.pop("register_number")
        date_of_birth = validated_data.pop("date_of_birth")
        user_type = validated_data.pop("user_type")
        first_name = validated_data.pop("first_name")
        last_name = validated_data.pop("last_name")        
        full_name = validated_data.pop("full_name")
        standard = validated_data.pop("standard")
        section = validated_data.pop("section")
        address = validated_data.pop("address")

        user =   User.objects.create(email =email,phone=phone,date_of_birth=date_of_birth,register_number=register_number)
        if user_type == 'is_admin':
            user.is_admin =True
            user.is_staff=True
        elif user_type=='is_staff':
            user.is_staff=True
        else:
            user.is_student=True
        user.save()
        # subject = 'welcome to myapp'
        # message = f'Hi {user.username}, thank you for registering in our new app'
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = [user.email,]
        # send_mail(subject,message,email_from,recipient_list)
        Profile.objects.create(user=user,first_name=first_name,last_name=last_name,standard=standard,section=section,address=address, full_name=full_name)
        return user
class SigninSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','phone']
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
