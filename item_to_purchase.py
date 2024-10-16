'''Item To Purchase Class'''

class ItemToPurchase:
    '''Defines attributes and methods for items to purchase'''
    item_name = ''
    item_price = 0.0
    item_quantity = 0
    item_description = ''

    def __init__(self, item_name = None, item_price=0, item_quantity=0, item_description = None):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        '''Print item cost with following format:
           Bottled Water 10 @ $1 = $10
           '''
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${(self.item_price * self.item_quantity):.2f}')
    