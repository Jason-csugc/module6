'''Shopping Cart Module'''

import item_to_purchase

class ShoppingCart:
    '''Defines variables and methods for shopping cart'''
    customer_name = ''
    current_date = ''
    cart_items = []


    def __init__(self, cart_name:str=None, date:str='January 1, 2020'):
        self.customer_name = cart_name
        self.current_date = date

    def add_item(self, item_to_add: item_to_purchase.ItemToPurchase) -> None:
        '''Add item to self.cart_items'''
        self.cart_items.append(item_to_add)

    def remove_item(self, item_name: str) -> None:
        '''Remove item from self.cart_items'''
        item_to_remove = None

        for item in self.cart_items:
            if item.item_name == item_name:
                item_to_remove = item
                break

        if item_to_remove is not None:
            self.cart_items.remove(item_to_remove)
        else:
            print('Item not found in cart. Nothing removed.')

    def modify_item(self, item_to_modify:item_to_purchase.ItemToPurchase) -> None:
        '''Modify an items description, price or quantity if they are the default values.'''
        item_found = False

        for item in self.cart_items:
            if item.item_name == item_to_modify.item_name:
                item_found = True
                if item_to_modify.item_price != 0.0:
                    item.item_price = item_to_modify.item_price
                if item_to_modify.item_quantity != 0:
                    item.item_quantity = item_to_modify.item_quantity
                if item_to_modify.item_description == '':
                    item.item_description = item_to_modify.item_description

        if item_found is False:
            print('Item not found in cart. Nothing modified.')

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
            total_cost += item.item_price * item.item_quantity

        return total_cost

    def print_total(self)-> None:
        '''Returns formatted total of items in cart'''
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')

        print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
        print(f'Number of Items: {self.get_num_items_in_cart()}')
        for item in self.cart_items:
            print(item.print_item_cost())
        print(f'Total: ${self.get_cost_of_cart():.2f}')

    def print_descriptions(self)-> None:
        '''Prints cart description'''

        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
            return
        print(f'{self.customer_name}\' Shopping Cart - {self.current_date}')
        print('Item Descriptions')
        for item in self.cart_items:
            print(f'{item.item_name}: {item.item_description}')
