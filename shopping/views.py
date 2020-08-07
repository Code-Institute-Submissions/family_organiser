from django.shortcuts import render, redirect
import json
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from .models import Category, Item, PurchasedItems, Favorite, Partner, PartnerRequest
from user.models import UserProfile, Friend
from random import randint
import datetime
from .functions.functions import *

# Create your views here.
def shopping_page(request):
    """
    Display the shopping list and the forms to add/remove items.
    """
    # If user isn't logged in return to the home page.
    if request.user.is_anonymous:
        return redirect('home')

    categories = Category.objects.filter(user=request.user)

    if len(categories) == 0:
        return redirect('shopping_intro')

    shopping_partners = get_shopping_partners(request)
    categories_used = find_categories_used(request)
    all_items_no_duplicates = add_items_quantity_not_duplicates(request)
    favorites = Favorite.objects.filter(user=request.user).order_by('-quantity')
    all_items_no_duplicates_sorted = sorted(all_items_no_duplicates, key = lambda x: x['item'], reverse=True)

    context = {
        'items': all_items_no_duplicates_sorted,
        'categories': categories,
        'categories_used': categories_used,
        'favorites': favorites,
    }

    return render(request, 'shopping/shopping_page.html', context)

def quick_item(request, item, category):
    """
    Add or remove an item from the database returning json
    """
    # If user isn't logged in return to the home page.
    if request.user.is_anonymous:
        return redirect('home')

    item_name = item.capitalize()
    quantity = 1
    category_selected = Category.objects.get(category=category, user=request.user)

    # Get users items from the database.
    users_items = Item.objects.filter(user=request.user)

    try:
        item_in_database = Item.objects.get(item=item_name, user=request.user)
        item_in_database.quantity += quantity
        item_in_database.save()
        new_item = False
    except:
        new_item = True
    
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
        favorite = Favorite.objects.get(item=item_name, user=request.user)
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

    shopping_partners_list = get_shopping_partners(request)
    all_items = all_shopping_items(request)
    categories = Category.objects.filter(user=request.user)
    categories_used = find_categories_used_dict(request)
    all_items_no_duplicates = add_items_quantity_not_duplicates(request)
    all_items_no_duplicates = sorted(all_items_no_duplicates, key = lambda x: x['item'], reverse=True)

    return JsonResponse({'items': all_items_no_duplicates, 'categories_used': categories_used, })

def update_category(request, operation, pk):
    """
    Add or remove category from the database.
    """
    # If user isn't logged in return to the home page.
    if request.user.is_anonymous:
        return redirect('home')

    if request.method == 'POST':
        if operation == 'add':
            try: 
                category = Category.objects.get(user=request.user, category=request.POST.get('category'))
            except:
                new_category = Category(
                    user = request.user,
                    category = request.POST.get('category'),
                )
                new_category.save()

        if operation == 'remove':

            category = Category.objects.get(pk=pk)
            category.delete()

    return redirect('shopping_page')

