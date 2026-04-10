from typing import List




class Solution:
    
    def countNumberStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        # Build out the hashmap 
        # of preferences
        res = len(students)
        cnt = {}
        
        for s in students:
            if s not in cnt:
                cnt[s] = 0
            cnt[s] += 1
            
        # now we have a hashmap {1: 3, 0: 2} res = 5
        
        for sandwich in sandwiches:
            if cnt[sandwich] > 0:
                cnt[sandwich] -= 1
                res -= 1
            else:
                break
            
        return res
    
if __name__ == "__main__":
    ob1 = Solution()
    students = [1,1,1,0,0,1]
    sandwiches = [1,0,0,0,1,1]
    result = ob1.countNumberStudents(students, sandwiches)
    print(f"Students left hungry {result}")
    
    
# Solution is faster: Each student eats a sanwhich then decrement from the hashmap and decrement the result
# which is the length of the students