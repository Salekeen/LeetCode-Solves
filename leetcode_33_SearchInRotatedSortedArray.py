from ast import List


class Solution:
    def search(self, nums: List[int], target:int) -> int:
        l ,r = 0, len(nums) -1

        while l<=r:
            mid = (l+r) // 2
            # BASE CASE
            if target == nums[mid]:
                return mid
            
            # left sorted portion
            # checking whether mid is in left sorted portion or not
            if nums[l] <= nums[mid]:
                if target>nums[mid] or target < nums[l]:
                    # search right
                    l = mid+1
                else:
                    r = mid -1
            # right sorted portion
            else:
                if target<nums[mid] or target>nums[r]:
                    # search left
                    r = mid -1
                else:
                    l = mid+1
    
        return -1
