# strategy - reduce buy price and increase the profit
class solution:
    def maxProfit(self , prices):
        buy_prices = prices[0]
        profit = 0

        for p in prices[1:]:
            if buy_prices > p:
                buy_prices = p

            profit = max(profit,(p-buy_prices))
        return profit , buy_prices

sol = solution()
result = sol.maxProfit([7,1,5,3,6,4])
print(result)