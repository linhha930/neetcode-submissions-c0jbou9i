class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        best = 0

        for p in prices:
            if p < min_price:
                min_price = p
            else:
                profit = p - min_price
                if profit > best:
                    best = profit

        return best