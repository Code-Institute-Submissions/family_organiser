from django.shortcuts import render
from message.functions.functions import get_searched_users
from .forms import EventForm

# Create your views here.
def create_event(request):
    """
    Create a new event and invite friends to the created event.
    """
    # Find the friends searched by the user.
    if request.method == 'GET':
        searched_users = get_searched_users(request)
    else:
        searched_users = []

    # Create the event.
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES)
            event_form = form.save(commit=False)
            event_form.event_creator = request.user
            event_form.save()

    context = {
        'searched_users': searched_users,
        'create_event_form': EventForm,
    }

    return render(request, 'event/create_event.html', context)