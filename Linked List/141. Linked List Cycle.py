"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
"""

from LinkedinListNode import ListNode
from LinkedinListNode import LinkedList

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                return True
        return False

# Test Case-1
p1 = LinkedList()
p1.append(3)
temp = p1.head
p1.append(2)
temp = temp.next
cycle = temp
p1.append(0)
temp = temp.next
p1.append(-4)
temp = temp.next
temp.next = cycle
head = p1.head
solution1 = Solution()
print(solution1.hasCycle(head)) 

# Test Case-2
p2 = LinkedList()
p2.append(1)
temp = p2.head
cycle = temp
p2.append(2)
temp = temp.next

temp.next = cycle
head = p2.head

solution2 = Solution()
print(solution2.hasCycle(head)) 

# Test Case-3
p3 = LinkedList()
p3.append(1)
p3.append(2)
p3.append(3)
p3.append(4)
p3.append(5)
head = p3.head

solution3 = Solution()
print(solution3.hasCycle(head)) 