from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from status.models import Status, CommentNotification, LikeNotification
from shopping.models import Item, Category, PartnerRequest, Partner
from .models import FriendRequests, Friend, UserProfile, AcceptedFriendRequests
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

    try:
        partner_requests = PartnerRequest.objects.filter(to_user=request.user)
    except:
        partner_requests = []

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

    # Get the current users shopping partners
    try:
        shopping_partners = Partner.objects.get(current_user=request.user)
        shopping_partners_list = shopping_partners.partners.all()
    except:
        shopping_partners = []
        shopping_partners_list = []

    # Get all the current users items
    items = Item.objects.filter(user=request.user).order_by('item')

    all_items = [item for item in items]

    # Add all the users items and their shopping partners items into all_items

    for shopping_partner in shopping_partners_list:
        if not shopping_partner == request.user:
            partners_shopping_list = Item.objects.filter(user=shopping_partner)
            for item in partners_shopping_list:
                all_items.append(item)

    # Add the quantity of any duplicate items
    all_items_no_duplicates = []

    for loop_index, item in enumerate(all_items):
        if loop_index == 0:
            all_items_no_duplicates.append(item)
        else:
            item_is_not_a_copy = True
            for list_item in all_items_no_duplicates:
                if list_item.item == item.item:
                    item_is_not_a_copy = False
                    list_item.quantity += item.quantity

            if item_is_not_a_copy:
                all_items_no_duplicates.append(item)

    # Find the users accepted friend requests 
    accepted_friend_requests = AcceptedFriendRequests.objects.filter(from_user=request.user)

    context = {
        'friend_count': len(all_friends),
        'friend_requests': len(friend_requests),
        'accepted_friend_requests': len(accepted_friend_requests),
        'partner_requests': len(partner_requests),
        'user_profile': user_profile,
        'news_feed': news_feed,
        'item_categories': item_categories,
        'items': all_items_no_duplicates,
    }

    return render(request, 'user/profile.html', context)


def find_users(request):
    """
    Search for other users and send a friend request
    """
    if request.method == 'GET':
        try:
            query = request.GET['q']
            queries = Q(username__startswith=query) | Q(first_name__startswith=query) | Q(last_name__startswith=query) | Q(username__startswith=query.capitalize()) | Q(first_name__startswith=query.capitalize()) | Q(last_name__startswith=query.capitalize())
            all_users = User.objects.filter(queries)
            searched_users = []
            for one_user in all_users:
                user_profile = UserProfile.objects.get(user=one_user)

                user_dict = {
                    'first_name': one_user.first_name,
                    'last_name': one_user.last_name,
                    'username': one_user.username,
                    'id': one_user.id,
                    'user_profile': {
                        'profile_image': user_profile.profile_image,
                    }
                }
                searched_users.append(user_dict)
        except:
            searched_users = []

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
    user_profile.accepted_friend_notification = 0
    user_profile.save()

    # get like and comment notifications and order them by date
    notifications = []

    comment_notifications = CommentNotification.objects.filter(user=request.user)
    like_notifications = LikeNotification.objects.filter(user=request.user)
    accepted_friend_requests = AcceptedFriendRequests.objects.filter(from_user=request.user)

    for notification in comment_notifications:
        notifications.append(notification)

    for notification in like_notifications:
        notifications.append(notification)

    for notification in accepted_friend_requests:
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

def view_user_profile(request, pk):
    """
    Find the a users profile and display their basic 
    information or if current user redirect them to their profile page.
    """
    # Find friend or turn a empty list if none.
    find_user = User.objects.get(pk=pk)

    if find_user == request.user:
        return redirect('profile')

    try:
        friends = Friend.objects.get(current_user=find_user)
        all_friends = friends.users.all()
    except:
        all_friends = []

    friend_requests = FriendRequests.objects.filter(to_user=find_user)

    try:
        partner_requests = PartnerRequest.objects.filter(to_user=find_user)
    except:
        partner_requests = []

    # Find user profile or create a friend list and user profile if new user.
    try:
        user_profile = UserProfile.objects.get(user=find_user)
    except:
        user_profile = UserProfile(
            user = find_user,
            age = 18,
            profile_image = '',
            bio = "Click add on your profile image to finish set up!",
            premium = False,
        )
        user_profile.save()

        friends_list = Friend(
            current_user = find_user,
        )
        friends_list.save()

    # find all status created by the current user
    news_feed = Status.objects.filter(user=find_user).order_by('created_date').reverse()

    # item categories
    item_categories = Category.objects.filter(user=find_user)

    # Get the current users shopping partners
    try:
        shopping_partners = Partner.objects.get(current_user=find_user)
        shopping_partners_list = shopping_partners.partners.all()
    except:
        shopping_partners = []
        shopping_partners_list = []

    # Get all the current users items
    items = Item.objects.filter(user=find_user).order_by('item')

    all_items = [item for item in items]

    # Add all the users items and their shopping partners items into all_items

    for shopping_partner in shopping_partners_list:
        if not shopping_partner == find_user:
            partners_shopping_list = Item.objects.filter(user=shopping_partner)
            for item in partners_shopping_list:
                all_items.append(item)

    # Add the quantity of any duplicate items
    all_items_no_duplicates = []

    for loop_index, item in enumerate(all_items):
        if loop_index == 0:
            all_items_no_duplicates.append(item)
        else:
            item_is_not_a_copy = True
            for list_item in all_items_no_duplicates:
                if list_item.item == item.item:
                    item_is_not_a_copy = False
                    list_item.quantity += item.quantity

            if item_is_not_a_copy:
                all_items_no_duplicates.append(item)

    context = {
        'find_user': find_user,
        'friend_count': len(all_friends),
        'friend_requests': len(friend_requests),
        'partner_requests': len(partner_requests),
        'user_profile': user_profile,
        'news_feed': news_feed,
        'item_categories': item_categories,
        'items': all_items_no_duplicates,
    }

    return render(request, 'user/view_user_profile.html', context)