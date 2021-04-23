# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        return
        f = ListNode()
        
        while True:
            while l2:
                if l2.val < l1.val:
                    f.val = l2.val
                    l2 = l2.next
                    f = f.next
                break
            
            f.val = l1.val
            l1 = l1.next
            f = f.next
                    
                

sol = Solution()
sol.mergeTwoLists([1,2,4][1,3,4])