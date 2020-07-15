from django.shortcuts import render

# Create your views here.
def premium_info(request):

    context = {
        'stripe_public_key': 'pk_test_Xny4SfQ3je684fNr2E6YMCSp00VgEdfufp',
        'client_secret': 'test client secret',
    }

    return render(request, 'premium/premium_info.html', context)