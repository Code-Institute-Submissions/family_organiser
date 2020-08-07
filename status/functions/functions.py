from user.models import Friend, UserProfile
from status.models import Status, Comment, CommentNotification, LikeNotification

def get_all_friends(request):
    """
    Get all the users friend.
    """
    try:
        friends = Friend.objects.get(current_user=request.user)
        all_friends = friends.users.all()
    except:
        all_friends = []

    return all_friends

def get_news_feed(request):
    """
    Get the current users and friends posts and sort them in order by date.
    """
    news_feed = []

    for friend in get_all_friends(request):
        status = Status.objects.filter(user=friend)
        for post in status:
            news_feed.append(post)

    # Get all the current users status
    try:
        posts = Status.objects.filter(user=request.user)
    except:
        posts = []

    for post in posts:
        news_feed.append(post)

    # Sort all status by data
    news_feed = sorted(news_feed, key = lambda x: x.created_date, reverse=True)

    return news_feed

def create_comment_and_status_notification(request, pk):
    # Get the status that has been commented on
    status = Status.objects.get(pk=pk)

    # Create the new comment and save it to the database
    users_comment = request.POST.get('comment')
    author = request.user
    author_profile = UserProfile.objects.get(user=request.user)

    comment = Comment(
        comment = users_comment,
        author = author,
        author_profile = author_profile,
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

    return None

def add_like_and_notification(request, pk):
    
    status = Status.objects.get(pk=pk)
    liked_by = status.liked_by.all()

    # If user hasn't liked the post add them to liked_by and add 1 to the likes
    if request.user not in liked_by.all():
        status.liked_by.add(request.user)
        status.likes = status.likes + 1
        status.save()
        print('like post')

        # Send a notification to the status owner to tell them their status has been liked on.
        try:
            LikeNotification.objects.get(user=status.user, status=status, liker=request.user)
        except:
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

    return None