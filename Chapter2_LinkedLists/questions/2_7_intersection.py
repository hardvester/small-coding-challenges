from linkedListOwn import Node, LinkedList

def findIntersectNodes(ll1, ll2):
    ll1_length = ll1.getLength()
    ll2_length = ll2.getLength()
    length_diff = ll1_length - ll2_length

    if length_diff>0:
        starter_ll = ll1
    elif length_diff<0:
        starter_ll = ll2
    else:
        pass
        # run in paraler




if __name__ == "__main__":    
    intersect = Node('I am the intersect xD', Node('z', None))
    ll1 = LinkedList(Node('p', intersect))
    ll2 = LinkedList(Node('d', Node('r', intersect)))

    ll1.printNodes()
    ll2.printNodes()
    print(findIntersectNodes(ll1, ll2))



