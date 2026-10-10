class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or k == 0:
            return 0
        
        # If k is very large, it's equivalent to unlimited transactions
        if k >= len(prices) // 2:
            return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices) - 1))
        
        # Initialize buy and sell arrays for k transactions
        buy = [-prices[0]] * k
        sell = [0] * k
        
        for price in prices:
            for i in range(k):
                if i == 0:
                    buy[i] = max(buy[i], -price)
                else:
                    buy[i] = max(buy[i], sell[i-1] - price)
                sell[i] = max(sell[i], buy[i] + price)
                
        return sell[k-1]