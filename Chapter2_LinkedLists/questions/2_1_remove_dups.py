from linkedListOwn import Node, LinkedList

def remove_dups_with_array(linkedList):
    if linkedList.head == None:
        return
    itr = linkedList.head
    uniqueValues = [itr.data]
    while itr.next:
        if (itr.next.data in uniqueValues):
            # I have done the movement here already
            itr.next = itr.next.next
        else:
            uniqueValues.append(itr.data)
            itr = itr.next
    return linkedList

def remove_dups_without_buffer(linkedList):
    if linkedList.head == None:
        return
    itr = linkedList.head
    while itr:
        followingNode = itr.next
        while followingNode:
            print(followingNode.data)
            if itr.data == followingNode.data:
                itr.next = followingNode.next.next
            else:
                followingNode = followingNode.next
        itr = itr.next
    return linkedList


    

if __name__ == "__main__":    
    ll = LinkedList()
    ll.insert_values(['A','B','A','C','D','B','B','A'])
    ll.printNodes()
    ll = remove_dups_without_buffer(ll)
    ll.printNodes()
    test = {}
    
