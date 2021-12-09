from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from TeamProfile.models import TeamProfile
from TeamProfile.serializers import TeamProfileSerializer

from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def teamProfileApi(request,id=0):
    if request.method=='GET':
        teamProfile = TeamProfile.objects.all()
        teamProfileSerializer = TeamProfileSerializer(teamProfile, many=True)
        return JsonResponse(teamProfileSerializer.data, safe=False)

    elif request.method=='POST':
      teamProfile_data=JSONParser().parse(request)
      teamProfile_serializer = TeamProfileSerializer(data=teamProfile_data)
      if teamProfile_serializer.is_valid():
        teamProfile_serializer.save()
        return JsonResponse("Added Successfully!!" , safe=False)
      return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        teamProfile_data = JSONParser().parse(request)
        teamProfile=TeamProfile.objects.get(TeamId=teamProfile_data['TeamId'])
        teamProfile_serializer=TeamProfileSerializer(teamProfile,data=teamProfile_data)
        if teamProfile_serializer.is_valid():
            teamProfile_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        teamProfile=TeamProfile.objects.get(TeamId=id)
        teamProfile.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

