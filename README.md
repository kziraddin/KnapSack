# Unbounded Knapsack Problem

This project implements a solution to the unbounded knapsack problem, which determines the sum closest to but not exceeding a target sum `k` using any element from an integer array `arr` zero or more times. This approach uses dynamic programming to solve the problem for multiple test cases efficiently.

## Problem Description

Given an integer array `arr` and a target sum `k`, we need to find the maximum sum we can achieve that is:
- **As close as possible to `k`**
- **Does not exceed `k`**

Each element in `arr` can be used any number of times (including zero).

### Function Signature

```python
def unboundedKnapsack(k: int, arr: List[int]) -> int:
    # implementation
Input
t: The number of test cases.
For each test case:
n: The number of elements in arr.
k: The target sum.
arr: A list of n integers representing the available elements.

Output
For each test case, output the maximum achievable sum that is closest to but does not exceed the target k.

## Constraints
1<=t<=10
1<=n,k,arr[i]<=2000

Example
Input
2
3 12
1 6 9
5 9
3 4 4 4 8

Output
12
9

Explanation

In the first test case, using {6, 6} achieves the target sum 12.
In the second test case, using {3, 3, 3} achieves the target sum 9.

Solution Approach
This problem is solved using dynamic programming:

Dynamic Programming Array (dp): Create an array dp of size k + 1 where dp[i] represents the maximum achievable sum closest to and not exceeding i.

Initialization: Set dp[0] to 0, since achieving a sum of 0 is possible without using any elements from arr.

DP Transition:
For each i from 1 to k, check each element num in arr.
If i >= num, update dp[i] to be the maximum of its current value and dp[i - num] + num.
Final Answer: After populating dp, dp[k] will contain the maximum sum that can be achieved without exceeding k.

Code
def unboundedKnapsack(k, arr):
    dp = [0] * (k + 1)
    
    for i in range(1, k + 1):
        for num in arr:
            if i >= num:
                dp[i] = max(dp[i], dp[i - num] + num)
                    
    return dp[k]

Time Complexity: 
𝑂(𝑘×𝑛),where k is the target sum, and n is the size of arr.
Space Complexity: 
𝑂(𝑘) for the dp array.
