import re
from django.shortcuts import get_object_or_404, render, get_list_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from django.urls import reverse_lazy
from .forms import ResourceForm, MeetingForm

# Create your views here.

def index(request):
    return render(request, 'Club/index.html')


def resource(request):
    resource_list = Resource.objects.all()
    return render(request, 'Club/resources.html', {'resource_list': resource_list})


def meeting(request):
    meeting_list = Meeting.objects.all()
    return render(request, 'Club/meeting.html', {'meeting_list': meeting_list})


def meetingDetail(request, id):
    meeting=get_object_or_404(Meeting, pk=id)
    return render(request, 'Club/meetingdetail.html', {'meeting': meeting})


def resourceDetail(request, id):
    resource=get_object_or_404(Resource, pk=id)
    return render(request, 'Club/resourcedetail.html', {'resource': resource})


def newResource(request):
    form = ResourceForm

    if request.method == 'POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = ResourceForm()
    else:
        form = ResourceForm()
    return render(request, 'Club/newresource.html', {'form': form})


def newMeeting(request):
    form = MeetingForm

    if request.method == 'POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = MeetingForm()
    else:
        form = MeetingForm()
    return render(request, 'Club/newmeeting.html', {'form': form})
