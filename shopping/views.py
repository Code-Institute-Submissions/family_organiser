from django.shortcuts import render, redirect
from .models import Category, Item

# Create your views here.
def shopping_page(request):

    items = Item.objects.filter(user=request.user)
    categories = Category.objects.filter(user=request.user)

    context = {
        'items': items,
        'categories': categories,
    }

    return render(request, 'shopping/shopping_page.html', context)

def add_item(request):

    if request.method == 'POST':

        item = request.POST.get('item')
        quantity = request.POST.get('quantity')
        category = Category.objects.get(category=request.POST.get('category'))

        new_item = Item(
            user = request.user,
            item = item,
            quantity = quantity,
            category = category, 
        )
        new_item.save()
      

    return redirect('shopping_page')