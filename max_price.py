class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i in range(1, len(prices)):
          if prices[i] > prices[i - 1]:
            buy_price = prices[i] - prices[i - 1]
            max_profit += buy_price
            
        return max_profit
      
# テストコード
if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    solution = Solution()
    max_price = solution.maxProfit(prices)
    print("最初:", prices[1])
    print("最後:", prices[0 - 1])
    print("マックス金額！:", max_price)

        
        