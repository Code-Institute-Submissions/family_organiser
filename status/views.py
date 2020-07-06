from django.shortcuts import render, redirect
from .models import Status, Comment
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

    news_feed = sorted(news_feed, key = lambda x: x.created_date, reverse=True)

    context = {
        'news_feed': news_feed,
    }

    return render(request, 'status/news_feed.html', context)

def update_status(request, operation, pk):
    """
    Add the users status to the database
    """
    if operation == 'add':
        status = Status(
            user = request.user,
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            likes = 0,
            image = request.FILES.get('image'),
        )
        status.save()

    elif operation == 'remove':
        status = Status.objects.get(pk=pk)
        status.delete()

    return redirect('profile')

def like_status(request, pk):
    """
    Add a like to the users status
    """
    status = Status.objects.get(pk=pk)

    liked_by = status.liked_by.all()
    like_post = True

    for users in liked_by:
        if users == request.user:
            like_post = False

    if like_post:
        status.liked_by.add(request.user)
        status.likes = status.likes + 1
        status.save()

    return redirect('news_feed')

def add_comment(request, pk):
    status = Status.objects.get(pk=pk)

    print(request.POST.get('comment'))

    comment = Comment(
        comment = request.POST.get('comment'),
        author = request.user,
    )
    comment.save()

    status.comment.add(comment)


    return redirect('news_feed')