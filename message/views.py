from django.shortcuts import render
from user.models import Friend

# Create your views here.
def start_conversation(request):

    friends = Friend.objects.get(current_user=request.user)
    friends_list = friends.users.all()

    context = {
        'friends': friends_list,
    }

    return render(request, 'messages/start_conversation.html', context)