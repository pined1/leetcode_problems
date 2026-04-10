# Ask Scope:
# Implement a list in first out stack using only two queues
# Push/Top/Pop (Needs to be in O(1))
# Single queue 


# Push values in O(1) time

# Q eueue is similar like a line of people: Adding a value 
# [1, 2, 3, 4, 5] adding values from the right 
# remove the values from the popleft 1 goes first
# 2
# 3
# 4
# 5


# Top value is the most recently added look at right most value 
# Empty len(q) non zero non empty 
# Popping values O(n) is the size of the queue
# Q can only remove from the left so get the len of the queue
#     then keep popleft append till len(q) that is the value we wanted to remove
#.     rotation

from collections import deque

class MyStack:
    
    def __init__(self):
        self.q = deque()
    
    
    def push(self, x: int) -> None:
        self.q.append(x)
        
    
    def pop(self) -> int:
        # want to create the loop 
        # go to the last element - 1
        for i in range(len(self.q) - 1):
            val = self.q.popleft()
            self.q.append(val)
            
        return self.q.popleft()
            

    
    
    def top(self) -> int:
        return self.q[-1]
    
    
    def empty(self):
        if len(self.q) == 0:
            return True
        else:
            return False
        
        
# Test code to run in your VS Code
if __name__ == "__main__":
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    print(f"Top element: {stack.top()}")    # Should be 2
    print(f"Popped: {stack.pop()}")         # Should be 2
    print(f"Is empty? {stack.empty()}")      # Should be False