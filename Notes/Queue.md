# Queues

Similar to stacks, follow FIFO. Support Enqueue / Dequeue Operations
First in first out


## Enqueue
When we push elements its like stack, Push elements to the end of the 
queue. 


## Dequeue
Dequeue is removing from the beginning. First element we add is the first 
element that we remove. 


## Time Wise
We want to do this add to the end in constant time and remove in constant time
In, an array removing having to shift everything that is O(n) operation


Linked List 


Can have a cur pointer to a 
listNode 1 -- (next pointer) --> ListNode2 --- (next pointer) --> ListNode3

Remove from the head of the list. Cur = cur.next would follow the next node and move the 
cur pointer. Dequeue is very effient. Because of these pointers. 
Dequeue is like removing the pointer at that node, like it doesn't even exist. 