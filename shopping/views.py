from django.shortcuts import render, redirect
from .models import Category, Item

# Create your views here.
def shopping_page(request):

    items = Item.objects.filter(user=request.user)
    categories = Category.objects.filter(user=request.user)
    
    # Find the categories being used
    categories_used = []
    for item in items:
        if item.category not in categories_used:
            categories_used.append(item.category)


    context = {
        'items': items,
        'categories': categories,
        'categories_used': categories_used,
    }

    return render(request, 'shopping/shopping_page.html', context)

def add_item(request):

    if request.method == 'POST':

        item_name = request.POST.get('item')
        quantity = int(request.POST.get('quantity'))
        category = Category.objects.get(category=request.POST.get('category'))

        # Get users items from the database.
        users_items = Item.objects.filter(user=request.user)
        new_item = True

        # If item in database add the quantity instead of creating a new object.
        for item in users_items:
            if item.item == item_name:
                item_in_database = Item.objects.get(item=item_name)
                item_in_database.quantity += quantity
                item_in_database.save()
                new_item = False
        
        # Add item if new
        if new_item:
            new_item = Item(
                user = request.user,
                item = item_name,
                quantity = quantity,
                category = category, 
            )
            new_item.save()

    return redirect('shopping_page')

def update_category(request, operation, pk):
    
    if request.method == 'POST':
        print('nearly')
        if operation == 'add':
            new_category = Category(
                user = request.user,
                category = request.POST.get('category'),
            )
            new_category.save()
        print('nearly')
        if operation == 'remove':

            category = Category.objects.get(pk=pk)
            category.delete()
            print('remove item')

    return redirect('shopping_page')