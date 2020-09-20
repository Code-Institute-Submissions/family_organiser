from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Status, Comment, CommentNotification, LikeNotification
from user.models import Friend, UserProfile
from django.utils import timezone
from .functions.functions import *
from user.functions.functions import get_users_profile
from .forms import StatusForm

# Create your views here.
@login_required
def news_feed(request):
    """
    Will show users all their friends posts
    """

    all_friends = get_all_friends(request)
    news_feed = get_news_feed(request)
    user_profile = get_users_profile(request.user.id)

    context = {
        'news_feed': news_feed,
        'user_profile': user_profile,
        'status_form': StatusForm,
    }

    return render(request, 'status/news_feed.html', context)

@login_required
def update_status(request, operation, pk, redirect_user):
    """
    Add the users status to the database
    """

    # Add the status to the database, else remove the status from the database
    if operation == 'add':
        form = StatusForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

    elif operation == 'remove':
        status = get_object_or_404(Status, pk=pk)
        status.delete()

    if redirect_user == 'profile':
        return redirect('profile')
    if redirect_user == 'news_feed':
        return redirect('news_feed')

@login_required
def like_status(request, pk):
    """
    Add a like to the users status
    """

    if request.is_ajax():
        add_like_and_notification(request, pk)

    return redirect('news_feed')

@login_required
def add_comment(request, pk, redirect_user):
    """
    Add a comment to the select status and send a notification to the user.
    """

    if request.is_ajax():
        create_comment_and_status_notification(request, pk)
   
    if redirect_user == 'profile':
        return redirect('profile')
    if redirect_user == 'news_feed':
        return redirect('news_feed')

@login_required
def view_status(request, pk):
    """
    Take the user to a page that shows one status from their notificats or from the news feed.
    """

    status = Status.objects.get(pk=pk)
    user_profile = get_users_profile(request.user.id)

    context = {
        'news_feed': [status],
        'user_profile': user_profile,
    }

    return render(request, 'status/view_status.html', context)