"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
Do not modify the linked list.
"""
from LinkedinListNode import ListNode
from LinkedinListNode import LinkedList

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                new = head
                while new!=slow:
                    slow = slow.next 
                    new = new.next
                return new    
        return None   

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
if not solution1.detectCycle(head):
    print("Cycle free LL")
else:
    print(solution1.detectCycle(head).val)

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
if not solution2.detectCycle(head):
    print("Cycle free LL")
else:
    print(solution2.detectCycle(head).val)

# Test Case-3
p3 = LinkedList()
p3.append(1)
p3.append(2)
p3.append(3)
p3.append(4)
p3.append(5)
head = p3.head

solution3 = Solution()
if not solution3.detectCycle(head):
    print("Cycle free LL")
else:
    print(solution3.detectCycle(head).val)   