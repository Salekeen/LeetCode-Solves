# USE MODIFIED BINARY SEARCH
from ast import List


class Solution:
    def findMin(self, nums:List[int])->int:
        # initialize result to an arbitary value
        res = nums[0] # choosing the leftmost

        # init the pointers
        l ,r = 0, len(nums)-1

        # terminating cond.
        while (l<=r):
            # checking whether the subarray is already sorted or not
            if nums[l]<nums[r]:
                res = min(res,nums[l])
                break

            m = (l+r) // 2
            res = min(res,nums[m])

            if (nums[m]>=nums[l]):
                l = m+1
            else:
                r = m-1
        return res
