from django.conf.urls import url
from TeamProfile import views


urlpatterns=[
   url(r'^teamProfile/$',views.teamProfileApi),
   url(r'^teamProfile/([0-9]+)$',views.teamProfileApi)
]