"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partit
"""

from LinkedinListNode import ListNode
from LinkedinListNode import LinkedList

class Solution:
    def partition(self, head, x):

        if head==None or head.next==None: return head
        smallDummyHead = ListNode()
        smallHead = smallDummyHead
        geqDummyHead = ListNode()
        geqHead = geqDummyHead
        current = head
        while current!=None:
            if current.val < x:
                smallDummyHead.next = current      
                smallDummyHead = smallDummyHead.next
            else:
                geqDummyHead.next = current
                geqDummyHead = geqDummyHead.next
            current = current.next
        geqDummyHead.next = None    
        smallDummyHead.next = geqHead.next
        return smallHead.next

p1 = LinkedList()
p1.append(1)
p1.append(4)
p1.append(3)
p1.append(2)
p1.append(5)
p1.append(2)
l1 = p1.head

solution = Solution()
head = solution.partition(l1, 3)

answer = LinkedList(head)
answer.print()  


# Another solution O(n) time and space:
"""
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        if not head: return head
        dummy, small, geq = head, [], []
        while dummy!=None:
            if dummy.val < x:
                small.append(dummy)
            else:
                geq.append(dummy)
            dummy = dummy.next    
                
        dummynode = ListNode()
        newhead = dummynode
        for address in small:
            dummynode.next = address
            dummynode = dummynode.next
            
        for address in geq:
            dummynode.next = address
            dummynode = dummynode.next
        dummynode.next = None    
        return newhead.next
"""