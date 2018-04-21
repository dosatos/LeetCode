"""
Letter Combinations of a Phone Number
Percentile: 98%

Problem:
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.

Clarification Questions:
Shall I be concerned about space or time complexity in this question?
How big is N?
can N be empty?
can a number re-appear again in this string (to be there more than 1 time)?
what happens if 1 is there? treat is as None? and Zero is ' ' (space) <<< 1 and 0 cannot be in the string. if so, return []

Test cases:
23
111
""
1
0
789
7
9

Approach:
make the mapping of a number (in str format) to letters using a dict. Key: a number, Values: a tuple of letters
use idea of levels -> each next number is a level
recursively concatenate to the current level letters the concatenated letters of the following level

At the last level:
    check if current level is the last level (check if something left afterwards)
    return the letters of this level in a list

"""

class Solution:
    def recursive_sol(self, digits, level, dl_map):
        
        this_l = digits[level]
        rest_ll = digits[level+1:]
        
        letters = dl_map[this_l]
        if not rest_ll:
            return [char for char in letters]
        
        storage = []
        # add to all current letters all the other levels
        try:
            for char in letters:
                for passed in self.recursive_sol(digits, level+1, dl_map):
                    storage.append(char + passed)
            return storage
        except:
            return []
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        dl_map = {
            '2': ["a", "b", "c"],
            '3': ["d", "e", "f"],
            '4': ["g", "h", "i"],
            '5': ["j", "k", "l"],
            '6': ["m", "n", "o"],
            '7': ["p", "q", "r", "s"],
            '8': ["t", "u", "v"],
            '9': ["w", "x", "y", "z"],
            '0': [" "]
        }
        if digits == "" or "1" in digits or "0" in digits:
            return []
        return self.recursive_sol(digits, 0, dl_map)
        