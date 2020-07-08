from django.shortcuts import render, redirect
from .models import Status, Comment, CommentNotification, LikeNotification
from user.models import Friend, UserProfile
from django.utils import timezone

# Create your views here.
def news_feed(request):
    """
    Will show users all their friends posts
    """

    # Find the current users friends
    friends = Friend.objects.get(current_user=request.user)
    all_friends = friends.users.all()

    # Get all friends status and store them in an array
    news_feed = []

    for friend in all_friends:
        status = Status.objects.filter(user=friend)
        for post in status:
            news_feed.append(post)

    # Get all the current users status
    posts = Status.objects.filter(user=request.user)

    for post in posts:
        news_feed.append(post)

    # Sort all status by data
    news_feed = sorted(news_feed, key = lambda x: x.created_date, reverse=True)

    # get users profile
    user_profile = UserProfile.objects.get(user=request.user)

    context = {
        'news_feed': news_feed,
        'user_profile': user_profile,
    }

    return render(request, 'status/news_feed.html', context)

def update_status(request, operation, pk):
    """
    Add the users status to the database
    """

    # Add the status to the database, else remove the status from the database
    if operation == 'add':
        status = Status(
            user = request.user,
            user_profile = UserProfile.objects.get(user=request.user),
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

    if request.is_ajax():

        status = Status.objects.get(pk=pk)
        liked_by = status.liked_by.all()

        # If user hasn't liked the post add them to liked_by and add 1 to the likes
        if request.user not in liked_by.all():
            status.liked_by.add(request.user)
            status.likes = status.likes + 1
            status.save()
            print('like post')

            # Send a notification to the status owner to tell them their status has been liked on.
            like_notification = LikeNotification(
                user = status.user,
                status = status,
                liker = request.user,
            )
            like_notification.save()

            user_profile = UserProfile.objects.get(user=status.user)
            user_profile.status_notification += 1
            user_profile.save()

        else:
            status.liked_by.remove(request.user)
            status.likes = status.likes - 1
            status.save()
            print('unlike post')


    return redirect('news_feed')

def add_comment(request, pk, redirect):
    """
    Add a comment to the select status and send a notification to the user.
    """
    if request.is_ajax():
        # Get the status that has been commented on
        status = Status.objects.get(pk=pk)

        # Create the new comment and save it to the database
        comment = Comment(
            comment = request.POST.get('comment'),
            author = request.user,
            author_profile = UserProfile.objects.get(user=request.user),
        )
        comment.save()

        # Add the comment to the status
        status.comment.add(comment)

        # Send a notification to the status owner to tell them their status has been commmented on.
        comment_notification = CommentNotification(
            user = status.user,
            status = status,
            commenter = request.user,
        )
        comment_notification.save()

        user_profile = UserProfile.objects.get(user=status.user)
        user_profile.status_notification += 1
        user_profile.save()
   
    if redirect == 'profile':
        return redirect('profile')
    if redirect == 'news_feed':
        return redirect('news_feed')