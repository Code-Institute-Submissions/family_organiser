from shopping.models import Partner, PartnerRequest, Item, PurchasedItems, Favorite

def get_partner_requests(request):
    """
    Get the users partner notification requests.
    """
    try:
        partner_requests = PartnerRequest.objects.filter(to_user=request.user)
    except:
        partner_requests = []

    return partner_requests

def all_shopping_items(request):
    """
    Get all shopping items from the current user and their shopping partners.
    """
    # Get all the current users items
    items = Item.objects.filter(user=request.user).order_by('item')

    all_items = [item for item in items]

    # Add all the users items and their shopping partners items into all_items

    for shopping_partner in get_shopping_partners(request):
        if not shopping_partner == request.user:
            partners_shopping_list = Item.objects.filter(user=shopping_partner)
            for item in partners_shopping_list:
                all_items.append(item)

    return all_items

def get_shopping_partners(request):
    """
    Get all the current users shopping partners.
    """
    try:
        shopping_partners = Partner.objects.get(current_user=request.user)
        shopping_partners_list = shopping_partners.partners.all()
    except:
        shopping_partners = []
        shopping_partners_list = []

    return shopping_partners_list

def add_items_quantity_not_duplicates(request):
    """
    Remove the duplicates of items and add the quantity of the same items.
    """
    all_items_no_duplicates = []

    for loop_index, item in enumerate(all_shopping_items(request)):
        item_dict = {
            'item': item.item,
            'quantity': item.quantity,
            'category': item.category.category,
            'id': item.id,
            'user': {
                'username': item.user.first_name
                }
        }

        if loop_index == 0:
            all_items_no_duplicates.append(item_dict)
        else:
            item_is_not_a_copy = True
            for list_item in all_items_no_duplicates:
                if list_item['item'] == item.item:
                    item_is_not_a_copy = False
                    list_item['quantity'] += item.quantity
                    list_item['user']['username'] += ' / ' + item.user.first_name
            if item_is_not_a_copy:
                all_items_no_duplicates.append(item_dict)

    return all_items_no_duplicates

def find_categories_used(request):
    """
    Search all items and find the categories that have been used.
    """
    categories_used = []

    for item_index, item in enumerate(all_shopping_items(request)):
        if item_index == 0:
            categories_used.append(item.category)
        else:
            add_category = True

            for list_item in categories_used:
                if list_item.category == item.category.category:
                    add_category = False
            
            if add_category:
                categories_used.append(item.category)

    return categories_used

def find_categories_used_dict(request):
    """
    Search all items and find the categories that have been used and sort them in an array of dictionaries.
    """
    categories_used = []

    for item_index, item in enumerate(all_shopping_items(request)):
        category_dict = {
            'category': item.category.category,
        }
        if item_index == 0:
            categories_used.append(category_dict)
        else:
            add_category = True

            for list_item in categories_used:
 
                if list_item['category'] == item.category.category:
                    add_category = False
            
            if add_category:
                categories_used.append(category_dict)

    return categories_used

def remove_purchased_item(request, pk):
    remove_item = PurchasedItems.objects.get(pk=pk)
    remove_item_favs = Favorite.objects.get(user=request.user, item=remove_item.item)

    if remove_item_favs.quantity == remove_item.quantity:
        remove_item_favs.delete()
        remove_item.delete()
    else:
        remove_item_favs.quantity -= remove_item.quantity
        remove_item_favs.save()
        remove_item.delete()

    return None


def get_favorites_from_user_and_partners(request):
    favorites = []

    current_users_favorites = Favorite.objects.filter(user=request.user).order_by('-quantity')
    for favorite in current_users_favorites:
        favorites.append(favorite)

    for partner in get_shopping_partners(request):
        partners_favorites = Favorite.objects.filter(user=partner).order_by('-quantity')
        for favorite in partners_favorites:
            favorites.append(favorite)

    return favorites