""" 
=========== Problem:
On a table are N cards, with a positive integer printed on the front and back of each card (possibly different).

We flip any number of cards, and after we choose one card. 

If the number X on the back of the chosen card is not on the front of any card, then this number X is good.

What is the smallest number that is good?  If no number is good, output 0.

Here, fronts[i] and backs[i] represent the number on the front and back of card i. 

A flip swaps the front and back numbers, so the value on the front is now on the back and vice versa.

Example:

Input: fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
Output: 2
Explanation: If we flip the second card, the fronts are [1,3,4,4,7] and the backs are [1,2,4,1,3].
We choose the second card, which has number 2 on the back, and it isn't on the front of any card, so 2 is good.
 

Note:

1 <= fronts.length == backs.length <= 1000.
1 <= fronts[i] <= 2000.
1 <= backs[i] <= 2000.

=========== Approach
we can achieve the result after arbitrary number of flips
by flipping those numbers that appear on a side more than once to another one, thus,
reaching a side of all "good" cards. From this a minimum could be taken.

This only reachable, though, if a number does not have a card 
representing the number on both sides.

Thus, we need to get rid of such numbers.

=========== Solution:
to store all candidates in a dictionary 
(better than to store in a list as we will request its items regularly)

Also, we have to create an array of 'forbidden' numbers: to store numbers that are on both sides of a card. If iterating we find such number, we append the number into forbidden, and remove from 'candidates' dict.

then find min of the 'candidates'


"""
class Solution:
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        forbidden = []
        candidates = {}
        for i in range(len(fronts)):
            f = fronts[i]
            b = backs[i]
            if f != b:
                if f not in forbidden:
                    candidates[f] = 1
                if b not in forbidden:
                    candidates[b] = 1
            else:
                forbidden.append(f)
                if f in candidates:
                    del candidates[f]
        if candidates:
            return min(candidates.keys())
        return 0
        