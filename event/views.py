from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from message.functions.functions import get_searched_users
from django.contrib.auth.decorators import login_required
from .forms import EventForm
from .models import Event, EventInvite
from .functions.functions import *

@login_required
def menu(request):

    context = {
        
    }

    return render(request, 'event/menu.html', context)

@login_required
def create_event(request):
    """
    Create a new event and invite friends to the created event.
    """
    # Create the event.
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES)
            event_form = form.save(commit=False)
            event_form.event_creator = request.user
            event_form.save()

            return redirect('invite', event_form.pk, 0)

    context = {
        'create_event_form': EventForm,
    }

    return render(request, 'event/create_event.html', context)


@login_required
def invite(request, event_pk, user_pk):
    """
    Invite friends to an event passed into the view.
    """
    # Find the friends searched by the user.
    if request.method == 'GET':
        searched_users = get_searched_users(request)
    else:
        searched_users = []

    event = get_object_or_404(Event, pk=event_pk)
    invited_users = EventInvite.objects.filter(event=event)

    # Send invite to user.
    if request.method == 'POST':
        EventInvite.create_invitation(get_object_or_404(User, pk=user_pk), event)

    context = {
        'event': event,
        'searched_users': searched_users,
        'invited_users': invited_users,
    }

    return render(request, 'event/invite.html', context)

