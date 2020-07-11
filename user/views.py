from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from status.models import Status, CommentNotification, LikeNotification
from shopping.models import Item, Category, PartnerRequest
from .models import FriendRequests, Friend, UserProfile
from django.db.models import Q

def profile(request):
    """
    Display the users profile
    """
    # Find friend or turn a empty list if none.
    try:
        friends = Friend.objects.get(current_user=request.user)
        all_friends = friends.users.all()
    except:
        all_friends = []

    friend_requests = FriendRequests.objects.filter(to_user=request.user)

    partner_requests = PartnerRequest.objects.filter(to_user=request.user)

    # Find user profile or create a friend list and user profile if new user.
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except:
        user_profile = UserProfile(
            user = request.user,
            age = 18,
            profile_image = '',
            bio = "Click add on your profile image to finish set up!",
            premium = False,
        )
        user_profile.save()

        friends_list = Friend(
            current_user = request.user,
        )
        friends_list.save()

    # find all status created by the current user
    news_feed = Status.objects.filter(user=request.user).order_by('created_date').reverse()

    # item categories
    item_categories = Category.objects.filter(user=request.user)

    # get all items
    items = Item.objects.filter(user=request.user)

    context = {
        'friend_count': len(all_friends),
        'friend_requests': len(friend_requests),
        'partner_requests': len(partner_requests),
        'user_profile': user_profile,
        'news_feed': news_feed,
        'item_categories': item_categories,
        'items': items,
    }


    return render(request, 'user/profile.html', context)


def find_users(request):
    """
    Search for other users and send a friend request
    """
    if request.method == 'GET':
        try:
            query = request.GET['q'].capitalize()
            queries = Q(username__startswith=query) | Q(first_name__startswith=query) | Q(last_name__startswith=query) | Q(username__startswith=query.capitalize()) | Q(first_name__startswith=query.capitalize()) | Q(last_name__startswith=query.capitalize())
            all_users = User.objects.filter(queries)
        except:
            all_users = []

    friends = Friend.objects.get(current_user=request.user)
    all_friends = friends.users.all()

    context = {
        'all_users': all_users,
        'friends': all_friends,
    }

    return render(request, 'user/find_users.html', context)

def create_friend_request(request, pk):
    """
    Takes the request from the user and saves the request to the database
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

def notifications(request):
    """
    Shows the users sent friend requests for shopping and todo list
    """

    # Reset the users notifications to zero
    user_profile = UserProfile.objects.get(user=request.user)
    user_profile.status_notification = 0
    user_profile.save()

    # get like and comment notifications and order them by date
    notifications = []

    comment_notifications = CommentNotification.objects.filter(user=request.user)

    for notification in comment_notifications:
        notifications.append(notification)

    like_notifications = LikeNotification.objects.filter(user=request.user)

    for notification in like_notifications:
        notifications.append(notification)
   
    notifications = sorted(notifications, key = lambda x: x.created_date, reverse=True)

    # Find friend requests
    friend_requests = FriendRequests.objects.filter(to_user=request.user)

    # find partner requests
    partner_requests = PartnerRequest.objects.filter(to_user=request.user)

    context = {
        'friend_requests': friend_requests,
        'partner_requests': partner_requests,
        'notifications': notifications,
    }
    return render(request, 'user/notifications.html', context)


def update_friends(request, operation, pk, request_id):
    """
    Add or remove the chosen user from or too their friends list
    """

    new_friend = User.objects.get(pk=pk)

    try:
        friend_request = FriendRequests.objects.get(pk=request_id)
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

def settings(request):
    """
    Edit account details
    """
    user_profile = UserProfile.objects.get(user=request.user)

    context = {
        'user_profile': user_profile,
    }

    return render(request, 'user/settings.html', context)

def change_profile_image(request):
    """
    Change and save the users new profile image
    """
    user_profile = UserProfile.objects.get(user=request.user)

    profile_image = request.FILES.get('profile_image')
    user_profile.profile_image = profile_image
    user_profile.save()

    return redirect('profile')

def change_profile_details(request):
    """
    Change the profile details if changed by the user
    """
    user_profile = UserProfile.objects.get(user=request.user)

    # get the data from the form       
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    age = request.POST.get('age')
    bio = request.POST.get('bio')
    # update the users information
    
    user_profile.first_name = first_name
    user_profile.last_name = last_name
    user_profile.username = username
    user_profile.age = age
    user_profile.bio = bio

    user_profile.save()

    return redirect('profile')