from linkedListOwn import Node, LinkedList

# initial version, that I cam up with, not to effective as there is lots of converting
def sum_lists(ll1, ll2):
    sum = str(get_number(ll1) + get_number(ll2))
    node = headerNode = Node()
    for num in sum:
        node.data = num
        node.next = Node()
        node = node.next
    return LinkedList(headerNode)

def get_number(ll):
    itr = ll.head
    num = ''
    while itr:
        num = str(itr.data) + num 
        itr = itr.next
    return int(num)

# end of my approach


# book approach



if __name__ == "__main__":
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll1.insert_values([7,1,6])
    ll2.insert_values([5,9,3])
    sum_lists(ll1,ll2).printNodes()
    

    