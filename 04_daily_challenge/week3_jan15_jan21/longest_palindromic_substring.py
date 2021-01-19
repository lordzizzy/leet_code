# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3609/

# Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.


# Example 1:
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

# Example 3:
# Input: s = "a"
# Output: "a"

# Example 4:
# Input: s = "ac"
# Output: "a"


# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters (lower-case and/or upper-case)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = end = 0

        for i in range(0, len(s)):
            # for the case of a
            n1 = self.expand(s, i, i)
            # for the case of aa
            n2 = self.expand(s, i, i+1)

            n = max(n1, n2)
            if n > end - start:
                start = i - (n-1)//2
                end = i + n//2

        return s[start:end+1]

    def expand(self, s: str, left: int, right: int) -> int:
        n = len(s)
        L = left
        R = right
        while L >= 0 and R < n and s[L] == s[R]:
            L -= 1
            R += 1
        return R - L - 1


def checkSolution(s: str, expected: str):
    sln = Solution()
    r = sln.longestPalindrome(s)
    assert len(r) == len(expected), \
        f"result={r}'s length: {len(r)} but expected:{len(expected)}"
    print(f'Passed solution for {s}, result={r}')


if __name__ == "__main__":
    checkSolution(s="babad", expected="bab")
    checkSolution(s="cbbd", expected="bb")
    checkSolution(s="a", expected="a")
    checkSolution(s="ac",  expected="a")
