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

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count



ll = LinkedList()
ll.insert_values(['red', 'bed', 'ced'])
ll.printNodes()



