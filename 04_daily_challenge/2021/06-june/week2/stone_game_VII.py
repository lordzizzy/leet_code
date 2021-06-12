# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3775/

# Stone Game VII
# Alice and Bob take turns playing a game, with Alice starting first.

# There are n stones arranged in a row. On each player's turn, they can remove
# either the leftmost stone or the rightmost stone from the row and receive
# points equal to the sum of the remaining stones' values in the row. The
# winner is the one with the higher score when there are no stones left to
# remove.


# Bob found that he will always lose this game (poor Bob, he always loses), so
# he decided to minimize the score's difference. Alice's goal is to maximize
# the difference in the score.


# Given an array of integers stones where stones[i] represents the value of the
# ith stone from the left, return the difference in Alice and Bob's score if
# they both play optimally.
#

# Example 1:
# Input: stones = [5,3,1,4,2]
# Output: 6
# Explanation:
# - Alice removes 2 and gets 5 + 3 + 1 + 4 = 13 points. Alice = 13, Bob = 0, stones = [5,3,1,4].
# - Bob removes 5 and gets 3 + 1 + 4 = 8 points. Alice = 13, Bob = 8, stones = [3,1,4].
# - Alice removes 3 and gets 1 + 4 = 5 points. Alice = 18, Bob = 8, stones = [1,4].
# - Bob removes 1 and gets 4 points. Alice = 18, Bob = 12, stones = [4].
# - Alice removes 4 and gets 0 points. Alice = 18, Bob = 12, stones = [].
# The score difference is 18 - 12 = 6.

# Example 2:
# Input: stones = [7,90,5,1,100,10,10,2]
# Output: 122


# Constraints:
# n == stones.length
# 2 <= n <= 1000
# 1 <= stones[i] <= 1000

from typing import Callable, List
from termcolor import colored
from functools import lru_cache
from itertools import accumulate


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        return self.stoneGameVII_bottomup_dp_2(stones)

    # More about detail Minimax: https://en.wikipedia.org/wiki/Minimax
    def stoneGameVII_dp_topdown_1(self, stones: List[int]) -> int:
        N = len(stones)
        pre_sum = [0] + list(accumulate(stones))

        # let stones = [A, B, C]
        # let pre_sum = [0, A, A+B, A+B+C]
        # let left = 1, right = 2
        # => (A+B+C) - (A) = B+C
        def get_sum(left: int, right: int) -> int:
            return pre_sum[right + 1] - pre_sum[left]

        @lru_cache(1000 * 2)
        def dp(left: int, right: int, is_alice: bool) -> int:
            if left == right:
                return 0

            if is_alice:
                # alice wants to pick the maximum score
                a = dp(left + 1, right, not is_alice) + get_sum(left + 1, right)
                b = dp(left, right - 1, not is_alice) + get_sum(left, right - 1)
                return max(a, b)
            else:
                # bob wants the minimum of differences
                a = dp(left + 1, right, not is_alice) - get_sum(left + 1, right)
                b = dp(left, right - 1, not is_alice) - get_sum(left, right - 1)
                return min(a, b)

        return dp(0, N - 1, True)

    def stoneGameVII_bottomup_dp_1(self, stones: List[int]) -> int:
        N = len(stones)
        dp = [0] * N

        for i in reversed(range(N)):
            dp_prev = 0
            sum = stones[i]
            for j in range(i, N):
                if i != j:
                    a = sum
                    sum += stones[j]
                    b = sum - stones[i]
                    dp[j] = max(a - dp_prev, b - dp[j])
                    # print(f"i:{i}, j:{j}, dp[{j}] = {dp[j]}")
                dp_prev = dp[j]

        return dp[-1]

    def stoneGameVII_bottomup_dp_2(self, stones: List[int]) -> int:
        N = len(stones)
        dp = [0] * N

        for i in reversed(range(N)):
            v = stones[i]
            run_sum = 0

            for j in range(i + 1, N):
                new_run = run_sum + stones[j]
                dp[j] = max(new_run - dp[j], run_sum + v - dp[j - 1])
                run_sum = new_run

        return dp[N - 1]


SolutionFunc = Callable[[List[int]], int]


def test_solution(stones: List[int], expected: int) -> None:
    def test_impl(func: SolutionFunc, stones: List[int], expected: int) -> None:
        r = func(stones)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Optimal difference in score from stones of {stones} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Optimal difference in score from stones of {stones} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.stoneGameVII_dp_topdown_1, stones, expected)
    test_impl(sln.stoneGameVII_bottomup_dp_1, stones, expected)
    test_impl(sln.stoneGameVII_bottomup_dp_2, stones, expected)


if __name__ == "__main__":
    test_solution(stones=[1, 2, 3], expected=2)
    test_solution(stones=[5, 3, 1, 4, 2], expected=6)
    test_solution(stones=[7, 90, 5, 1, 100, 10, 10, 2], expected=122)
