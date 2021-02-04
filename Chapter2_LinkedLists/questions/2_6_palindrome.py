from linkedListOwn import Node, LinkedList

def reverseLL(ll):
    itr = ll.head
    previous = Node(itr.data, None)
    if itr.next is None:
        return {'ll': LinkedList(previous), 'll_len': 1}
    ll_len = 1   
    while itr.next:
        temp = Node(itr.next.data, previous)
        previous = temp
        itr = itr.next
        ll_len += 1

    return {'ll': LinkedList(temp), 'll_len': ll_len}

def isPalindrome(ll):
    reversedLL  = reverseLL(ll)
    return


if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.insert_values([7,2])
    print(reverseLL(ll1)["ll_len"])