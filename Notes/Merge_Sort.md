# Merge Sort Function

THis algorithm is a divide and conquer algorithm

mergeSort(3, 7, 8, 5, 4, 2, 6, 1)
Divide into sub arrays stop when the array has a size of 1..

We will have a new function "merge" that will take in three arguements. The left portion, the right portion and the original array.

Merge will take them into the original array in the correct order. 

Tackle actually left most branch then goes to the right.. 

(3, 7, 8, 5, 4, 2, 6, 1)

(3, 7, 8, 5) -------- (4, 2, 6, 1)

(3, 7) ---------------(8, 5)

(3) ---- (7)

Merge function takes in the left and right then its original array:
Then it does a comparison on the left and right then inserts in the correct place in the orignal array

Whichever element is less will be placed in the next index in the original array. 

MergeSort time complexity is O(nlogn) - Memory is: O(n) since we do have to create new sub arrays



```python
array = [8, 2, 5, 3, 4, 7, 6, 1]

def mergeSort(array: str):


    if len(array) <= 1:
        return
    
    mid = len(array) // 2

    left_half = array[:mid]
    right_half = array[mid:]

    mergeSort(left_half)
    mergeSort(right_half)

    merge(left_half, right_half, array)

    

def merge(left: int, right: int, array: int):
    # need pointers to know where I am in the left sub array
    # where I am in the right sub array
    # and a pointer to reference the original array 

    i = j = k = 0

    # checking still in bounds both might not be the case
    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    # could be one array is shorter than the other
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

```