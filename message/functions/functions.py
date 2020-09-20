from django.db.models import Q
from user.models import Friend, UserProfile
from message.models import Message
from user.functions.functions import get_users_profile

def get_searched_users(request):
    """
    Get users searched from the database
    """
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

    return searched_users

def get_all_friends(request):
    try:
        friends = Friend.objects.get(current_user=request.user)
        all_friends_query_set = friends.users.all()
        all_friends = []
        for friend in all_friends_query_set:
            all_friends.append(friend.username)
    except:
        all_friends = []

    return all_friends

def get_conversation_messages(request, message_user):
    """
    Get the message from the current user and the recipient.
    """
    messages_from_recipient = Message.objects.filter(sent_from=message_user, sent_to=request.user)
    message_from_current_user = Message.objects.filter(sent_to=message_user, sent_from=request.user)
    conversation_messages = []

    for message in messages_from_recipient:
        conversation_messages.append(message)

    for message in message_from_current_user:
        conversation_messages.append(message)

    conversation_messages = sorted(conversation_messages, key = lambda x: x.created_date)
    
    return conversation_messages

def get_current_conversation_dict(request):
    conversations_from = Message.objects.filter(sent_from=request.user)
    conversations_to = Message.objects.filter(sent_to=request.user)
    current_conversations_with_users = []

    for conversation in conversations_from:
        current_conversations_with_users.append(conversation.sent_to)

    for conversation in conversations_to:
        current_conversations_with_users.append(conversation.sent_from)

    current_conversations = []

    for index, conversation in enumerate(current_conversations_with_users):
        if index == 0:
            current_conversations.append(conversation)
        else:
            new_conversation = True
            for list_item in current_conversations:
                if list_item == conversation:
                    new_conversation = False
            if new_conversation:
                current_conversations.append(conversation)

    current_conversation_dicts = []

    for conversation in current_conversations:
        user_profile = get_users_profile(conversation.id)
        conversation_dict = {
            'first_name': conversation.first_name,
            'last_name': conversation.last_name,
            'id': conversation.id,
            'profile_image': user_profile.profile_image,
        }
        current_conversation_dicts.append(conversation_dict)
    
    return current_conversation_dicts