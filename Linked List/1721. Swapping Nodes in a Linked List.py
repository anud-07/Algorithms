"""
You are given the head of a linked list, and an integer k.
Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
"""
from LinkedinListNode import ListNode
from LinkedinListNode import LinkedList

class Solution:
    def swapNodes(self, head, k):
        
        def distanceK(head, k):
            count = 1
            while count!=k:
                count += 1 
                head = head.next
            return head    

        slow, fast = None, distanceK(head, k)
        exchange = fast
        while fast!=None:
            if slow!=None:
                slow = slow.next 
            else:
                slow = head
            fast = fast.next 
        exchange.val, slow.val = slow.val, exchange.val
        return head

p1 = LinkedList()
p1.append(1)
p1.append(2)
p1.append(3)
p1.append(4)
p1.append(5)
l1 = p1.head

solution = Solution()
head = solution.swapNodes(l1, 2)

answer = LinkedList(head)
answer.print()        