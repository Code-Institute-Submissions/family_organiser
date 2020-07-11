from django.shortcuts import render

# Create your views here.
def premium_info(request):

    return render(request, 'premium/premium_info.html')