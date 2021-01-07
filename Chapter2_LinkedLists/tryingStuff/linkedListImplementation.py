# source https://medium.com/@kojinoshiba/data-structures-in-python-series-1-linked-lists-d9f848537b4d

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None # the pointer initially points to nothing
    
    def traverse(self):
        node = self # start from the head node
        while node != None:
            print(node.val) # access the node value
            node = node.next # move on to the next node

class car:
    def __init__(self, price):
        self.price = price
    
    def double_price(self, price):
        return price*price

myCar = car(1000)



print(myCar)

