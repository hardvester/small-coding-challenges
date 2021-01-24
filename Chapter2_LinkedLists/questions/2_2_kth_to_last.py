from linkedListOwn import Node, LinkedList

# for us k = 1 is the last node, k = 0 is undefined
def kthToLast(LinkedList, k):
    p1 = LinkedList.head
    p2 = LinkedList.head

    for _ in range(0, k-1):
        p1 = p1.next
        if p1 == None:
            print('Out of range')
            return # I should return something that range k is too big

    while p1.next:
        p1 = p1.next
        p2 = p2.next

    # we do it this way so that we can print the result, the book only return p2
    LinkedList.head = p2
    return LinkedList




if __name__ == "__main__":    
    ll = LinkedList()
    ll.insert_values(['A','B','A','s',2,333,23])
    ll.printNodes()
    kthToLast(ll, 8).printNodes()