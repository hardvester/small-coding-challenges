from linkedListOwn import Node, LinkedList

def reverseLL(ll):
    itr = ll.head
    previous = Node(itr.data, None)
    if itr.next is None:
        return LinkedList(previous)
       
    while itr.next:
        temp = Node(itr.next.data, previous)
        previous = temp
        itr = itr.next
    
    return LinkedList(temp)


if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.insert_values([7])
    ll1.printNodes()
    reverseLL(ll1).printNodes()