from django.shortcuts import render
from user.models import Friend
from .models import Message
from django.contrib.auth.models import User

# Create your views here.
def start_conversation(request):
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

    return render(request, 'message/start_conversation.html', context)

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