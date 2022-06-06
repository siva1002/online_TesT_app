from django.urls import path
from.views import *
urlpatterns=[
    path('',SignupView.as_view()),
    path('login/',SigninView.as_view()),
    path('login/staff/<int:pk>',AdminEditView.as_view()),
    path('login/stafflist',AdminView.as_view())
]