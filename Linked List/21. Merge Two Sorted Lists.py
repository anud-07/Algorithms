"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Test cases:
l1 = [1,2,4], l2 = [1,3,4]
"""

from LinkedinListNode import ListNode
from LinkedinListNode import LinkedList

class Solution:
    def mergeTwoLists(self, l1, l2):

        dummy_head = ListNode(0)
        current = dummy_head

        while l1 and l2:
            if l1.val < l2.val:
                current.next, l1 = l1, l1.next 
            else:  
                current.next, l2 = l2, l2.next 
            current = current.next    
        if not l1:
            current.next = l2
        else:
            current.next = l1
        return dummy_head.next

p1 = LinkedList()
p1.append(1)
p1.append(2)
p1.append(4)
l1 = p1.head

p2 = LinkedList()
p2.append(1)
p2.append(3)
p2.append(4)
l2 = p2.head

solution = Solution()
head = solution.mergeTwoLists(l1, l2)

answer = LinkedList(head)
answer.print()