def insight(request, filter):   
    """
    Display instight page with graphs and table of the users favorite items and shopping habbits.
    """ 
    # If user isn't logged in return to the home page.
    if request.user.is_anonymous:
        return redirect('home')

    user_profile = UserProfile.objects.get(user=request.user)

    if user_profile.premium:

        if filter == 'personal':
            # Get all users favorite items and order them by quantity
            favorites = Favorite.objects.filter(user=request.user).order_by('-quantity')
             # get purchsed items form the oldest first
            purchased_items = PurchasedItems.objects.filter(user=request.user).order_by('created_date')
             # Get all purchased items 
            all_purchased_items = PurchasedItems.objects.filter(user=request.user).order_by('-created_date')
        if filter == 'group':
            # Get users shopping partners
            partners = get_shopping_partners(request)

            # Append the current users and their shopping partners favorite into a list
            favorites = get_favorites_from_user_and_partners(request)

            favorites_list = favorites
            favorites = []
            
            for index, favorite in enumerate(favorites_list):
                if index == 0:
                    favorites.append(favorite)
                else:
                    new_item = True
                    for list_item in favorites:
                        if list_item.item == favorite.item:
                            list_item.quantity += favorite.quantity
                            new_item = False
                    if new_item:
                        favorites.append(favorite)

            favorites = sorted(favorites, key = lambda x: x.quantity, reverse=True)

            # Append the current users purchased items and their shopping partners items together in a list
            purchased_items = []
            current_users_purchased_items = PurchasedItems.objects.filter(user=request.user).order_by('-created_date')
            for purchased in current_users_purchased_items:
                purchased_items.append(purchased)

            for partner in partners:
                partners_purchased_items = PurchasedItems.objects.filter(user=partner).order_by('-quantity')
                for item in partners_purchased_items:
                    purchased_items.append(item)

            all_purchased_items = sorted(purchased_items, key = lambda x: x.created_date, reverse=True)

        # top five chart data
        all_favorites = favorites
        chart_data_top_five = []
        chart_labels_top_five = []

        for fav_index, favorite in enumerate(all_favorites):
            if fav_index < 5:
                chart_labels_top_five.append(favorite.item)
                chart_data_top_five.append(favorite.quantity)

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

        # Get the months that items have been added to the list and append them in an array, ready for the monthly report and chart.
        for item in purchased_items:
            item_year = str(item.created_date)[0:4]
            item_month = str(item.created_date)[5:7]
            item_day = str(item.created_date)[8:10]
            format_date = datetime.date(int(item_year), int(item_month), int(item_day))
            monthly_report_dates.append(format_date.strftime('%B'))

        monthly_report_dates = list(dict.fromkeys(monthly_report_dates))
        print(monthly_report_dates)
        monthly_report_data = []
        
        # find the name of each item used and sort in in used_items
        used_items = []
        for item in purchased_items:
            used_items.append(item.item)

        used_items = list(dict.fromkeys(used_items))
        
        # get the users account
        user_profile = UserProfile.objects.get(user=request.user)
        
        # Start the search from when the user created an account
        search_month = str(user_profile.start_date)[0:7]

        # (bug if user doesn't submit a item for a few months it won't work.)
        # (bug jan 2020 and jan 2021 will add up the quantity for jan.) (Maybe fixed can't tell until last bug is fixed)
        # For each items used, search all items each month between the users start date and now.
        # Storing the amount of the same items found each month in item_quantity_in_months
        for item in used_items:
            item_quantity_in_months = []
            for month in range(len(monthly_report_dates)):
                same_items_list = []
                for search_item in purchased_items:
                    if search_item.item == item:
                        search_item_month = str(search_item.created_date)[0:7]
                        if search_item_month == search_month:
                            if not search_item.quantity:
                                same_items_list.append(0)
                            else:
                                same_items_list.append(search_item.quantity)

                item_quantity_in_months.append(sum(same_items_list))
                month_edit = int(search_month[5:7]) + 1
                if month_edit < 10:
                    month_edit = '0' + str(month_edit)

                search_month = search_month[0:5] + month_edit

            # Creating an dictionary for each item with the quantity for each month
            item_dict = {
                    'item': item,
                    'quantity': item_quantity_in_months,
                }
            monthly_report_data.append(item_dict)
            # Reseting the month ready for the next item.
            search_month = str(user_profile.start_date)[0:7]

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

        context = {
            'purchased_items': all_purchased_items,
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
    """
    Search and add shopping partners to the users shopping list.
    """
    # If user isn't logged in return to the home page.
    if request.user.is_anonymous:
        return redirect('home')

    user_profile = UserProfile.objects.get(user=request.user)
    # if the user has a premium account return the shopping partners page or return premium information.
    if user_profile.premium:
        if request.method == 'GET':

            try:

                query = request.GET['q']
                queries = Q(username__startswith=query) | Q(first_name__startswith=query) | Q(last_name__startswith=query) | Q(username__startswith=query.capitalize()) | Q(first_name__startswith=query.capitalize()) | Q(last_name__startswith=query.capitalize())
                users_friends = Friend.objects.get(current_user=request.user)
                all_users = users_friends.users.filter(queries)

                searched_users = []
                for one_user in all_users:
                    user_profile = UserProfile.objects.get(user=one_user)

                    user_dict = {
                        'first_name': one_user.first_name,
                        'last_name': one_user.last_name,
                        'username': one_user.username,
                        'id': one_user.id,
                        'user_profile': {
                            'profile_image': user_profile.profile_image,
                        }
                    }
                    searched_users.append(user_dict)
            except:
                searched_users = []

        friends = Friend.objects.get(current_user=request.user)
        all_friends = friends.users.all()

        # Get users shopping partners or return an empty array
        try:
            shopping_partners = Partner.objects.get(current_user=request.user)
            shopping_partners = shopping_partners.partners.all()
        except:
            shopping_partners = []

        context = {
            'searched_users': searched_users,
            'friends': all_friends,
            'shopping_partners': shopping_partners,
        }

        return render(request, 'shopping/shopping_partner.html', context)

    else: 
        return redirect('premium_info')

def create_request(request, pk):
    """
    Create or remove a request to a user to join their shopping list.
    """
    # If user isn't logged in return to the home page.
    if request.user.is_anonymous:
        return redirect('home')

    requested_user = User.objects.get(pk=pk)
    
    try:
        PartnerRequest.objects.get(from_user=request.user, to_user=requested_user)
    except:
        PartnerRequest.objects.create(from_user=request.user, to_user=requested_user)


    return redirect('add_partner')

def update_partners(request, operation, pk, request_id):
    """
    Add or remove the chosen user from or too their partner list
    """
    user_profile = UserProfile.objects.get(user=request.user)

    if user_profile.premium:

        new_partner = User.objects.get(pk=pk)

        try:
            partner_request = PartnerRequest.objects.get(pk=request_id)
            partner_request.delete()
        except:
            partner_request = None


        if operation == 'add':
            Partner.make_partner(request.user, new_partner)
            Partner.make_partner(new_partner, request.user)
        elif operation == 'remove':
            Partner.remove_partner(request.user, new_partner)
            Partner.remove_partner(new_partner, request.user)
            
            
        return redirect('profile')

    else: 
        return redirect('premium_info')

def edit_item_quantity(request, operation, pk):
    """
    Add, remove, increment or decrement an item from the database, also save a copy to the purchased items and favorites.
    """
    # If user isn't logged in return to the home page.
    if request.user.is_anonymous:
        return redirect('home')

    if operation == 'decrement':
        try:
            edit_item = Item.objects.get(pk=pk)
            edit_item.quantity -= 1
            edit_item.save()
            if edit_item.quantity <= 0:
                edit_item.delete()
        except:
            edit_item = None


    if operation == 'increment':
        try:
            edit_item = Item.objects.get(pk=pk)
            edit_item.quantity += 1
            edit_item.save()
        except:
            edit_item = None

        purchase_item = PurchasedItems(
                user = request.user,
                item = edit_item.item,
                quantity = 1,
                category = edit_item.category, 
            )
        purchase_item.save()

        try:
            favorite = Favorite.objects.get(item=edit_item, user=request.user)
            favorite.quantity += 1
            favorite.save()
        except:
            favorite_item = Favorite(
                user = request.user,
                item = edit_item,
                quantity = 1,
                category = category, 
            )
            favorite_item.save()

    if operation == 'add':

            item_name = request.POST.get('item').capitalize()
            quantity = int(request.POST.get('quantity'))
            category = Category.objects.get(category=request.POST.get('category'), user=request.user)

            # Get users items from the database.
            users_items = Item.objects.filter(user=request.user)
            new_item = True

            # If item in database add the quantity instead of creating a new object.
            for item in users_items:
                if item.item == item_name:
                    item_in_database = Item.objects.get(item=item_name, user=request.user)
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
                favorite = Favorite.objects.get(item=item_name, user=request.user)
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
        remove_item = Item.objects.get(pk=pk)
        remove_item.delete()

     # Get the current users shopping partners or return empty arrays
    try:
        shopping_partners = Partner.objects.get(current_user=request.user)
        shopping_partners_list = shopping_partners.partners.all()
    except:
        shopping_partners = []
        shopping_partners_list = []

    # Get all the current users items
    items = Item.objects.filter(user=request.user).order_by('item')

    all_items = [item for item in items]

    # Add all the users items and their shopping partners items into all_items

    for shopping_partner in shopping_partners_list:
        if not shopping_partner == request.user:
            partners_shopping_list = Item.objects.filter(user=shopping_partner)
            for item in partners_shopping_list:
                all_items.append(item)

    categories = Category.objects.filter(user=request.user)

    
    # Find the categories being used and append to categories_used
    categories_used = []

    for item_index, item in enumerate(all_items):
        category_dict = {
            'category': item.category.category,
        }
        if item_index <= 0:
            categories_used.append(category_dict)
        else:
            add_category = True

            for list_item in categories_used:
 
                if list_item['category'] == item.category.category:
                    add_category = False
            
            if add_category:
                categories_used.append(category_dict)

    # Add the quantity of any duplicate items
    all_items_no_duplicates = add_items_quantity_not_duplicates(request)

    # Sort items alphabetically
    all_items_no_duplicates = sorted(all_items_no_duplicates, key = lambda x: x['item'], reverse=True)

    return JsonResponse({'items': all_items_no_duplicates, 'categories_used': categories_used, })

def edit_purchased_item(request, operation, pk):
    """
    Allows the user to remove items from their purchased items list and also remove the copy
    from their favorites
    """
    # If user isn't logged in return to the home page.
    if request.user.is_anonymous:
        return redirect('home')

    if operation == 'remove':
        remove_purchased_item(request, pk)

    return redirect('insight', 'personal')

def shopping_intro(request):

    return render(request, 'shopping/shopping_intro.html')