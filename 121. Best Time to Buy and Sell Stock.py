"""
Say you have an array for which the ith element is the price of a given stock
on day i.

If you were only permitted to complete at most one transaction (ie, buy one and
sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger
than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""


# maxprofit = max(maxprofit, prices[i] - minprice)
class Solution1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices:
            minprice = max(prices)
            maxprofit = 0
            for i in range(len(prices)):
                if minprice > prices[i]:
                    minprice = prices[i]
                elif maxprofit < prices[i] - minprice:
                    maxprofit = max(maxprofit, prices[i] - minprice)
            return maxprofit
        else:
            return 0


# maxprofit = max(maxprofit, maxprice - prices[i - 1])
class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprice, maxprofit = 0, 0
        for i in range(len(prices), 0, -1):
            maxprofit, maxprice = max(maxprofit, maxprice - prices[i - 1]), \
                max(prices[i - 1], maxprice)
        return maxprofit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print Solution1().maxProfit(prices)
    print Solution2().maxProfit(prices)
