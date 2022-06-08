from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView,ListAPIView,RetrieveAPIView,GenericAPIView,UpdateAPIView
from accounts.permission import IsAdminUser
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import *
from .serializers import SubjectSerializer,ChapterSerializer,GradeSerializer,ChapterViewSerializer
from .models import Subject,Grade,Chapter
# Create your views here.


class GradeView(ListCreateAPIView):
    serializer_class = GradeSerializer
    queryset = Grade.objects.all()
    permission_classes = [IsAdminUser]

    def list(self,request):
        queryset = self.get_queryset()
        serializer = GradeSerializer(queryset,many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer = GradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success"})
        return Response({"status": "failure", "data": serializer.errors})


class SubjectCreate(ListCreateAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAdminUser]

    def list(self,request):
        queryset = self.get_queryset()
        serializer = SubjectSerializer(queryset,many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success"})
        return Response({"status": "failure", "data": serializer.errors})


class SubjectEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = SubjectSerializer
    permission_classes = [IsAdminUser]

    def retrieve(self, request,pk):
        queryset = get_object_or_404(Subject,pk=pk)
        serializer = SubjectSerializer(queryset)
        return Response(serializer.data)
    
    def update(self,request,pk):
        subject = Subject.objects.get(pk=pk)
        serializer = SubjectSerializer(subject,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class ChaptersView(CreateAPIView):

    serializer_class=ChapterSerializer
    queryset= Chapter.objects.all()
    permission_classes=[IsAdminUser]

    def get(self, request, format=None):
        queryset= Chapter.objects.all()
        serializer = ChapterSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ChapterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(HTTP_200_OK)
        return Response({"status": "failure"})


class ChapterEditView(RetrieveUpdateDestroyAPIView):

    serializer_class=ChapterSerializer
    permission_classes=[IsAdminUser]
    queryset = Chapter.objects.all()

    def retrive(self,request,pk):
        try:
            queryset = Chapter.objects.get(pk=pk)
        except:
            return Response({"status": "success"}, status=HTTP_400_BAD_REQUEST)
        serializer = ChapterSerializer(queryset)
        return Response(serializer.data)

    def update(self,request,pk):
        subject = Chapter.objects.get(pk=pk)
        serializer = ChapterSerializer(subject,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
        

class ChaptersOfSubjectsView(APIView):
    serializer_class=ChapterViewSerializer
    def post(self,request):
        grade = request.data.get('grade')
        subject=request.data.get('subject')
        if subject:
            data = []
            try:
                grade = Grade.objects.get(grade=grade)
                subject = Subject.objects.get(name=subject,grade=grade.grade)
                chapters = Chapter.objects.filter(subject=subject)
                for object in chapters:
                    data.append( {
                    "subject" : subject.name,
                    "grade" :subject.grade.grade,
                    "name": object.name,
                    "chapter_no": object.chapter_no,
                    "description": object.description,
                    })

            except:
                return Response({"status": "Not found"}, status=HTTP_404_NOT_FOUND)
            return Response({"status": "success", "data": data}, status=HTTP_200_OK)
        return Response({"status": "failed"}, status=HTTP_400_BAD_REQUEST)

