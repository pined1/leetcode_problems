

from typing import List

class Solution:
    
    def mergeSort(self, array: List[int]) -> List[int]:
        
        if len(array) <= 1:
            return
        
        mid = len(array) // 2
        
        left_sub = array[:mid]
        right_sub = array[mid:]
        
        self.mergeSort(left_sub)
        self.mergeSort(right_sub)
        
        # will change tthe array in place
        self.merge(left_sub=left_sub, right_sub=right_sub, array=array)
    
    
    def merge(self, left_sub: List[int], right_sub: List[int], array: List[int]):
        # left sub pointer
        # right sub pointer
        # array pointer
        i = j = k = 0
        
        while i < len(left_sub) and j < len(right_sub):
            
            if left_sub[i] < right_sub[j]:
                array[k] = left_sub[i]
                i += 1
            else:
                array[k] = right_sub[j]
                j += 1
            k += 1
            
        # can break out if one of them is smaller
        while i < len(left_sub):
            array[k] = left_sub[i]
            i += 1
            k += 1
            
        while j < len(right_sub):
            array[k] = right_sub[j]
            j += 1
            k += 1
            
            

if __name__ == "__main__":
    ob1 = Solution()
    array = [8, 2, 6, 1, 5, 3, 0]
    print(f"UnSorted Array: {array}")
    ob1.mergeSort(array=array)
    print(f"Sorted Array: {array}")
    