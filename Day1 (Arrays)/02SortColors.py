'''Link: https://leetcode.com/problems/sort-colors/
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Follow up:
Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?
 
Example 1:                                Example 2:
Input: nums = [2,0,2,1,1,0]               Input: nums = [2,0,1]
Output: [0,0,1,1,2,2]                     Output: [0,1,2]

Example 3:                                Example 4:
Input: nums = [0]                         Input: nums = [1]
Output: [0]                               Output: [1]

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2.'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # One swap O(n), O(1), 48ms, 19.94%
        def swap(arr, i, j):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        def solution1(nums):
            l, m = 0, 0
            h = len(nums)-1
            while m <= h:
                if nums[m] == 0:
                    swap(nums, l, m)
                    l += 1
                    m += 1
                elif nums[m] == 1:
                    m += 1
                else:
                    swap(nums, m, h)
                    h -= 1
        
        # Two pass O(n), O(1), 36ms, 53.20%
        def solution2(nums):
            one, two, zero = 0, 0, 0
            for i in range(len(nums)):
                if nums[i] == 0: zero+=1
                elif nums[i] == 1: one+=1
                else: two+=1
            for i in range(zero): nums[i] = 0
            for i in range(one): nums[i+zero] = 1
            for i in range(two): nums[i+zero+one] = 2
        solution1(nums)
                
        
