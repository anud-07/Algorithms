"""
206. Reverse Linked List.py

Test cases:
head = [1,2,3,4,5]
"""
from LinkedinListNode import ListNode
from LinkedinListNode import LinkedList

class Solution:
    def reverseList(self, head):
        
        if not head: return head

        # atleast one node in the list 
        prev, current = None, head
        while current!=None:
            front = current.next 
            current.next = prev
            prev = current
            current = front 
        return prev     

p1 = LinkedList()
p1.append(1)
p1.append(2)
p1.append(3)
p1.append(4)
p1.append(5)
head = p1.head

solution = Solution()
head = solution.reverseList(head)

answer = LinkedList(head)
answer.print()