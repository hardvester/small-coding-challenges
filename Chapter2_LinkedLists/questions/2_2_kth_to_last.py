from linkedListOwn import Node, LinkedList

def kthToLast(LinkedList, k):
    itr = LinkedList.head
    counter = 0
    while True:
        if counter == k:
            LinkedList.head = itr
            return LinkedList
        counter += 1
        itr = itr.next


if __name__ == "__main__":    
    ll = LinkedList()
    ll.insert_values(['A','B','A','s',2,333,23])
    ll.printNodes()
    kthToLast(ll, 4).printNodes()