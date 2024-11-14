'''Given an array of integers and a target sum, determine the sum nearest to but not exceeding the target that can be created. 
To create the sum, use any element of your array zero or more times.

For example, if arr = [2,3,4]   and your target sum is 10, you might select [2,2,2,2,2], [2,2,3,3] or  [3,3,3,1]. In this case,
you can arrive at exactly the target.

Function Description

Complete the unboundedKnapsack function in the editor below. It must return an integer that represents the sum nearest 
to without exceeding the target value.

unboundedKnapsack has the following parameter(s):

k: an integer
arr: an array of integers

Input Format

The first line contains an integer t, the number of test cases.

Each of the next t pairs of lines are as follows:
- The first line contains two integers n and k, the length of arr and the target sum.
- The second line contains n space separated integers arr[i].

Constraints

1<=t<=10
1<=n,k,arr[i]<=2000

Output Format

Print the maximum sum for each test case which is as near as possible, but not exceeding, to the target sum on a separate line.

Sample Input

2
3 12
1 6 9
5 9
3 4 4 4 8
Sample Output

12
9
Explanation

In the first test case, one can pick {6, 6}. In the second, we can pick {3,3,3}.'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'unboundedKnapsack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def unboundedKnapsack(k, arr):
    # Write your code here
    dp = [0]*(k+1)
    
    for i in range(1, k+1):
        for num in arr:
            if i >= num:
                dp[i] = max(dp[i], dp[i-num] + num)
                    
    return dp[k]

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    t = int(input().strip())
    results = []
    
    for _ in range(t):
        
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])

        arr = list(map(int, input().rstrip().split()))

        result = unboundedKnapsack(k, arr)
        results.append(result)
    
    fptr.write('\n'.join(map(str, results)) + '\n')
    fptr.close()
