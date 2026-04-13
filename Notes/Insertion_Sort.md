# Sorting

Ascending Order 
1, 2, 3, 4, 5

Descending Order
5, 4, 3, 2, 1

* [ 2, 3, 4, 1, 6]

## Insertion Sort is break the problem

* [2] is sorted by default 
Any array of 1 value is sorted
* [2, 3] check if this is sorted
* Solve using recursion - Do this iterative

Loop
       [2, 3, 4, 1, 6]
* Start at the 3 because the 2 (which is the beginning of the list is already technically sorted)

GOal: Have the mini one sorted 
[2, 3] compare the value only one in the array if its smaller swap, if greater on the right, if its equal put on the right 

[2, 3, 4] - the sub array is already sorted. Stay where it needs to be no need to check if smaller/greater than 2 because it already checked the 3.

[2, 3, 4, 1??] - (1 value and insert it) compare 1 to 4, so j pointer and j + 1 pointer 

If the pointer j + 1 is less than j [ 2, 3, 4, 1] in this case its 1(j + 1) is < 4(j) - now lets do the swap
Put it in a temp variable in space 

- tmp = 1
- arr[j + 1] = arr[j] (4 and 1 have swapped) 
- [2, 3, 4, 4]
- arr[j] = tmp
- [2, 3, 1, 4]
- j -= 1
- we move j because we dont know if its not in correct order so its moved to the left 

* [2, 3, 1, 4]
- j is still in bound
- the value at j is 3 value at j + 1 is 1
- 1 < 3 (do the swap)
- temp = arr[j + 1]
- tmp = 1
- arr[j + 1] = arr[j]
- arr[j] = tmp
- j-= 1


* [2, 1, 3, 4]
- j is at 2 and j + 1 is at 1
- is arr[j + 1] < arr[j] ( yes lets do the swap then)
- tmp = arr[j + 1] 1
- arr[j + 1] = arr[j] [ 2 and 1 flip]
- [2, 2, 3, 4]
- arr[j] = tmp
- [1, 2, 3, 4]
- j -= 1

Outer Loop the first 4 values are sorted, now i pointer moves over and everything on the left is already sorted 
What is really good, everything on the left is sorted.. 

## Stable Algorithm 
- A stable will preserve the original relative (value) will show in the final output is preserved

## Unstable Algorithm 
- Does not keep the preserve of the original relative order


### Notes: 
* Insert Sort alrogithm is prefered since it is Stable Algorithm keeping that original relative the same since its going left to right comparison

* Best Case O(n) time complexity already sorted is linear time complexity
* Worst Case find shift all the way based on the relative of the input max amount of N times 1 was all the way to the right 
* 1 + 2 + 3 + 4 is bounded in O(n) time (1/2) * N^2 time complexity just draw out a grid and shade in the values in the boxes

