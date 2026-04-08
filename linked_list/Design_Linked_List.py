# Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
# If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

   
   
class ListNode:
    
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:
    
    
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def get(self, index: int) -> int:
        # at this index return the value 
        # of the node at that ith place
        cur = self.left.next
        
        while cur and index > 0:
            cur = cur.next
            index -= 1
            
        # need to check if cur is not out of bounds
        # looped went out before index was reached
        if cur and index == 0 and cur != self.right:
            return cur.val
    
    def addAtHead(self, val: int) -> None:
        # plan to just place a value node
        # at the head of the linked list
        node = ListNode(val)
        next = self.left.next
        prev = self.left
        
        prev.next = node
        next.prev = node
        
        node.next = next
        node.prev = prev
        
    
    def addAtTail(self, val: int) -> None:
        # plan to place a new node with this value
        # at the tail of the linked list
        
        node = ListNode(val)
        next = self.right
        prev = self.right.prev
        
        prev.next = node
        next.prev = node
        
        node.next = next
        node.prev = prev
        
    
    def addAtIndex(self, index: int, val: int) -> None:
        # start cur pointer at the self.left.next
        # keep incrementing till get to that index
        # if we reach self.right that is ok, inserting before
        # if pointer goes passed dummy node (self.right.next)
        
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
            
        if cur and index == 0:
            node = ListNode(val)
            next = cur
            prev = cur.prev
        
            prev.next = node
            next.prev = node
        
            node.next = next
            node.prev = prev
            
    
    
    def deleteAtIndex(self, index: int) -> None:
        # delete the node at this index
        # delete the node our pointer ends at
        # if it ends at the dummy node not a valid node
        # not perform even out of bounds
        
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
            
        if cur and cur != self.right and index == 0:
            next, prev = cur.next, cur.prev
            next.prev = prev
            prev.next = next
            
            
if __name__ == "__main__":
    l1 = MyLinkedList()
    l1.addAtHead(1)
    l1.addAtHead(2)
    l1.addAtHead(3)
    l1.addAtIndex(1, 2) 
    print("get(1):", l1.get(1)) 
    l1.deleteAtIndex(1)                                                                                  
    print("get(1):", l1.get(1)) 
    
        
        
# Summary: In this solution we used a doubly linked list with two dummy nodes to take care of edge cases from both sides
# What helped visualize was the pointers order on piece of paper. Check for the cases if the pointer is out of bounds 
# and for the index problems if correctly at the right one.
