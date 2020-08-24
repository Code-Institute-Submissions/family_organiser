from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from status.models import Status, CommentNotification, LikeNotification
from shopping.models import Item, Category, PartnerRequest, Partner
from .models import FriendRequests, Friend, UserProfile, AcceptedFriendRequests
from message.models import MessageNotification, Message
from event.models import EventInvite
from django.db.models import Q
from .functions.functions import *
from shopping.functions.functions import get_partner_requests
from status.forms import StatusForm
from shopping.forms import ItemForm

@login_required
def profile(request):
    """
    Display the users profile, status, shopping items and notifications.
    """

    all_friends = find_friends(request, request.user)
    friend_requests = FriendRequests.objects.filter(to_user=request.user)
    partner_requests = get_partner_requests(request)
    user_profile = get_users_profile(request.user.id)
    news_feed = Status.objects.filter(user=request.user).order_by('created_date').reverse()
    item_categories = Category.objects.filter(user=request.user)
    all_items = get_all_shopping_items(request)
    accepted_friend_requests = AcceptedFriendRequests.objects.filter(from_user=request.user)
    message_notification = get_message_notifications(request)

    context = {
        'friend_count': len(all_friends),
        'friend_requests': len(friend_requests),
        'accepted_friend_requests': len(accepted_friend_requests),
        'partner_requests': len(partner_requests),
        'message_notification': message_notification,
        'user_profile': user_profile,
        'news_feed': news_feed,
        'item_categories': item_categories,
        'items': all_items,
        'bio_length': len(user_profile.bio),
        'status_form': StatusForm,
        'item_form': ItemForm,
    }

    return render(request, 'user/profile.html', context)

@login_required
def find_users(request):
    """
    Search for other users and send a friend request
    """

    if request.method == 'GET':
        searched_users = search_users(request)

    user_profile = get_users_profile(request.user.id)

    try:
        friends = Friend.objects.get(current_user=request.user)
        all_friends_query_set = friends.users.all()
        all_friends = []
        for friend in all_friends_query_set:
            all_friends.append(friend.username)
    except:
        all_friends = []

    try:
        friend_requests = FriendRequests.objects.filter(from_user=request.user)
        friend_request_sent = []
        for friend_request in friend_requests:
            friend_request_sent.append(friend_request.to_user.username)
    except:
        friend_request_sent = []

    context = {
        'searched_users': searched_users,
        'friends': all_friends,
        'friend_request_sent': friend_request_sent,
        'user_profile': user_profile,
    }

    return render(request, 'user/find_users.html', context)

@login_required
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

@login_required
def family(request, pk):
    """
    View the list of friends that the users has
    """
    requested_user = get_object_or_404(User, pk=pk)
    user_profile = get_users_profile(request.user.id)

    friends = find_friends(request, requested_user)
    all_friends = find_friends(request, requested_user)

    all_friends_dict = []

    for friend in all_friends:
        user_profile = UserProfile.objects.get(pk=friend.id)

        friend_dict = {
            'first_name': friend.first_name,
            'last_name': friend.last_name,
            'id': friend.id,
            'profile_image': user_profile.profile_image,
        }

        all_friends_dict.append(friend_dict)

    context = {
        'friends': all_friends_dict,
        'requested_user': requested_user,
        'user_profile': user_profile,
    }

    return render(request, 'user/family.html', context)

@login_required
def notifications(request):
    """
    Shows the users sent friend requests for shopping and todo list
    """

    # get like and comment notifications and order them by date
    notifications = get_all_notifications(request)

    # Find friend requests
    friend_requests = FriendRequests.objects.filter(to_user=request.user)

    # find partner requests
    partner_requests = get_partner_requests(request)

    # Reset the users notifications to zero
    user_profile = get_users_profile(request.user.id)
    user_profile.status_notification = 0
    user_profile.accepted_friend_notification = 0
    user_profile.event_notification = 0
    user_profile.save()
    

    context = {
        'friend_requests': friend_requests,
        'partner_requests': partner_requests,
        'notifications': notifications,
        'user_profile': user_profile,
    }
    return render(request, 'user/notifications.html', context)

@login_required
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
        accepted_friend = AcceptedFriendRequests(
            from_user = new_friend,
            to_user = request.user,
        )
        accepted_friend.save()

        new_friend_user_profile = UserProfile.objects.get(user=new_friend)
        new_friend_user_profile.accepted_friend_notification += 1
        new_friend_user_profile.save()

    elif operation == 'remove':
        Friend.remove_friend(request.user, new_friend)
        Friend.remove_friend(new_friend, request.user)

        old_friends_messages = Message.objects.filter(sent_from=new_friend)
        for message in old_friends_messages:
            message.delete()
        old_friends_messages = Message.objects.filter(sent_to=new_friend)
        for message in old_friends_messages:
            message.delete()
        
    return redirect('profile')

@login_required
def settings(request):
    """
    Edit account details
    """

    user_profile = get_users_profile(request.user.id)

    context = {
        'user_profile': user_profile,
    }

    return render(request, 'user/settings.html', context)

@login_required
def change_profile_image(request):
    """
    Change and save the users new profile image
    """

    user_profile = get_users_profile(request.user.id)

    profile_image = request.FILES.get('profile_image')
    user_profile.profile_image = profile_image
    user_profile.save()

    return redirect('profile')

@login_required
def change_profile_details(request):
    """
    Change the profile details if changed by the user
    """

    update_profile_details(request)

    return redirect('profile')

@login_required
def view_user_profile(request, pk):
    """
    Find the a users profile and display their basic 
    information or if current user redirect them to their profile page.
    """
        
    # Find friend or turn a empty list if none.
    find_user = User.objects.get(pk=pk)

    user_profile = get_users_profile(pk)

    if find_user == request.user:
        return redirect('profile')

    try:
        friends = Friend.objects.get(current_user=find_user)
        all_friends = friends.users.all()
    except:
        all_friends = []

    # find all status created by the current user
    news_feed = Status.objects.filter(user=find_user).order_by('created_date').reverse()

    context = {
        'find_user': find_user,
        'friend_count': len(all_friends),
        'user_profile': user_profile,
        'news_feed': news_feed,
        'bio_length': len(user_profile.bio),
    }

    return render(request, 'user/view_user_profile.html', context)

@login_required
def delete_account(request):

    current_user = User.objects.get(username=request.user.username)
    current_user.delete()

    return redirect('home')