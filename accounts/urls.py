from django.urls import path,re_path

from academics.views import QuestionAddView, QuestionsView
from.views import *
urlpatterns=[
    path('',SignupView.as_view()),
    path('login/',LoginView.as_view()),
    path('student-profile/<int:pk>/',StudentProfileView.as_view()),
    path('user-details/',UserDetailsView.as_view()),
    path('user-details/<int:pk>/',UserDetailsEditView.as_view()),
    path('otp/',OtpverifyView.as_view()),
    path('logout/',LogOut.as_view()),
    path('question/',QuestionAddView.as_view()),
    path('log',SimpleLoginView.as_view())
  
]