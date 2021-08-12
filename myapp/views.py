from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages

# Create your views here.
def index(request):
    events = event.objects.all()
    return render(request, 'index.html', {'events' : events})

def create_event(request):
    if request.method == 'POST':
        print(request.FILES)
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event created successfully')
        else:
            messages.warning(request, 'Invalid details')
    return render(request, 'create_event.html')

def update(request, id):
    eventItem = event.objects.filter(id=id).first()
    eventItem.is_liked = not eventItem.is_liked
    eventItem.save()
    return redirect('index')