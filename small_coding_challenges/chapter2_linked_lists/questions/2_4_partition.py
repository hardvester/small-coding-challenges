from linkedListOwn import Node, LinkedList

def partition(ll, x):
    before_head = before = Node(0)
    after_head = after = Node(0)
        
    itr = ll.head
    while itr:
        if itr.data < x:
            before.next = itr
            before = before.next
        else:
            after.next = itr
            after = after.next
        itr = itr.next

    # chain the 2 linked lists
    before.next = after_head.next
    
    return LinkedList(before_head.next)


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values([1,2,3,2,1,5])
    ll.printNodes()
    partition(ll,2).printNodes()
