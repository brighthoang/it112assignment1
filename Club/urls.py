from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resource/', views.resource, name="resource"), 
    path('meeting/', views.meeting, name="meeting"),
    path('meetingdetail/<int:id>', views.meetingDetail, name="meetingdetail"),
    path('resourcedetail/<int:id>', views.resourceDetail, name="resourcedetail"),
    path('newresource/', views.newResource, name='newresource'),
    path('newmeeting/', views.newMeeting, name='newmeeting'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]