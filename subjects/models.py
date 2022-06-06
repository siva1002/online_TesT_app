from django.db import models
from django.core.validators import MinLengthValidator,MaxValueValidator
# Create your models here.
class Grade(models.Model):
    grade = models.IntegerField(
    validators=[
    MaxValueValidator(12)
    ]
    )
class Subject(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=15)
    grade = models.ForeignKey(Grade,on_delete=models.SET_NULL,null =True)
    code = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class Chapter(models.Model):
    subject = models.CharField(max_length=20)
    chapter_no = models.IntegerField()
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name    