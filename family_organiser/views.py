from django.shortcuts import render

def error_404(request, exception):
        context = {
            'error': 'Error 404'
        }
        return render(request,'family_organiser/error.html', context)

def error_500(request,  exception):
        context = {
            'error': 'Error 500'
        }
        return render(request,'family_organiser/error.html', context)

def error_403(request, exception):
    context = {
        'error': 'Error 403'
    }
    return render(request,'family_organiser/error.html', context)

def error_400(request,  exception):
        context = {
            'error': 'Error 400'
        }
        return render(request,'family_organiser/error.html', context)