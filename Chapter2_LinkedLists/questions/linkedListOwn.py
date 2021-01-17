class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def addNodeAtBeginning(self, data):
        self.head = Node(data, self.head)

    def printNodes(self):
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '=>'
            itr = itr.next
        print(llstr)
        

ll = LinkedList()
ll.addNodeAtBeginning('ed')
ll.addNodeAtBeginning('ped')
ll.printNodes()




