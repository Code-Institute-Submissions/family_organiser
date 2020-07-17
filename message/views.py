from django.shortcuts import render
from user.models import Friend
from .models import Message
from django.contrib.auth.models import User
from user.models import UserProfile
from django.db.models import Q

# Create your views here.
def new_conversation(request):

    if request.method == 'GET':

        try:

            query = request.GET['q']
            queries = Q(username__startswith=query) | Q(first_name__startswith=query) | Q(last_name__startswith=query) | Q(username__startswith=query.capitalize()) | Q(first_name__startswith=query.capitalize()) | Q(last_name__startswith=query.capitalize())
            users_friends = Friend.objects.get(current_user=request.user)
            all_users = users_friends.users.filter(queries)

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

    return render(request, 'message/new_conversation.html', context)

def select_conversation(request):
    """
    Continue a coversation that has already been started.
    """
    # If user isn't logged in return to the home page.
    if request.user.is_anonymous:
        return redirect('home')


    try:
        friends = Friend.objects.get(current_user=request.user)
        friends_list = friends.users.all()
    except:
        friends_list = []

    context = {
        'friends': friends_list,
    }

    return render(request, 'message/select_conversation.html', context)

def conversation(request, pk):
    """
    Conversation page where users will see all their message between themself and the recipient,
    and be able to send new messages.
    """
    # If user isn't logged in return to the home page.
    if request.user.is_anonymous:
        return redirect('home')
        

    message_user = User.objects.get(pk=pk)

    if request.method == 'POST':
        users_message = request.POST.get('message')

        new_message = Message(
            message = users_message,
            sent_from = request.user,
            sent_to = message_user,
        )
        new_message.save()

    messages_from_recipient = Message.objects.filter(sent_from=message_user, sent_to=request.user)
    message_from_current_user = Message.objects.filter(sent_to=message_user, sent_from=request.user)
    
    conversation_messages = []

    for message in messages_from_recipient:
        conversation_messages.append(message)

    for message in message_from_current_user:
        conversation_messages.append(message)

    conversation_messages = sorted(conversation_messages, key = lambda x: x.created_date)

    context = {
        'message_user': message_user,
        'messages': conversation_messages,
    }

    return render(request, 'message/conversation.html', context)