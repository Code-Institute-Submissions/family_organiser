from django.shortcuts import render
from message.functions.functions import get_searched_users

# Create your views here.
def create_event(request):
    """
    Create a new event and invite friends to the created event.
    """
    if request.method == 'GET':
        searched_users = get_searched_users(request)

    context = {
        'searched_users': searched_users,
    }

    return render(request, 'event/create_event.html', context)