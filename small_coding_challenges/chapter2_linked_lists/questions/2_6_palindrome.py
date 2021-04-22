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
    itr1 = ll.head
    itr2 = reversedLL["ll"].head
    for _ in range(ceil(reversedLL["ll_len"]/2)):
        print(itr1.data, itr2.data)
        if itr1.data != itr2.data:
            print('not a palindrome')
            return
        itr1 = itr1.next
        itr2 = itr2.next
    print('is a palindrome')
    return




if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.insert_values(['g','e','g', 'f'])
    isPalindrome(ll1)
    print(3/2)