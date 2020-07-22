# find max profit with a single buy and sell
# have to buy first
# then sell

bicoin_prices = [1050, 270, 1540, 3800, 2]
# find_max_profit(bitcoin_prices)
# should return 3530
# buy at 270 and selling at 3800
# why is 270 is low?
# subtract largest from smallest

# run through multiple examples
# ask questions to inform handling

def find_max_profit(prices):
    # find the largest
    # if any values after are less than create a new prices
    # then find lowest in the new prices
    # subtract largest from lowest
    sell = 0
    sell_index = 0
    for i in range(len(prices)):
        if prices[i] > sell:
            sell = prices[i]
            # print(sell)
            sell_index = i
    prices = prices[:sell_index]
    buy = sell
    for i in range(len(prices)):
        if prices[i] < buy:
            buy = prices[i]
    return sell - buy
print(find_max_profit(bicoin_prices))