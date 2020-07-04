from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Q

def profile(request):
    """
    Display the users profile
    """
    return render(request, 'user/profile.html')

def find_users(request):
    """
    Search for other users and send a friend request
    """
    if request.method == 'GET':
        try:
            query = request.GET['q']
            queries = Q(username=query) | Q(first_name=query) | Q(last_name=query)
            all_users = User.objects.filter(queries)
            print('search')
        except:
            all_users = User.objects.all()

    context = {
        'all_users': all_users,
    }

    return render(request, 'user/find_users.html', context)