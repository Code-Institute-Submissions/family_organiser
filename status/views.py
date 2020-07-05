from django.shortcuts import render
from .models import Status

# Create your views here.
def news_feed(request):
    """
    Will show users all their friends posts
    """
    news_feed = Status.objects.all()


    context = {
        'news_feed': news_feed,
    }


    return render(request, 'status/news_feed.html', context)