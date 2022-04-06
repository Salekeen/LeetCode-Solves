# HASH SET

from ast import List
class Solution:
    def containsDuplicates(self, nums:List[int])->bool:
        # lets iniatilize our hashset
        hashset = set()

        for n in nums:
            # checking if n exists in the set
            if n in hashset:
                return True
            hashset.add(n)
        return False
