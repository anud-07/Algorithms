"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Test Cases:
head = [1,1,2]
"""

from LinkedinListNode import ListNode
from LinkedinListNode import LinkedList

class Solution:
    def deleteDuplicates(self, head):
        
        if not head: return None
        
        dummyNode = ListNode(val = 101)
        prev, prev.next, current = dummyNode, head, head
        
        while current!=None:
            if prev.val==current.val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        return dummyNode.next 

p1 = LinkedList()
p1.append(1)
p1.append(1)
p1.append(2)
p1.append(2)
p1.append(3)
p1.append(4)
head = p1.head

solution = Solution()
head = solution.deleteDuplicates(head)

answer = LinkedList(head)
answer.print()