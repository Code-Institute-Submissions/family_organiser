from django.shortcuts import render, redirect
import json
from django.http import JsonResponse
from .models import Category, Item, PurchasedItems, Favorite
from user.models import UserProfile
from random import randint
import datetime

# Create your views here.
def shopping_page(request):

    items = Item.objects.filter(user=request.user).order_by('item')
    categories = Category.objects.filter(user=request.user)
    
    # Find the categories being used and append to categories_used
    categories_used = []
    for item in items:
        if item.category not in categories_used:
            categories_used.append(item.category)

    # Get all users favorite items and order them by quantity
    favorites = Favorite.objects.filter(user=request.user).order_by('-quantity')

    context = {
        'items': items,
        'categories': categories,
        'categories_used': categories_used,
        'favorites': favorites,
    }

    return render(request, 'shopping/shopping_page.html', context)

def update_item(request, operation):

    if request.method == 'POST':
        
        if operation == 'add':

            item_name = request.POST.get('item').capitalize()
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

            purchase_item = PurchasedItems(
                user = request.user,
                item = item_name,
                quantity = quantity,
                category = category, 
            )
            purchase_item.save()
            
            try:
                favorite = Favorite.objects.get(item=item_name)
                favorite.quantity += quantity
                favorite.save()
            except:
                favorite_item = Favorite(
                    user = request.user,
                    item = item_name,
                    quantity = quantity,
                    category = category, 
                )
                favorite_item.save()

            items = Item.objects.filter(user=request.user).order_by('item')

            return redirect('shopping_page')
        
        # Remove items checked by the user
        if operation == 'remove':
            number_of_items = len(request.POST) - 1
            checked_items = 0
            item_pk = 0
            
            # if item has been checked, get the pk and remove the item from the database or add 1 to 
            # item_pk and try again until all checkboxs have been remove.
            while checked_items < number_of_items:
                requested_name = request.POST.get(str(item_pk))
  
                if not requested_name:
                    item_pk += 1
                else:
                    select_item = Item.objects.get(pk=item_pk)
                    select_item.delete()
                    item_pk += 1
                    checked_items += 1

    return redirect('shopping_page')

def quick_item(request, item, category):
    """
    Add or remove an item from the database returning json
    """
    item_name = item.capitalize()
    quantity = 1
    category_selected = Category.objects.get(category=category)

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
            category = category_selected, 
        )
        new_item.save()

    purchase_item = PurchasedItems(
        user = request.user,
        item = item_name,
        quantity = quantity,
        category = category_selected, 
    )
    purchase_item.save()

    try:
        favorite = Favorite.objects.get(item=item_name)
        favorite.quantity += quantity
        favorite.save()
    except:
        favorite_item = Favorite(
            user = request.user,
            item = item_name,
            quantity = quantity,
            category = category, 
        )
        favorite_item.save()

    # Get the items form the database and order them into an array.
    items = Item.objects.filter(user=request.user).order_by('item')
    categories = Category.objects.filter(user=request.user)
    items_list = []

    for item in items:
        item_dict = {
            'user': item.user.username,
            'item': item.item,
            'item_id': item.id,
            'quantity': item.quantity,
            'category': item.category.category,
        }
        items_list.append(item_dict)

    # Find the categories being used and append to categories_used
    categories_used = []
    for item in items:
        if item.category.category not in categories_used:
            categories_used.append(item.category.category)

    return JsonResponse({'items': items_list, 'categories_used': categories_used, })

def update_category(request, operation, pk):
    """
    Add or remove category from the database.
    """
    if request.method == 'POST':
        if operation == 'add':
            new_category = Category(
                user = request.user,
                category = request.POST.get('category'),
            )
            new_category.save()
        if operation == 'remove':

            category = Category.objects.get(pk=pk)
            category.delete()

    return redirect('shopping_page')

