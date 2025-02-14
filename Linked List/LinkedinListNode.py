class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class LinkedList:
    def __init__(self, head=None): 
        self.head = head 

    def print(self):   
        current = self.head  
        if not current:
            print("Deleting last item in List")
            return 
        while current!=None:
            print(" ->" + str(current.val), end="")
            current = current.next
        print(" ")   

    def append(self, d):      
        current = self.head
        if current==None:
            self.head = ListNode(d)   
        else:
            while current.next!=None:
                current = current.next
            current.next = ListNode(d)
        return

    def pop(self):
        current = self.head
        if not current:
            print("Cannot delete: List empty")
        elif not current.next:
            self.head = None
        else:
            prev = None
            while current.next!=None:
                prev = current 
                current = current.next 
            prev.next = None    
        return 

if __name__ == '__main__':
    linkedL = LinkedList()   
    linkedL.print()
    linkedL.append(2)
    linkedL.print()
    linkedL.append(4)
    linkedL.print()
    linkedL.append(6)
    linkedL.print()
    linkedL.pop()
    linkedL.print()
    linkedL.pop()    
    linkedL.print() 
    linkedL.pop()   
    linkedL.print() 
    linkedL.pop()