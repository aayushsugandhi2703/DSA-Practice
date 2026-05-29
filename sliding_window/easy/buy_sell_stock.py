# Given the list of stocks prices, find the maximum profit you can make by buying and selling one share of the stock. 
# You must buy before you sell.

def max_profit_using_two_pointers(prices):
    l, r = 0, 1
    best = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            price = prices[r] - prices[l]
            best = max(best, price)
        else:
            l = r
        r += 1
    return best
#complexity: O(n) time and O(1) space

def main():
    prices = [7,1,5,3,6,4]
    result = max_profit_using_two_pointers(prices)
    print(f"The maximum profit you can make by buying and selling one share of the stock is: {result}")

if __name__ == "__main__":
    main()