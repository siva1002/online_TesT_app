from django.urls import path
from.views import *
urlpatterns=[
    path('',SignupView.as_view()),
    path('login/',LoginView.as_view()),
    path('student-profile/<int:pk>/',StudentProfileView.as_view()),
    path('user-details/',UserDetailsView.as_view()),
    path('user-details/<int:pk>/',UserDetailsEditView.as_view())
]