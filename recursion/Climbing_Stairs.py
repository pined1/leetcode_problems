# You are given an integer n representing the number of steps to reach the top of a staircase. 
# You can climb with either 1 or 2 steps at a time.

# Return the number of distinct ways to climb to the top of the staircase.

# Example 1:
#.    Input: n = 2

#.    Output: 2

#. Explanation:
#.     1 + 1 = 2
#.     2 = 2


#. Example 2:
#.      Input: n = 3

#.      Output: 3

#. Explanation:
#. 1 + 1 + 1 = 3
#. 1 + 2 = 3
#. 2 + 1 = 3
import time


class Solution:
    
    
    def climbingStairs(self, stairs: int) -> int:
        # Given stairs take 1 step or 2 steps at each spot
        # How many ways can you find?? 
        # Use a Desision Tree Take one step or two steps 
        # 0 Step can take 1 step or 2 step to get to the result count the number of ways end count how many 
        # leaf nodes we were able to reach the target
        
        # Every path leads to a base Case return 0 or return 1: Return 0 if its over n step return 1 when we get to base case n
        
        # Sub problems instead of starting at 0, start at 1, start at 2, 
        
        # 2 ^ (n +/- 1)
        return self.dfs(0, stairs)
    
        
        
    def dfs(self, current_step: int, target: int) -> int:
        
        # Base Case reach the bottom target
        if current_step == target:
            return 1
        
        # Might over shoot
        if current_step > target:
            return 0
        
        return self.dfs(current_step + 1, target) + self.dfs(current_step + 2, target)


if __name__ == "__main__":
    ob1 = Solution()
    
    # WARNING: Start with 30-35. Don't go straight to 100!
    n_value = 20
    
    print(f"Calculating for n = {n_value}...")
    
    start_time = time.time() # Start the clock
    result = ob1.climbingStairs(n_value)
    end_time = time.time()   # Stop the clock
    
    elapsed_time = end_time - start_time
    
    print(f"Total number of ways: {result}")
    print(f"Time taken: {elapsed_time:.4f} seconds")