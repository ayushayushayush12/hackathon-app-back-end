from rest_framework import serializers
from TeamSubmission.models import TeamSubmission

class TeamSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamSubmission
        fields = ('TeamId',
                  'VideoLink',
                  'GithubLink',
                  'ProjectIdea',
                  'CodingLanguages')