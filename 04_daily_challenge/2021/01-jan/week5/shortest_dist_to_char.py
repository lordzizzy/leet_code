# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3631/

# Shortest Distance to a Character
# Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the shortest distance from s[i] to the character c in s.

# Example 1:
# Input: s = "loveleetcode", c = "e"
# Output: [3,2,1,0,1,0,0,1,2,2,1,0]

# Example 2:
# Input: s = "aaab", c = "b"
# Output: [3,2,1,0]

# Constraints:
# 1 <= s.length <= 10^4
# s[i] and c are lowercase English letters.
# c occurs at least once in s.

# sample 20 ms submission
# class Solution:
#     def shortestToChar(self, S: str, C: str) -> List[int]:
#         ans = [None] * len(S)

#         prev = -math.inf
#         for i, char in enumerate(S):
#             if char == C:
#                 prev = i
#                 ans[i] = 0
#             else:
#                 ans[i] = i - prev

#         prev = math.inf
#         for i in reversed(range(len(S))):
#             char = S[i]
#             if char == C:
#                 prev = i
#                 ans[i] = 0
#             else:
#                 ans[i] = min(ans[i], prev - i)

#         return ans

from typing import List
from termcolor import colored


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        res = [n] * n
        last = -1
        curr = 0
        while curr < n:
            if s[curr] != c:
                curr += 1
                continue

            res[curr] = 0

            # update everything on left side
            for l in reversed(range(last+1, curr)):
                dist = curr - l
                if dist < res[l]:
                    res[l] = dist

            # find next c, if any
            next = curr + 1
            while next < n:
                if s[next] == c:
                    break
                next += 1

            # update the dist from curr+1 to (next - curr+1)/2
            end = curr+1+(next-curr+1)//2 if next < n else n
            for r in range(curr+1, end):
                dist = r - curr
                if dist < res[r]:
                    res[r] = dist

            last = curr
            curr = next

        return res


def test_solution(s: str, c: str, expected: List[int]):
    def test_impl(func, s, c, expected):
        r = func(s, c)
        if r == expected:
            print(
                colored(f"PASSED {func.__name__} => {s} shortest char to {c} is {r}", "green"))
        else:
            print(colored(
                f"FAILED {func.__name__} => {s} shortest char to {c} is {r}, expected: {expected}", "red"))
    sln = Solution()
    test_impl(sln.shortestToChar, s, c, expected)


if __name__ == "__main__":
    test_solution(s="loveleetcode", c="e", expected=[
                  3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0])
    test_solution(s="aaab", c="b", expected=[3, 2, 1, 0])
    test_solution(s="baaa", c="b", expected=[0, 1, 2, 3])
    test_solution(s="xuzmnimdwf", c="n", expected=[
                  4, 3, 2, 1, 0, 1, 2, 3, 4, 5])
