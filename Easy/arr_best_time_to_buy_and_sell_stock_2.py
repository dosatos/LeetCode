"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Clarification qustions:
- Any Space/Time Complexity Limitations?
- How big is N?
- How big the elements of N?
- Can the list be empty? if so, what to return?
- Is it possible to have a zero profit scenario?

Test Cases:
[3, 5, 1, 3, 1, 1, 2]
[]
[1 1]
[2 1]
[1 2]

Approach:
- loop over the and compare current item and the next item
 - buy rule: if next item is bigger than current -> I can earn even if 1
 - sell rule: if next item is going down -> I will realise the price
 - if the item is last - sell
 
 Linear Time Complexity O(N), Constant Space Complexity O(1)

"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not list:
            return 0
        
        profit = 0
        ihave = 0

        for idx in range(len(prices)-1):
            this = prices[idx]
            next = prices[idx+1]
            if next > this and not ihave:
                # buy
                profit -= this
                ihave = 1
            elif next < this and ihave:
                # sell
                profit += this
                ihave = 0
        if ihave:
            # sell
            profit += next
            ihave = 0
        return profit
    
    
            
            
            
            
            
            
            
        
            
            