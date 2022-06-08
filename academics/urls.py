from django.urls import path
from .views import *
urlpatterns=[
    path('subjects/',SubjectCreate.as_view()),
    path('grades/',GradeView.as_view()),
    path('subjects/<int:pk>/',SubjectEditView.as_view()),
    path('chapters/',ChaptersView.as_view()),
    path('chapter/<int:pk>/',ChapterEditView.as_view()),
    path('',ChaptersOfSubjectsView.as_view())
]