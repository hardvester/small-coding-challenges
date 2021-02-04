from linkedListOwn import Node, LinkedList

def reverseLL(ll):
    itr = ll.head
    last_element = itr.head
    last_element.next = None
    while itr.next:
        node = itr.next
    return




if __name__ == "__main__":
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll1.insert_values([7,1,6])
    ll2.insert_values([5,9,3])
    ll1_copy = ll1
    print(ll1.next)
    print(ll1_copy.next)