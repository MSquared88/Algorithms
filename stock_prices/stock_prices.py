    # Write a function `find_max_profit` that receives as input a list of stock prices. Your function should return the maximum profit that can be made from a single buy and sell. You must buy first before selling; no shorting is allowed here.

def find_max_profit(prices):
    #define a max profit and min price
    max_profit_so_far = float("-inf")
    current_min_price_so_far = float("inf")


    #look at each number in the list
    for i in range(0 , len(prices)):
        # print(current_min_price_so_far)
        # print(max_profit_so_far)
        # #compare lowest price to current price
        # if current_min_price_so_far > prices[i]:
        #     current_min_price_so_far = prices[i]
        
        # elif max_profit_so_far = 
        # #compare max profit so far to buying the current stock

        # if max_profit_so_far < prices[i] - current_min_price_so_far:
        #     max_profit_so_far = prices[i] - current_min_price_so_far
        
        # compare buying it to the selling it for the  rest of the numbers in the list 
        for j in range(i+1, len(prices)):
            if prices[j] - prices[i] > max_profit_so_far:
                max_profit_so_far = prices[j] - prices[i]
            # check aand see what max_profit could be made by 
            # buying it and selling 
            

    
    return max_profit_so_far

print(find_max_profit([100, 90, 80, 50, 20, 10]))



# For example, `find_max_profit([1050, 270, 1540, 3800, 2])` should return 3530, which is the maximum profit that can be made from a single buy and then sell of these stock prices. 

# ## Hints

#  For this problem, we essentially want to find the maximum difference between the smallest and largest prices in the list of prices, but we also have to make sure that the max profit is computed by subtracting some price by another price that comes _before_ it; it can't come after it in the list of prices. 

#  So what if we kept track of the `current_min_price_so_far` and the `max_profit_so_far`? 


#!/usr/bin/python
import argparse
if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
