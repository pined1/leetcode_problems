# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

class ListNode:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        
    def __repr__(self):
        nodes = []
        curr = self
        while curr:
            nodes.append(str(curr.val))
            curr = curr.next
        return " -> ".join(nodes)
        


class ReverseList:
    
    
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        
        
        # to reverse the singly linked list I will need to re org the pointers at hand
        # () -> () -> () all pointers would be facing the reverse direction
        # need temp variables to keep track of what is prev and current temp
        
        prev = None
        cur = head
        
        
        while cur:
            
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            
        # broke out since cur is pointing out of bounds so return the prev  
        return prev
            
      
# Summary: Need to have memory of three parts here. prev pointer and the temp pointer and cur. 
# The order in moving along matters the most. Ensure cur is at the head, then set your right which 
# is your temp variable, then you can break the chain.. So, set your right then break the chain. 
# Update your left
# Update your current pointer

# Set your right 
# Break the chain
# Move your prev
# Move your cur
    
    
if __name__ == "__main__":
    # declared my nodes
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    
    # link the nodes together
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    l1 = ReverseList()
    print(l1.reverseList(node1))
        