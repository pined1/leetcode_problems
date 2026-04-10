from collections import deque
from typing import List


class Solution:
    
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        
        
        # Bottle neck is the sandwhiches
        
        for sandwhich in sandwiches:
            cnt = 0
            
            while cnt < len(q) and q[0] != sandwhich:
                
                student = q.popleft()
                q.append(student)
                
                cnt += 1
            # Now we have two reasons that it broke out the loop 
            # cnt reached the same len as lenstudents or we found 
            # a sanwhich match
            if q and q[0] == sandwhich:
                q.popleft()
            else:
                break
            
        return len(q)
    
    

if __name__ == "__main__":
    ob1 = Solution()
    students = [1,1,1,0,0,1]
    sandwiches = [1,0,0,0,1,1]
    result = ob1.countStudents(students, sandwiches)
    print(f"Students left hungry {result}")
    