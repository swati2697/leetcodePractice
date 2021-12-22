# Question: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109




class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #initial intuition
        # i = 0
        # j = 0
        # for i in nums:
        #     for j in range(i+1, len(nums)-1):
        #         if (j >= len(nums)):
        #             return False
        #         elif (nums[i] == nums[j]):
        #             return True
        
        #Sorting logic
        i=0
        nums.sort()
        for i in range(0, len(nums)-1):
             if(nums[i] == nums[i+1]):
                 return True
        return False
    
        #HASHSET Logic
        nums_set = set()
        for i in range(0, len(nums)):
            if(nums[i] in nums_set):
                return True
            nums_set.add(nums[i])
        return False
        
