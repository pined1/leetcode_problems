# Recursion 

Two - Branch

Fibonacci Numbe:

*GOLDEN RULE*
F(n) = F(n - 1) + F(n - 2)

### Example: 
F(0) = 0, F(1) = 1, F(2) = 1, F(3) = 2, F(4) = 4

F(2) = F(1) + F(0)
F(2) = 1 + 0 ==> 1

F(3) = F(2) + F(1) + F(0)
F(3) = 1 + 1 + 0 ===> 2

F(4) = F(3) + F(2) + F(1) + F(0)
F(4) = 2 + 1 + 1 + 0 ===> 4

Loop Through Step by Step:
Two Branch Solution: Sub Problems:
F(N) = F(n - 1) + F(n - 2)

                        F(5)
             F(4)                    F(3)

       F(3)         F(2)          F(2)        F(1)

  F(2)  F(1)      F(1) F(0)     F(1)  F(0)        ??? No We have reached base case

F(1) F(0)
Base Case is 0 or 1

DRAW OUT THE DESISION TREES: 
Break it Out two Sub Problems? What is the HEIGHTS? THE LEVELS??
5 Levels == N = 5
Layers is N 

* Number of terms 2 * 2 * 2 * 2 * 2 (2 ^ n) Upper Bound 
* Double terms last level total numbers of values
* Upper Bound can be 2 * 2 ^ n = 2 ^ n+1 = 2 ^ n - 1. Because we dont care about constant

