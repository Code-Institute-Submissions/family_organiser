from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def profile(request):
    """
    Display the users profile
    """
    return render(request, 'user/profile.html')

