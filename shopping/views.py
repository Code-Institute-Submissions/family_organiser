from django.shortcuts import render
from .models import Category, Item

# Create your views here.
def shopping_page(request):

    items = Item.objects.filter(user=request.user)
    categorys = Category.objects.filter(user=request.user)

    context = {
        'items': items,
        'categorys': categorys,
    }

    return render(request, 'shopping/shopping_page.html', context)