def insight(request):   
    """
    Display instight page with graphs and table of the users favorite items and shopping habbits.
    """ 
    user_profile = UserProfile.objects.get(user=request.user)
    if user_profile.premium:
        # Create a list of favorite items from purchased items
        purchased_items = PurchasedItems.objects.filter(user=request.user).order_by('-item')

        # Get all users favorite items and order them by quantity
        favorites = Favorite.objects.filter(user=request.user).order_by('-quantity')

        # top five chart data
        all_favorites = favorites
        chart_data_top_five = []
        chart_labels_top_five = []

        for favorite in range(5):
            try:
                chart_labels_top_five.append(all_favorites[favorite].item)
                chart_data_top_five.append(all_favorites[favorite].quantity)
            except:
                break

        # all favorites for chart data
        all_favorites = favorites
        chart_data = []
        chart_labels = []

        for favorite in all_favorites:
            chart_labels.append(favorite.item)
            chart_data.append(favorite.quantity)

        # dataset for the line chart
        line_chart_dataset = []
        monthly_report_dates = []

        # get purchsed items form the oldest first
        purchased_items = PurchasedItems.objects.filter(user=request.user).order_by('created_date')

        # Get the months that items have been added to the list and append them in an array, ready for the monthly report and chart.
        for item in purchased_items:
            item_year = str(item.created_date)[0:4]
            item_month = str(item.created_date)[5:7]
            item_day = str(item.created_date)[8:10]
            format_date = datetime.date(int(item_year), int(item_month), int(item_day))
            monthly_report_dates.append(format_date.strftime('%B'))

        monthly_report_dates = list(dict.fromkeys(monthly_report_dates))
        monthly_report_data = []

        # Create a list of favorite items from purchased items
        purchased_items = PurchasedItems.objects.filter(user=request.user).order_by('created_date')
        
        # find the name of each item used and sort in in used_items
        used_items = []
        for item in purchased_items:
            used_items.append(item.item)

        used_items = list(dict.fromkeys(used_items))
        
        # get the users account
        user_profile = UserProfile.objects.get(user=request.user)
        
        # Start the search from when the user created an account
        search_month = str(user_profile.start_date)[5:7]

        # (bug if user doesn't submit a item for a few months with won't work.)
        # (bug jan 2020 and jan 2021 will add up the quantity for jan.)
        # For each items used, search all items each month between the users start date and now.
        # Storing the amount of the same items found each month in an item_quantity_in_months
        for item in used_items:
            item_quantity_in_months = []
            for month in range(len(monthly_report_dates)):
                same_items_list = []
                for search_item in purchased_items:
                    if search_item.item == item:
                        search_item_month = str(search_item.created_date)[5:7]
                        if search_item_month == search_month:
                            if not search_item.quantity:
                                same_items_list.append(0)
                            else:
                                same_items_list.append(search_item.quantity)

                item_quantity_in_months.append(sum(same_items_list))
                search_month = int(search_month) + 1
                if search_month < 10:
                    search_month = '0' + str(search_month)

            # Creating an dictionary for each item with the quantity for each month
            item_dict = {
                    'item': item,
                    'quantity': item_quantity_in_months,
                }
            monthly_report_data.append(item_dict)
            # Reseting the month ready for the next item.
            search_month = str(user_profile.start_date)[5:7]

        # formating monthly_report_data in line_chart_dataset ready for chart.js
        line_chart_dataset = []

        for data in monthly_report_data:
            random_colour = []
            for number in range(3):
                random_colour.append(randint(80, 230))

            data_dict = {
                        'label': data['item'],
                        'data': data['quantity'],
                        'backgroundColor': [
                            'rgba(' + str(random_colour)[1:-1] + ',0.2)',
                        ],
                        'borderColor': [
                            'rgba(' + str(random_colour)[1:-1] + ', 1)',
                        ],
                        'borderWidth': 2,
                        'fill': 'false',
                    }
            line_chart_dataset.append(data_dict)

        # Get all purchased items 
        purchased_items = PurchasedItems.objects.filter(user=request.user).order_by('-created_date')

        context = {
            'purchased_items': purchased_items,
            'favorites': favorites,
            'chart_data_top_five': chart_data_top_five,
            'chart_labels_top_five': chart_labels_top_five,
            'chart_data': chart_data,
            'chart_labels': chart_labels,
            'line_chart_dataset': line_chart_dataset,
            'monthly_report_dates': monthly_report_dates,
            'monthly_report_data': monthly_report_data,
        }

        return render(request, 'shopping/insight.html', context)
    
    else:
        return redirect('premium_info')

def add_partner(request):

    user_profile = UserProfile.objects.get(user=request.user)
    if user_profile.premium:

        return render(request, 'shopping/shopping_partner.html')

    else: 
        return redirect('premium_info')