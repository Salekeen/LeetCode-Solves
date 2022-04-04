from ast import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val:index

        for i , n in enumerate(nums):
            diff = target - n
            # searching whether the value exits in the map
            if diff in prevMap:
                return [prevMap[diff],i]
            # adding the value to our hash map
            prevMap[n] = i 
        return