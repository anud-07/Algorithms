"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
"""

from LinkedinListNode import ListNode
from LinkedinListNode import LinkedList

class Solution:
    def swapPairs(self, head):
        
        if head==None or head.next==None:
            return head 
        
        connection, prev, current = None, head, head.next 
        while current!=None:
            front = current.next 
            current.next = prev
            prev.next = front 
            if connection !=None:
                connection.next = current
            else:
                newHead = current
            
            connection = prev
            prev = front 
            if prev==None or prev.next==None:
                return newHead
            else:
                current = prev.next

p1 = LinkedList()
p1.append(1)
p1.append(2)
p1.append(3)
p1.append(4)
l1 = p1.head

solution = Solution()
head = solution.swapPairs(l1)

answer = LinkedList(head)
answer.print()