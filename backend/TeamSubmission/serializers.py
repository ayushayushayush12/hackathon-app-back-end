from rest_framework import serializers
from TeamSubmission.models import TeamSubmission
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Login2
class TeamSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamSubmission
        fields = ('TeamId',
                  'VideoLink',
                  'GithubLink',
                  'ProjectIdea',
                  'CodingLanguages')
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class Login2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Login2
        fields = ['id', 'title']
       

