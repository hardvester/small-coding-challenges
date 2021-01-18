from linkedListOwn import Node, LinkedList

def remove_dups_with_array(linkedList):
    if linkedList.head == None:
        return
    itr = linkedList.head
    uniqueValues = []
    while itr:
        if (itr.data in uniqueValues):
            linkedList.
        itr = itr.next

if __name__ == "__main__":    
    ll = LinkedList()
    ll.insert_values(['A','B','C','D','B','B','A'])
    ll.printNodes()