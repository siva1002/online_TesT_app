from dataclasses import field
from rest_framework import serializers
from .models import Grade,Subject,Chapter



class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'

class ChapterViewSerializer(serializers.Serializer):
    grade = serializers.IntegerField()
    subject = serializers.CharField()