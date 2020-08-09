from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from user.models import Friend
from .models import Message, MessageNotification
from django.contrib.auth.models import User
from user.models import UserProfile
from django.db.models import Q
from .functions.functions import *

# Create your views here.
@login_required
def new_conversation(request):
    """
    Search the database for users and start new conversations.
    """
    if request.method == 'GET':
        searched_users = get_searched_users(request)

    all_friends = get_all_friends(request)

    context = {
        'searched_users': searched_users,
        'friends': all_friends,
    }

    return render(request, 'message/new_conversation.html', context)

@login_required
def select_conversation(request):
    """
    Continue a coversation that has already been started.
    """

    current_conversation_dicts = get_current_conversation_dict(request)
    new_message_conversation = MessageNotification.objects.filter(user=request.user)

    context = {
        'conversations': current_conversation_dicts,
        'new_message_conversation': new_message_conversation,
    }

    return render(request, 'message/select_conversation.html', context)

@login_required
def conversation(request, pk):
    """
    Display conversation page where users will see all their message between themself and the recipient,
    and be able to send new messages.
    """

    message_user = User.objects.get(pk=pk)

    notifications_from_recipient = MessageNotification.objects.filter(sent_from=pk)
    for notifications in notifications_from_recipient:
        notifications.delete()

    if request.method == 'POST':
        users_message = request.POST.get('message')

        new_message = Message(
            message = users_message,
            sent_from = request.user,
            sent_to = message_user,
        )
        new_message.save()

        message_notification = MessageNotification(
            user = message_user,
            sent_from = request.user,
            notifications = 1,
        )
        message_notification.save()
    
    conversation_messages = get_conversation_messages(request, message_user)

    context = {
        'message_user': message_user,
        'messages': conversation_messages,
    }

    return render(request, 'message/conversation.html', context)