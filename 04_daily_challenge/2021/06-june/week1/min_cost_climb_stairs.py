# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/603/week-1-june-1st-june-7th/3770/

# Min Cost Climbing Stairs
# You are given an integer array cost where cost[i] is the cost of ith step on
# a staircase. Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.

# Example 1:
# Input: cost = [10,15,20]
# Output: 15
# Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.

# Example 2:
# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping
# cost[3].

# Constraints:
# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999

from typing import Callable, List
from termcolor import colored
from functools import lru_cache

# REALLy good reference on dynamic programming here
# https://leetcode.com/problems/min-cost-climbing-stairs/discuss/110111/The-ART-of-dynamic-programming


class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        return self.minCostClimbingStairs_dp_topdown_with_memoization(costs)

    def minCostClimbingStairs_dp_topdown_with_memoization(
        self, costs: List[int]
    ) -> int:
        @lru_cache(maxsize=None)
        def step(begin: int) -> int:
            if begin >= len(costs):
                return 0
            return costs[begin] + min(step(begin + 1), step(begin + 2))

        return min(step(0), step(1))

    def minCostClimbingStairs_dp_bottomup(self, costs: List[int]) -> int:
        N = len(costs)
        dp = [0] * (N + 1)

        for i in range(2, N + 1):
            dp[i] = min(dp[i - 1] + costs[i - 1], dp[i - 2] + costs[i - 2])

        return dp[-1]

    # fastest, constant space, only care about n-1 and n-2 steps at step n =>
    # only 2 variables needed.
    def minCostClimbingStairs_dp_o1space(self, costs: List[int]) -> int:
        f1 = f2 = 0
        for i in range(2, len(costs) + 1):
            f1, f2 = min(costs[i - 1] + f1, costs[i - 2] + f2), f1
        return f1

    def minCostClimbingStairs_dp_o1space_reversed(self, costs: List[int]) -> int:
        f1 = f2 = 0
        for x in reversed(costs):
            f1, f2 = x + min(f1, f2), f1
        return min(f1, f2)


SolutionFunc = Callable[[List[int]], int]


def test_solution(cost: List[int], expected: int) -> None:
    def test_impl(func: SolutionFunc, cost: List[int], expected: int) -> None:
        r = func(cost)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Min cost to reach the top floor with costs: {cost} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Min cost to reach the top floor with costs: {cost} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.minCostClimbingStairs_dp_topdown_with_memoization, cost, expected)
    test_impl(sln.minCostClimbingStairs_dp_bottomup, cost, expected)
    test_impl(sln.minCostClimbingStairs_dp_o1space, cost, expected)
    test_impl(sln.minCostClimbingStairs_dp_o1space_reversed, cost, expected)


if __name__ == "__main__":
    test_solution(cost=[10, 15, 20], expected=15)
    test_solution(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1], expected=6)
