from django.conf.urls import url
from TeamSubmission import views


urlpatterns=[
    url(r'^teamSubmission/$',views.teamSubmissionApi),
    url(r'^teamSubmission/([0-9]+)$',views.teamSubmissionApi)
]