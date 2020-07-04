from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import FriendRequests, Friend
from django.db.models import Q

def profile(request):
    """
    Display the users profile
    """
    try:
        friends = Friend.objects.get(current_user=request.user)
        all_friends = friends.users.all()
    except:
        all_friends = []

    friend_requests = FriendRequests.objects.filter(to_user=request.user)

    context = {
        'friend_count': len(all_friends),
        'friend_requests': len(friend_requests)
    }


    return render(request, 'user/profile.html', context)


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

    friends = Friend.objects.get(current_user=request.user)
    all_friends = friends.users.all()

    context = {
        'all_users': all_users,
        'friends': all_friends,
    }

    return render(request, 'user/find_users.html', context)

def create_friend_request(request, pk):
    """
    Takes the request from the user and saves the requests to the database
    """
    requested_user = User.objects.get(pk=pk)
    
    try:
        FriendRequests.objects.get(from_user=request.user, to_user=requested_user)
    except:
        FriendRequests.objects.create(from_user=request.user, to_user=requested_user)

    return redirect('find_users')

def family(request):
    """
    View the list of friends that the users has
    """
    friends = Friend.objects.get(current_user=request.user)
    all_friends = friends.users.all()

    context = {
        'friends': all_friends,
    }


    return render(request, 'user/family.html', context)

def requests(request):
    """
    Shows the users sent friend requests for shopping and todo list
    """
    friend_requests = FriendRequests.objects.filter(to_user=request.user)

    context = {
        'friend_requests': friend_requests,
    }
    return render(request, 'user/requests.html', context)


def update_friends(request, operation, pk):
    """
    Add or remove the chosen user from or too their friends list
    """

    new_friend = User.objects.get(pk=pk)

    try:
        friend_request = FriendRequests.objects.get(from_user=pk)
        friend_request.delete()
    except:
        friend_request = None
    
    if operation == 'add':
        Friend.make_friend(request.user, new_friend)
        Friend.make_friend(new_friend, request.user)
    elif operation == 'remove':
        Friend.remove_friend(request.user, new_friend)
        Friend.remove_friend(new_friend, request.user)
        
    return redirect('profile')