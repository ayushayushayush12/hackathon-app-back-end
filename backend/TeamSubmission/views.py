from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from TeamSubmission.models import TeamSubmission
from TeamSubmission.serializers import TeamSubmissionSerializer

from django.core.files.storage import default_storage
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserSerializer, Login2Serializer
from .models import Login2

# Create your views here.
@csrf_exempt
def teamSubmissionApi(request,id=0):
    if request.method=='GET':
        teamSubmission = TeamSubmission.objects.all()
        teamSubmissionSerializer = TeamSubmissionSerializer(teamSubmission, many=True)
        return JsonResponse(teamSubmissionSerializer.data, safe=False)

    elif request.method=='POST':
      teamSubmission_data=JSONParser().parse(request)
      teamSubmission_serializer = TeamSubmissionSerializer(data=teamSubmission_data)
      if teamSubmission_serializer.is_valid():
        teamSubmission_serializer.save()
        return JsonResponse("Added Successfully!!" , safe=False)
      return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        teamSubmission_data = JSONParser().parse(request)
        teamSubmission=TeamSubmission.objects.get(TeamSubmissionId=teamSubmission_data['TeamSubmissionId'])
        teamSubmission_serializer=TeamSubmissionSerializer(teamSubmission,data=teamSubmission_data)
        if teamSubmission_serializer.is_valid():
            teamSubmission_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        teamSubmission=TeamSubmission.objects.get(TeamSubmissionId=id)
        teamSubmission.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Login2ViewSet(viewsets.ModelViewSet):
    queryset = Login2.objects.all()
    serializer_class = Login2Serializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

