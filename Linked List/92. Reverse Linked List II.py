"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Test cases:
head = [1,2,3,4,5], left = 2, right = 4
"""

from LinkedinListNode import ListNode
from LinkedinListNode import LinkedList

class Solution:
    def reverseBetween(self, head, left, right):
        
        if left==right: return head
        
        index, prev, current = 0, None, head
        while True:
            index += 1
            if index==left:
                start = prev 
                end = current 
            elif index<=right and index>left:
                front = current.next 
                current.next = prev 
                prev = current 
                current = front 
                if index==right:
                    if start!=None:
                        start.next = prev 
                        end.next = current
                        return head
                    else:
                        start = prev
                        end.next = current
                        return start
                continue    
            prev = current 
            current = current.next

p3 = LinkedList()
p3.append(1)
p3.append(2)
p3.append(3)
p3.append(4)
p3.append(5)
head = p3.head
left, right = 2, 4

solution = Solution()
head = solution.reverseBetween(head, left, right)

answer = LinkedList(head)
answer.print()