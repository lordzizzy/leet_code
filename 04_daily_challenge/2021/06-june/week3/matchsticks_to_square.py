# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/605/week-3-june-15th-june-21st/3780/

# Matchsticks to Square

# Solution
# You are given an integer array matchsticks where matchsticks[i] is the length
# of the ith matchstick. You want to use all the matchsticks to make one
# square. You should not break any stick, but you can link them up, and each
# matchstick must be used exactly one time.

# Return true if you can make this square and false otherwise.


# Example 1:
# Input: matchsticks = [1,1,2,2,2]
# Output: true
# Explanation: You can form a square with length 2, one side of the square came
# two sticks with length 1.

# Example 2:
# Input: matchsticks = [3,3,3,3,4]
# Output: false
# Explanation: You cannot find a way to form a square with all the matchsticks.

# Constraints:
# 1 <= matchsticks.length <= 15
# 0 <= matchsticks[i] <= 10⁹

from functools import lru_cache
from typing import Callable, Dict, List, Tuple

from termcolor import colored


class Solution:
    # Time complexity: O(4^N), Space complexity: O(N)
    def makesquare_dfs_recursive_TLE(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False

        N = len(matchsticks)
        perimeter = sum(matchsticks)
        possible_side = perimeter // 4

        if possible_side * 4 != perimeter:
            return False

        # The reason for this is that if there is no solution, trying a longer
        # matchstick first will get to negative conclusion earlier.
        reversed = sorted(matchsticks, reverse=True)
        sums = [0] * 4

        def dfs(idx: int) -> bool:
            if idx == N:
                return all(s == possible_side for s in sums)
            for i in range(4):
                if sums[i] + reversed[idx] <= possible_side:
                    sums[i] += reversed[idx]
                    if dfs(idx + 1):
                        return True
                    # undo the addition if dfs(idx+1) was false (we did not
                    # reach value of possible side through the addition order)
                    sums[i] -= reversed[idx]
            return False

        return dfs(idx=0)

    # Time complexity: O(N * 2^N), Space complexity: O(N + 2^N)
    def makesquare_dp_topdown(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False

        N = len(matchsticks)
        perimeter = sum(matchsticks)
        possible_side = perimeter // 4

        if possible_side * 4 != perimeter:
            return False

        dp: Dict[Tuple[int, int], bool] = {}

        def dfs(mask: int, sides_done: int) -> bool:
            total = 0
            for i in reversed(range(N - 1)):
                if not (mask & (1 << i)):
                    total += matchsticks[N - 1 - i]

            if total > 0 and total % possible_side == 0:
                sides_done += 1

            if sides_done == 3:
                return True

            if (mask, sides_done) in dp:
                return dp[(mask, sides_done)]

            ans = False
            c = int(total / possible_side)
            rem = possible_side * (c + 1) - total

            for i in reversed(range(N - 1)):
                # if current i-th stick fits and not already used
                if matchsticks[N - 1 - i] <= rem and mask & (1 << i):
                    #
                    if dfs(mask ^ (1 << i), sides_done):
                        ans = True
                        break

            dp[(mask, sides_done)] = ans
            return ans

        return dfs((1 << N) - 1, 0)

    # https://leetcode.com/discuss/general-discussion/1125779/Dynamic-programming-on-subsets-with-examples-explained
    # Time complexity: O(2^N), Space complexity: O(2^N)
    def makesquare_dp_topdown_2(self, matchsticks: List[int]) -> bool:
        N = len(matchsticks)
        side_length, rem = divmod(sum(matchsticks), 4)
        if rem or max(matchsticks) > side_length:
            return False

        @lru_cache(maxsize=None)
        def dfs(mask: int) -> int:
            if mask == 0:
                return 0
            for i in range(N):
                if mask & (1 << i):
                    neib = dfs(mask ^ 1 << i)
                    if neib >= 0 and neib + matchsticks[i] <= side_length:
                        return (neib + matchsticks[i]) % side_length
            return -1

        return dfs((1 << N) - 1) == 0


SolutionFunc = Callable[[List[int]], bool]


def test_solution(matchsticks: List[int], expected: bool) -> None:
    def test_impl(func: SolutionFunc, matchsticks: List[int], expected: bool) -> None:
        r = func(matchsticks)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Make a square with {matchsticks} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Make a square with {matchsticks} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.makesquare_dfs_recursive_TLE, matchsticks, expected)
    test_impl(sln.makesquare_dp_topdown, matchsticks, expected)
    test_impl(sln.makesquare_dp_topdown_2, matchsticks, expected)


if __name__ == "__main__":
    test_solution(matchsticks=[1, 1, 2, 2, 2], expected=True)
    test_solution(matchsticks=[3, 3, 3, 3, 4], expected=False)
