'''Main'''

import sys
import datetime
import item_to_purchase
import shopping_cart

def print_menu()->None:
    '''Prints program execution menu'''
    print('MENU')
    print('a - Add item to cart')
    print('r - Remove item from cart')
    print('c - change item quantity')
    print('i - Output items\' descriptions')
    print('o - Output shopping cart')
    print('q - Quit')
    user_input = input('Choose an option: ')
    return user_input


user_name = input('What is your name? ')
today_date = datetime.date.today()

cart = shopping_cart.ShoppingCart(cart_name=user_name, date=today_date.strftime("%B %d, %Y"))
user_selection = print_menu()

while user_selection != 'q':

    if user_selection == 'a':
        new_item_name = input('New item name: ')
        new_item_description = input('New item description: ')
        new_item_price = float(input('New item price: '))
        new_item_quantity = int(input('New item Quantity: '))
        cart.add_item(item_to_purchase.ItemToPurchase(item_name=new_item_name, \
                                                      item_description=new_item_description, \
                                                      item_price=new_item_price, \
                                                      item_quantity=new_item_quantity))
    elif user_selection == 'r':
        user_item = input("Item name to remove: ")
        cart.remove_item(user_item)
    elif user_selection == 'c':
        name = input('Item to update: ')
        qty = int(input('New quantity: '))
        new_item = item_to_purchase.ItemToPurchase(item_name=name, item_quantity=qty)
        cart.modify_item(new_item)
    elif user_selection == 'i':
        cart.print_descriptions()
    elif user_selection == 'o':
        cart.print_total()
    elif user_selection == 'q':
        sys.exit()

    user_selection = print_menu()
