# using prefix and postfix array

from ast import List


class Solution:
    def productExceptSelf(self, nums: List[int])->List[int]:
        # Initialize result array with all 1s
        res = [1] * len(nums)
        
        # calculating prefixes
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) -1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

