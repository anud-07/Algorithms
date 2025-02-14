"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
"""

from LinkedinListNode import ListNode
from LinkedinListNode import LinkedList

class Solution:
    def deleteDuplicates(self, head):
        
        if head==None or head.next==None:
            return head 
        
        connection, prev, current = None, head, head.next 
        while current!=None:
            if prev.val==current.val:
                dummy = current
                while dummy!=None and dummy.val==current.val:
                    dummy = dummy.next
                if connection!=None:       
                    connection.next = dummy
                else:
                    head = dummy
                prev = dummy
                if dummy!=None:
                    current = dummy.next
                else:
                    return head
            else:
                connection = prev
                prev = current 
                current = current.next
        return head       

p1 = LinkedList()
p1.append(1)
p1.append(2)
p1.append(3)
p1.append(3)
p1.append(4)
p1.append(4)
p1.append(5)
l1 = p1.head

solution = Solution()
head = solution.deleteDuplicates(l1)

answer = LinkedList(head)
answer.print()      

p2 = LinkedList()
p2.append(1)
p2.append(1)
p2.append(1)
p2.append(2)
p2.append(3)
l2 = p2.head

solution = Solution()
head = solution.deleteDuplicates(l2)

answer = LinkedList(head)
answer.print()      