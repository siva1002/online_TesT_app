from django.urls import path
from.views import *
urlpatterns=[
    path('',ChaptersView.as_view()),
    path('edit/<int:pk>',ChapterEditView.as_view())
]