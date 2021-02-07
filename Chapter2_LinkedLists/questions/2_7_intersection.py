from linkedListOwn import Node, LinkedList

def findIntersectNodes(ll1, ll2):
    ll1_length = ll1.getLength()
    ll2_length = ll2.getLength()
    length_diff = ll1_length - ll2_length

    if length_diff>0:
        starter_ll = ll1
    elif length_diff<0:
        starter_ll = ll2
    else:
        paralelCompare(ll1, ll2)
        # run in paralel

def equalLengthComparison(ll1, ll2):
    # supposing that the lengths are equal
    itr1 = ll1.head
    itr2 = ll2.head
    while itr1:
        if itr1 == itr2:
            return itr1.data # we don't need the data property, I added it only for testing
        itr1 = itr1.next
        itr2 = itr2.next
    print('the linked lists do not intersect')




if __name__ == "__main__":    
    intersect = Node('I am the intersect xD', Node('z', None))
    ll1 = LinkedList(Node('p', intersect))
    # ll2 = LinkedList(Node('d', Node('r', intersect)))
    ll2 = LinkedList(Node('z', intersect))

    ll1.printNodes()
    ll2.printNodes()

    print(equalLengthComparison(ll1, ll2))



