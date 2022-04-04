from ast import List


class Solution:
    def maxProfit(self, prices:List[int])->int:
        # lets initialize the left(buy) and right(sell) pointers
        l,r = 0,1
        maxP = 0

        while r<len(prices):
            # profitable
            if prices[l]<prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP,profit)
            else:
                l = r
            r+=1
        
        return maxP