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
<<<<<<< HEAD
    url(r'^Viewteams/$',views.teamSubmissionApi),
    url(r'^Viewteams/([0-9]+)$',views.teamSubmissionApi)
=======
    path('', include(router.urls)),
    
>>>>>>> 5787d6163622121aad52039b1eb84160d98c8e37
]