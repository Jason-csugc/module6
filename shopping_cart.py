'''Shopping Cart Module'''

import item_to_purchase

class ShoppingCart:
    '''Defines variables and methos for shopping cart'''
    customer_name = ''
    current_date = ''
    cart_items = [item_to_purchase.ItemToPurchase]


    def __init__(self, name:str=None, date:str='January 1, 2020'):
        self.customer_name = name
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

    def modify_item(item_to_modify:item_to_purchase.ItemToPurchase):
        return None
    

    def get_num_items_in_cart():
        return None


    def get_cost_of_cart():
        return None
    

    def print_total():
        return None
    
    def print_descriptions():
        return None

    