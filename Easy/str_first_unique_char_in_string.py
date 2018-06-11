"""
Percentile: 76%

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

Clarification questions:
Is time or memory complexity important in this case?
How big is len of the string?
Are there only alphabetical symbols?
Shall I consider space as a unique char?

Test cases:
1. ""
2. "e"
3. "ee"
4. "abc"

Approach:
Since I need to take a look at the each of the chars,
I do not see a solution of a complexity faster than O(N) in the worst case.

Also I need to memorize indexes, but not the chars themselves.

Approach 1:
The first solution would be to use a dict as a storage with the letters as keys and list of indexes as the positions.
such as {a: pos (if once, else -1)}. Then sort using sort(list, key=d.get) and return the first non-negative item or -1

The populating of the dict would give me linear complexity, while the sorting O(nlogn) all in all this idea leads to O(nlogn) time complexity and constant for the memory complexity as there are only 26 letters.

Approach 2:
Pre-populate dict with alphabetic symbols (letter: position), iterate over the string if negative, then put position index, else delete from the list.

Again as the dictionary is limited in len, the deleting should not be expensive. Time complexity O(N) in the worst case.

Solution:
1. prepopulate with alphabet letters as keys and -1 otherwise delete or sys.maxsize
2. if == -1
       then store index
   else:
       delete


"""

# import string

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return -1
        letters = dict(zip(strings.ascii_lowercase, [-1 for i in range(26)]))
        for idx, char in enumerate(s):
            if letters[char] == -1:
                letters[char] = idx
            else:
                letters[char] = -2
        positions = sorted(letters.values())
        for pos in positions:
            if pos >= 0:
                return pos
        return -1