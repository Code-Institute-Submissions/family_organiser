from django.shortcuts import render, redirect
from .models import Status
from user.models import Friend
from django.utils import timezone

# Create your views here.
def news_feed(request):
    """
    Will show users all their friends posts
    """

    friends = Friend.objects.get(current_user=request.user)
    all_friends = friends.users.all()

    news_feed = []

    for friend in all_friends:
        status = Status.objects.filter(user=friend)
        for post in status:
            news_feed.append(post)

    posts = Status.objects.filter(user=request.user)

    for post in posts:
        news_feed.append(post)

    context = {
        'news_feed': news_feed,
    }

    return render(request, 'status/news_feed.html', context)

def add_status(request):
    """
    Add the users status to the database
    """
    status = Status(
        user = request.user,
        title = request.POST.get('title'),
        content = request.POST.get('content'),
        likes = 0,
        image = request.FILES.get('image'),
    )
    status.save()

    return redirect('profile')