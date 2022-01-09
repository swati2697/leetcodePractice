# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
 

# Constraints:

# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #O(n) complexity normal looping(LINEAR SEARCH) technique
        nlength = len(nums)
        for i in range(0, nlength):
            if(nums[i] == target):
                return i
        return -1
    
        #O(log n) BINARY SEARCH ALGO approach
        start = 0
        end = len(nums)-1
        while(start <= end):
            center = (start + end) // 2  #floor function- rounds of the value to nearest int
            if(target == nums[center]):
                return center
            if(target > nums[center]):
                start = center+1
            else:
                end = center-1
        return -1
