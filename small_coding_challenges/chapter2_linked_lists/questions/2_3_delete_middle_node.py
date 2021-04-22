from linkedListOwn import Node, LinkedList

# this is for the case when we have access to every node
def delete_middle_node(ll, node):
    itr = ll.head

    while itr.next:
        if itr.next.data == node.data:      
            itr.next = itr.next.next   
            return ll     
        itr = itr.next

# the official case when we have access to only the selected node
def delete_middle_node_main(node):
    # we can not delete the last node
    if node.next == None:
        return 'last node can not be deleted'


    node.data = node.next.data
    node.next = node.next.next
    
    
if __name__ == "__main__":    
    ll = LinkedList()
    ll.insert_values(['a','b','c','d', 'e', 'f'])
    ll.printNodes()
    input_node = Node('c', 'd')
    delete_middle_node(ll, input_node).printNodes()

