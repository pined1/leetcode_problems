# Create a class for Insertion Sort
# What are the inputs "unsorted" array of numbers
from typing import List

class Solution:
    
    def insertionSort(self, array: List[int]) -> List[int]:
        if not array:
            return []
        
        if len(array) < 1:
            return array
        
        # will solve this in Iterative using a loop 
        # will take the loop iterate all the way through in the outer loop 
        # having the inner loop while loop check its neighbor
        for i in range(1, len(array)):
            j = i - 1
            
            # make sure that j pointer is still in bound
            while j >= 0 and array[j + 1] < array[j]:
                # meaning [2, 1] that the right value is less than left
                tmp = array[j + 1]
                array[j + 1] = array[j]
                
                # [2, 2]
                array[j] = tmp
                # [ 1, 2]
                j -= 1
        return array
    
    
if __name__ == "__main__":
    obj1 = Solution()
    result = obj1.insertionSort([4, 2, 1, 6, 2])
    print(result)