
from dataclasses import fields
from rest_framework import serializers
from .models import Grade,Subject,Chapter
from django.shortcuts import get_list_or_404
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.mail import send_mail

class SubjectSerializer(serializers.ModelSerializer):
       class Meta:
           model=Chapter
           fields='__all__'

    
        
