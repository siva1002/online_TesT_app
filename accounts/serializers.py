from rest_framework import serializers
from django.shortcuts import get_list_or_404
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.mail import send_mail
from .models import Profile


User = get_user_model()


# class User_type(enum.Enum):
#    is_student = "is_student"
#    is_staff = "is_staff"
#    is_admin = "is_admin"

usertype_choice={
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
        choices = usertype_choice,
        default='0'
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
        user =   User.objects.create(email =email,phone=phone,date_of_birth=date_of_birth,register_number=register_number,user_type = user_type)
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


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name','last_name','full_name',"standard","section","address"]


class UserDetailsSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ['id','email','phone','register_number','date_of_birth','is_active','user_type','created_at','profile']
        read_only_fields = ['id','created_at','user_type']
    
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile
        instance.email = validated_data.get('email', instance.email)
        instance.register_number = validated_data.get('register_number', instance.register_number)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()

        profile.first_name = profile_data.get(
            'first_name',
            profile.first_name
        )
        profile.last_name = profile_data.get(
            'last_name',
            profile.last_name
        )
        profile.full_name = profile_data.get(
            'full_name',
            profile.full_name
        )
        profile.standard = profile_data.get(
            'standard',
            profile.standard
        )
        profile.section = profile_data.get(
            'section',
            profile.section
        )
        profile.address = profile_data.get(
            'address',
            profile.address
        )        
        profile.save()

        return instance