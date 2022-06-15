from dataclasses import field
from rest_framework import serializers
from .models import Grade,Subject,Chapter,Question,Answers
questiontype_choice={

('MCQ','MCQ'),

('Fill_in_the_blanks','Fill_in_the_blanks'),

('Match_the_following','Match_the_following')

}
cognitive_level={

('Knowledge','Knowledge'),

('Comprehension','Comprehension'),

('Application','Application')

}
difficulty_level={

('Easy','Easy'),

('Medium','Medium'),

('Hard','Hard')

}


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
# class AnswerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Answers
#         fields=('option_a','option_b','option_c','option_d','answer')
# class Questionserializer(serializers.ModelSerializer):
#     answer=AnswerSerializer()
#     class Meta:
#         model=Question
#         fields=['grade','subject','chapter','question','question_type','difficulty_level','cognitive_level','answer']
#     def create(self,validated_data):
#         ans=validated_data.pop('answer')
#         q=Question.objects.create(**validated_data)
#         Answers.objects.create(**ans)
#         return q
class Questionserializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields=('grade','subject','chapter','question','question_type','difficulty_level','cognitive_level')
class AnswerSerializer(serializers.ModelSerializer):
    question=Questionserializer()
    class Meta:
        model=Answers
        fields=['question','option_a','option_b','option_c','option_d','answer']
    def create(self,validated_data):
        question=validated_data.pop('question')
        q=Question.objects.create(**question)
        Answers.objects.create(**validated_data)
        return q
class QuestionViewSerializer(serializers.Serializer):
    grade = serializers.IntegerField()
    subject = serializers.CharField()
    no_of_question=serializers.IntegerField()

