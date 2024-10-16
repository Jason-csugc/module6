'''Shopping Cart Module'''

import sys
import datetime
import item_to_purchase

class ShoppingCart:
    '''Defines variables and methos for shopping cart'''
    customer_name = ''
    current_date = ''
    cart_items = []


    def __init__(self, cart_name:str=None, date:str='January 1, 2020'):
        self.customer_name = cart_name
        self.current_date = date

    def add_item(self, item_to_add: item_to_purchase.ItemToPurchase) -> None:
        '''Add item to self.cart_items'''
        self.cart_items.append(item_to_add)

    def remove_item(self, item_name: str) -> str:
        '''Remove item from self.cart_items'''
        item_to_remove = None

        for item in self.cart_items:
            if item.item_name == item_name:
                item_to_remove = item
                break

        if item_to_remove is not None:
            self.cart_items.remove(item)
            return None

        return 'Item not found in cart. Nothing removed.'

    def modify_item(self, item_to_modify:item_to_purchase.ItemToPurchase) -> str:
        '''Modify an items description, price or quantity if they are the default values.'''

        item_found = False

        for item in self.cart_items:
            if item.item_name == item_to_modify:
                item_found = True
                if item_to_modify.item_price != 0.0:
                    item.item_price = item_to_modify.item_price
                if item_to_modify.item_quantity != 0:
                    item.item_quantity = item_to_modify.item_quantity
                if item_to_modify.item_description == '':
                    item.item_description = item_to_modify.item_description

        if item_found is False:
            return 'Item not found in cart. Nothing modified.'

        return None

    def get_num_items_in_cart(self)-> int:
        '''Returns count of all items in cart'''
        total_sum = 0
        for item in self.cart_items:
            total_sum += item.item_quantity

        return total_sum

    def get_cost_of_cart(self)-> float:
        '''Returns sum of all items cost'''

        total_cost = 0.0

        for item in self.cart_items:
            total_cost += item.item_price + item.item_quantity

        return total_cost

    def print_total(self)-> None:
        '''Returns formated total of items in cart'''
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')

        print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
        print(f'Number of Items: {self.get_num_items_in_cart()}')
        for item in self.cart_items:
            print(item.print_item_cost)
        print(f'Total: ${self.get_cost_of_cart:.2f}')

    def print_descriptions(self)-> None:
        '''Prints cart description'''
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
            return
        print(f'{self.customer_name}\' Shopping Cart - {self.current_date}')
        print('Item Descriptions')
        for item in self.cart_items:
            print(f'{item.item_name}: {item.item_description}')


def print_menu()->None:
    '''Prints program execution menu'''

    print('MENU')
    print('a - Add item to cart')
    print('r - Remove item from cart')
    print('c - change item quantity')
    print('i - Output shopping cart')
    print('q - Quit')
    user_input = input('Choose an option: ')
    return user_input


user_name = input('What is your name? ')
today_date = datetime.date.today()

shopping_cart = ShoppingCart(cart_name=user_name, date=today_date.strftime("%B %d, %Y"))
user_selection = print_menu()

while user_selection != 'q':

    if user_selection == 'a':
        new_item_name = input('New item name: ')
        new_item_description = input('New item description: ')
        new_item_price = float(input('New item price: '))
        new_item_quantity = int(input('New item Quantity: '))
        shopping_cart.add_item(item_to_purchase.ItemToPurchase(item_name=new_item_name, item_description=new_item_description, \
                                                               item_price=new_item_price, item_quantity=new_item_quantity))
    elif user_selection == 'r':
        user_item = input("Item name to remove: ")
        shopping_cart.remove_item(user_item)
    elif user_selection == 'c':
        name = input('Item to update: ')
        qty = int(input('New quantity: '))
        new_item = item_to_purchase.ItemToPurchase(item_name=name, item_quantity=qty)
        shopping_cart.modify_item(new_item)
    elif user_selection == 'i':
        shopping_cart.print_descriptions()
    elif user_selection == 'q':
        sys.exit()


    user_selection = print_menu()
