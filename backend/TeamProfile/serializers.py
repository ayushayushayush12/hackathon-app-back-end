from rest_framework import serializers
from TeamProfile.models import TeamProfile

class TeamProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamProfile
        fields = ('TeamId',
                  'TeamName',
                  'HSorColl',
                  'Names',
                  'Schools', 
                  'Grades',
                  'Struggle',
                  'IdeaProject',
                  'Location',
                  'ContactInfo',
                  'PhoneNumber')