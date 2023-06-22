#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        result = 0

        def maxProfitRecurse(index, owns_stock = False):

            if index == len(prices):
                return 0

            op0 = maxProfitRecurse(index + 1, owns_stock)

            if not owns_stock:
                op1 = maxProfitRecurse(index + 1, True) - prices[index]
                return max(op0, op1)
            else:
                op2 = prices[index] - fee + maxProfitRecurse(index + 1, False)
                return max(op0, op2)

        result = maxProfitRecurse(0)
        return result


#------------------------------------------------------
# Solution 2 - Solution 1 w/ cache
#------------------------------------------------------

# Runtime:  22.45%
# Memory:    5.62%


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        result = 0

        @cache
        def maxProfitRecurse(index, owns_stock = False):

            if index == len(prices):
                return 0

            op0 = maxProfitRecurse(index + 1, owns_stock)

            if not owns_stock:
                op1 = maxProfitRecurse(index + 1, True) - prices[index]
                return max(op0, op1)
            else:
                op2 = prices[index] - fee + maxProfitRecurse(index + 1, False)
                return max(op0, op2)

        result = maxProfitRecurse(0)
        return result


#------------------------------------------------------
# Solution 3 - iterative
#------------------------------------------------------

# Runtime:  80.31%
# Memory:   84.73%


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        result = 0

        account_no_stock = 0
        account_with_stock = -prices[0]

        for price in prices[1:]:
            start_no_stock = account_no_stock
            start_with_stock = account_with_stock

            no_stock_op1 = start_no_stock
            no_stock_op2 = start_with_stock + price - fee

            end_no_stock = max(no_stock_op1, no_stock_op2)

            with_stock_op1 = start_with_stock
            with_stock_op2 = start_no_stock - price

            end_with_stock = max(with_stock_op1, with_stock_op2)

            account_no_stock = end_no_stock
            account_with_stock = end_with_stock

        result = max(account_no_stock, account_with_stock)
        return result


#------------------------------------------------------
# Solution 4 - Solution 3 w/ custom max
#------------------------------------------------------

# Runtime:  96.21%
# Memory:   44.78%


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        result = 0

        account_no_stock = 0
        account_with_stock = -prices[0]

        for price in prices[1:]:
            start_no_stock = account_no_stock
            start_with_stock = account_with_stock

            no_stock_op1 = start_no_stock
            no_stock_op2 = start_with_stock + price - fee

            end_no_stock = no_stock_op1 if no_stock_op1 > no_stock_op2 else no_stock_op2

            with_stock_op1 = start_with_stock
            with_stock_op2 = start_no_stock - price

            end_with_stock = with_stock_op1 if with_stock_op1 > with_stock_op2 else with_stock_op2

            account_no_stock = end_no_stock
            account_with_stock = end_with_stock

        result = account_no_stock if account_no_stock > account_with_stock else account_with_stock
        return result