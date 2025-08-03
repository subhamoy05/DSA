# ---------> Stock Buy and Sell (With one Limit) <------------

# Problem Statement: Given an array prices[] of length N, representing the prices of the stocks on different days, the task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell.

# Note: Stock must be bought before being sold.
# Examples:
# Input: prices[] = {7, 10, 1, 3, 6, 9, 2}
# Output: 8
# Explanation: Buy for price 1 and sell for price 9.

# Input: prices[] = {7, 6, 4, 3, 1}
# Output: 0
# Explanation: Since the array is sorted in decreasing order, 0 profit can be made without making any transaction.

# Input: prices[] = {1, 3, 6, 9, 11}
# Output: 10
# Explanation: Since the array is sorted in increasing order, we can make maximum profit by buying at price[0] and selling at price[n-1]


def max_profit(prices):
    buy = prices[0]
    res = 0
    # Update the minimum value seen so far
    # if wee see smaller
    for i in range(1, len(prices)):
        buy = min(buy, prices[i])

        # Update result if we get more profit
        res = max(res, prices[i] - buy)

    return res


if __name__ == "__main__":
    prices = [7, 10, 1, 3, 6, 9, 2]
    print("Input Prices:", prices)
    print("Output:", max_profit(prices))
