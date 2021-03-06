

# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3607/

# Count Sorted Vowel Strings

# Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.
# A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

# Example 1:
# Input: n = 1
# Output: 5
# Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].

# Example 2:
# Input: n = 2
# Output: 15
# Explanation: The 15 sorted strings that consist of vowels only are
# ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
# Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.

# Example 3:
# Input: n = 33
# Output: 66045

# Constraints:
# 1 <= n <= 50

from termcolor import colored


class Solution:
    def __init__(self):
        self.cache = {}

    def countVowelStrings(self, n: int):
        r = self.count(n, 5)
        # print(self.cache)
        return r

    def count(self, n: int, c: int):
        if n == 1:
            return c
        # case of any string N that starts with "u" is always 1
        if c == 1:
            return 1
        total = 0
        n -= 1
        # we only need to loop from 2 <= c <= 5 because when c == 1, the result is just 1
        while (c > 1):
            key = n * 10 + c
            if r := self.cache.get(key):
                total += r
            else:
                r = self.cache[key] = self.count(n, c)
                total += r
            c -= 1
        # finally just add 1 for the c == 1 case
        return total + 1


def test_Solution(n: int, expected: int):
    s = Solution()
    count = s.countVowelStrings(n)
    if count == expected:
        print(colored(
            f"PASSED - Vowel string count for size {n} is {count}", "green"))
    else:
        print(colored(
            f"FAILED - Vowel string count for size {n} is {count} but expected {expected}", "red"))


if __name__ == "__main__":
    # default solution using dict for cache
    test_Solution(n=1, expected=5)
    test_Solution(n=2, expected=15)
    test_Solution(n=3, expected=35)
    test_Solution(n=4, expected=70)
    test_Solution(n=5, expected=126)
    test_Solution(n=6, expected=210)
    test_Solution(n=7, expected=330)
    test_Solution(n=33, expected=66045)
