# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3668/

# Coin Change
# You are given coins of different denominations and a total amount of money
# amount. Write a function to compute the fewest number of coins that you need
# to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:
# Input: coins = [2], amount = 3
# Output: -1

# Example 3:
# Input: coins = [1], amount = 0
# Output: 0

# Example 4:
# Input: coins = [1], amount = 1
# Output: 1

# Example 5:
# Input: coins = [1], amount = 2
# Output: 2

# Constraints:
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 10⁴

from typing import Callable, List, Tuple
from termcolor import colored


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.coinChange_dfs_recursive(coins, amount)

    def coinChange_dfs_recursive(self, coins: List[int], amount: int) -> int:
        MAX = 2 ** 32 - 1
        res = MAX
        coins.sort(reverse=True)

        def dfs(coins_left: int, steps: int, idx: int):
            nonlocal res
            if coins_left < 0:
                return
            if coins_left == 0:
                res = min(res, steps)
                return
            for i in range(idx, len(coins)):
                c = coins[i]
                if c <= coins_left < c * (res - steps): # if this is still possible
                    dfs(coins_left - c, steps + 1, i)

        dfs(amount, 0, 0)

        return res if res != MAX else -1

    # def coinChange_dfs_iterative(self, coins: List[int], amount: int) -> int:

    #     s: List[Tuple[int, int]] = [(amount, 0)]

    #     coins.sort()

    #     while len(s):
    #         left, steps = s.pop()
    #         if left > 0:
    #             for c in coins:
    #                 s.append((left - c, steps + 1))
    #         if left == 0:
    #             return steps

    #     return -1

    # def coinChange_dp(self, coins: List[int], amount: int) -> int:
    #     pass


SolutionFunc = Callable[[List[int], int], int]


def test_solution(coins: List[int], amount: int, expected: int) -> None:
    def test_impl(
        func: SolutionFunc, coins: List[int], amount: int, expected: int
    ) -> None:
        r = func(coins, amount)
        if r == expected:
            print(
                colored(
                    f"PASSED: {func.__name__} => Fewest coins to make up {amount} from {coins} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED: {func.__name__} => Fewest coins to make up {amount} from {coins} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.coinChange_dfs_recursive, coins, amount, expected)


if __name__ == "__main__":
    test_solution(coins=[1, 2, 5], amount=11, expected=3)
    test_solution(coins=[2], amount=3, expected=-1)
    test_solution(coins=[1], amount=0, expected=0)
    test_solution(coins=[1], amount=1, expected=1)
    test_solution(coins=[1], amount=2, expected=2)
    test_solution(coins=[1, 2, 5], amount=100, expected=20)
    test_solution(coins=[2, 5, 10, 1], amount=27, expected=4)
