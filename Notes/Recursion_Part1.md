# One Branch Recursion

n! = n * (n - 1) * (n - 2) * to get to base number 1

5! and decrement it by one at get the result

5! = 5 * 4 * 3 * 2 * 1

5! = 5 * 4!

n! = n * (n - 1)! " THINK IN SUB Problem" Sub problem Recursion 

# Visualization 
5! = sub problem is 4! * 5
        [Decision Tree]
        5!
    - 
   4! Recursive step 

 -
 3! Recursive step 

 -
 2! Recursive step

 1! = 1 This is the Base Case not mapped to a factorial just 1 0! = 1 when to stop 

Keep calling infinetly but need a base case keep going down and down? How would this run

```javascript
  int factorial(int n) {
    if (n <= 1) {
        return 1;
    }

    return n * factorial(n - 1);
  }
```
# One Branch Step 
Steps:
 - 5 is not less than or equal to 1 return 5 * factorial(4)
 - 4 is not less than or equal to 1 return 4 * factorial(3)
 - 3 is not less than or equal to 1 return 3 * factorial(2)
 - 2 is not less than or equal to 1 return 2 * factorial(1)
 - 1 is less than or equal to 1 so return 1
 - 1 is return 2 * 1 = 2
 - 2 is return 3 * 2 = 6
 - 6 is return 4 * 6 = 24
 - 24 is return 5 * 24 = 120

What is the time complexity n! --> n steps O(n) so there are n steps....
This solution has O(n) allocate memory extra memory why??? function compute space in memory, stay right there, keep each step in memory
When we have n steps each function has its own input variable with memory space. 


# Better way to do this

```python
n = 5
res = 1

while n <= 1:
    res = res * n
    n -= 1

return res
```

- Step 1: 5 is not less than or equal to 1: 1 * 5 = 5 
- res = 5
- n = 4

- Step 2: 4 is not less than or equal to 1: 5 * 4 = 20 
- res = 20
- n = 3

- Step 3: 3 is not less than or equal to 1: 20 * 3 = 60
- res = 60
- n = 2

- Step 4: 2 is not less than or equal to 1: 60 * 2 = 120
- res = 120
- n = 1

- Step 5: 1 is less than or equal to 1 break out return 120