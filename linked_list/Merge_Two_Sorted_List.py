# Merge Two Sorted Linked Lists

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

# The new list should be made up of nodes from list1 and list2.

class ListNode:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        
    # print the array 
    
    def __repr__(self):
        nodes = []
        cur = self
        
        while cur:
            nodes.append(str(cur.val))
            cur = cur.next
        return "->".join(nodes)
    
    
class Solution:
    
    
    def mergeTwoSortedList(self, head: ListNode | None, head2: ListNode | None) -> ListNode | None:
        
        # how to approach this problem
        # can have a list [] and [1, 2, 3] and need to merge them
        # can have a list of [2, 3, 4] and [5, 7, 9]
        # are the lists that are given already sorted? yes they are already sorted :) 
        # we are going to use a dummy node
        dummy = ListNode(0)
        tail = dummy
        
        
        # we have a dummy Node and tail is pointing at this node
        while head and head2:
            if head.val < head2.val:
                tail.next = head
                head = head.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
            
        # what if one of the list is already empty 
        # check if one of the list is none empty
        # we are outside of the while loop so one of these broke the loop
        # / if not its ok
        if head:
            tail.next = head
        if head2:
            tail.next = head2
            
        return dummy.next
    
    
if __name__ == "__main__":
    node1 = ListNode(1)
    node3 = ListNode(3)
    node5 = ListNode(5)
    node7 = ListNode(7)
    node1.next = node3
    node3.next = node5
    node5.next = node7
    
    node6 = ListNode(6)
    node8 = ListNode(8)
    node9 = ListNode(9)
    node10 = ListNode(10)
    node6.next = node8
    node8.next = node9
    node9.next = node10
    
    l1 = Solution()
    print(l1.mergeTwoSortedList(node1, node6))