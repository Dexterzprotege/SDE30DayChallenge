'''Problem Link: https://www.interviewbit.com/problems/repeat-and-missing-number-array/
You are given a read only array of n integers from 1 to n.
Each integer appears exactly once except A which appears twice and B which is missing.
Return A and B.
Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Note that in your output A should precede B.
Example:
Input:[3 1 2 5 3] 
Output:[3, 4] 
A = 3, B = 4'''

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    
    # Sort the array, compare index: O(nlogn), O(1) (Not Recommended)
    def solution1(A):
        A = sorted(A)
        arr = []
        for i in range(len(A)):
            if i+1 != A[i]:
                arr.append(i)
                arr.append(i+1)
                break
        return arr
    def repeatedNumber(self, A):
        return solution1(A)
        
