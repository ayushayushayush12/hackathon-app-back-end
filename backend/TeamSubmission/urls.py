from django.conf.urls import url
from TeamSubmission import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import UserViewSet, Login2ViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('login2', Login2ViewSet)


urlpatterns=[
    url(r'^teamSubmission/$',views.teamSubmissionApi),
    url(r'^teamSubmission/([0-9]+)$',views.teamSubmissionApi),
    path('', include(router.urls)),
    
]