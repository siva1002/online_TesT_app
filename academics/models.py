from django.db import DatabaseError, models
from django.core.validators import MaxValueValidator
# Create your models here.

class Grade(models.Model):
    grade = models.IntegerField(
        validators=[
            MaxValueValidator(12)
        ]
    )
    def __str__(self):
        return str(self.grade)

class Subject(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=15)
    grade = models.ForeignKey(Grade,on_delete=models.DO_NOTHING,null =True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.grade.grade) + ' ' +self.name

class Chapter(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.DO_NOTHING,null =True)
    chapter_no = models.IntegerField()
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

