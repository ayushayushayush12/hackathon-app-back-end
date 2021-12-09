from django.conf.urls import url
from TeamSubmission import views


urlpatterns=[
    url(r'^teamSubmission/$',views.teamSubmissionApi),
    url(r'^teamSubmission/([0-9]+)$',views.teamSubmissionApi),
    url(r'^Viewteams/$',views.teamSubmissionApi),
    url(r'^Viewteams/([0-9]+)$',views.teamSubmissionApi)
]