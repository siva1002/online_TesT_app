from django.shortcuts import render
from rest_framework.response import Response

from subjects.models import Chapter
from .serializers import SubjectSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView,UpdateAPIView,ListAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from rest_framework.status import HTTP_200_OK,HTTP_404_NOT_FOUND,HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404
# Create your views here.
class ChaptersView(CreateAPIView):
    serializer_class=SubjectSerializer
    queryset= Chapter.objects.all()
    permission_classes=[IsAdminUser]
    def get(self, request, format=None):
        queryset= Chapter.objects.all()   
        serializer = SubjectSerializer(queryset, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(HTTP_200_OK)
        return Response({"status": "failure"})
class ChapterEditView(RetrieveUpdateDestroyAPIView):
    serializer_class=SubjectSerializer
    permission_classes=[IsAdminUser]
    queryset = Chapter.objects.all()
    def retrive(self,request,pk):
        try:
            queryset = Chapter.objects.get(pk=pk)
        except:
            return Response({"status": "success"}, status=HTTP_400_BAD_REQUEST)
        serializer = SubjectSerializer(queryset)
        return Response(serializer.data)
    def update(self,request,pk):
        subject = Chapter.objects.get(pk=pk)
        serializer = SubjectSerializer(subject,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
