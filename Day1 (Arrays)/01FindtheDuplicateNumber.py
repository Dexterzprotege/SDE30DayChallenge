'''Link: https://leetcode.com/problems/find-the-duplicate-number/
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive. There is only one duplicate number in nums, return this duplicate number.
Follow-ups:
How can we prove that at least one duplicate number must exist in nums? 
Can you solve the problem without modifying the array nums?
Can you solve the problem using only constant, O(1) extra space?
Can you solve the problem with runtime complexity less than O(n2)?
 
Example 1:                                Example 2:
Input: nums = [1,3,4,2,2]                 Input: nums = [3,1,3,4,2]
Output: 2                                 Output: 3

Example 3:                                Example 4:
Input: nums = [1,1]                       Input: nums = [1,1,2]
Output: 1                                 Output: 1

Constraints:
2 <= n <= 3 * 104
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Sort and Compare: O(nlogn), O(1) 88ms, 33.71%
        def solution1(nums):
            nums = sorted(nums)
            for i in range(1, len(nums)):
                if nums[i]==nums[i-1]:
                    return nums[i]
                
        # Set or Map: O(n), O(n), 108ms, 37.12%
        def solution2(nums):
            s = set()
            for i in nums:
                if i in s:
                    return i
                s.add(i)
        
        # Binary Search: O(nlogn), O(1), 84ms, 37.19%
        def solution3(nums):
            lo = 1
            hi = len(nums)-1
            while lo<hi:
                mi = (lo +hi)//2
                count = 0
                for i in nums:
                    if i<=mi:
                        count += 1
                if count>mi:
                    hi = mi
                else:
                    lo = mi+1
            return lo
        
        # Slow and Fast pointers: O(n), O(1), 80ms, 40.29%
        def solution4(nums):
            slow = 0
            fast = 0
            while True:
                slow = nums[slow]
                fast = nums[nums[fast]]
                if slow == fast:
                    break
            finder = 0
            while True:
                slow = nums[slow]
                finder = nums[finder]
                if slow == finder:
                    return slow
                    
        return solution4(nums)
        
        
