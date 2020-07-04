from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import FriendRequests
from django.db.models import Q

def profile(request):
    """
    Display the users profile
    """
    return render(request, 'user/profile.html')

def requests(request):
    """
    Shows the users sent friend requests for shopping and todo list
    """
    friend_requests = FriendRequests.objects.filter(to_user=request.user.pk)

    context = {
        'friend_requests': friend_requests,
    }
    return render(request, 'user/requests.html', context)

def create_friend_request(request, pk):
    """
    Takes the request from the user and saves the requests to the database
    """
    requested_user = User.objects.get(pk=pk)
    FriendRequests.objects.create(from_user=request.user, to_user=requested_user)

    return redirect('find_users')


def find_users(request):
    """
    Search for other users and send a friend request
    """
    if request.method == 'GET':
        try:
            query = request.GET['q']
            queries = Q(username=query) | Q(first_name=query) | Q(last_name=query)
            all_users = User.objects.filter(queries)
            print('search')
        except:
            all_users = User.objects.all()

    context = {
        'all_users': all_users,
    }

    return render(request, 'user/find_users.html', context)