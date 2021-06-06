# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/603/week-1-june-1st-june-7th/3768/

# Maximum Performance of a Team
# You are given two integers n and k and two integer arrays speed and
# efficiency both of length n. There are n engineers numbered from 1 to n.
# speed[i] and efficiency[i] represent the speed and efficiency of the ith
# engineer respectively.

# Choose at most k different engineers out of the n engineers to form a team
# with the maximum performance.

# The performance of a team is the sum of their engineers' speeds multiplied by
# the minimum efficiency among their engineers.

# Return the maximum performance of this team. Since the answer can be a huge
# number, return it modulo 109 + 7.

# Example 1:
# Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
# Output: 60
# Explanation:
# We have the maximum performance of the team by selecting engineer 2 (with
# speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7).
# That is, performance = (10 + 5) * min(4, 7) = 60.

# Example 2:
# Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
# Output: 68
# Explanation:
# This is the same example as the first but k = 3. We can select engineer 1,
# engineer 2 and engineer 5 to get the maximum performance of the team. That
# is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.

# Example 3:
# Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
# Output: 72

# Constraints:
# 1 <= <= k <= n <= 10⁵
# speed.length == n
# efficiency.length == n
# 1 <= speed[i] <= 10⁵
# 1 <= efficiency[i] <= 10⁸

from typing import Callable, List
from termcolor import colored

import heapq


class Solution:
    def maxPerformance(
        self, n: int, speed: List[int], efficiency: List[int], k: int
    ) -> int:
        return self.maxPerformance_greedy_with_priorityq(n, speed, efficiency, k)

    def maxPerformance_greedy_with_priorityq(
        self, n: int, speed: List[int], efficiency: List[int], k: int
    ) -> int:
        candidates = sorted(zip(efficiency, speed), key=lambda t: t[0], reverse=True)
        speed_heap: List[int] = []
        speed_sum, perf = 0, 0
        
        for eff, spd in candidates:
            if len(speed_heap) > k - 1:
                speed_sum -= heapq.heappop(speed_heap)
            heapq.heappush(speed_heap, spd)
            speed_sum += spd
            perf = max(perf, speed_sum * eff)

        return perf % (10 ** 9 + 7)

    def maxPerformance_fastest(
        self, n: int, speed: List[int], efficiency: List[int], k: int
    ) -> int:
        speed_heap: List[int] = []
        speeds, perf = 0, 0
        indexes = list(range(n))
        indexes.sort(key=lambda i: -efficiency[i])

        for i in indexes:
            heapq.heappush(speed_heap, speed[i])
            speeds += speed[i]
            if len(speed_heap) > k:
                lowest_speed = heapq.heappop(speed_heap)
                speeds -= lowest_speed
            perf = max(perf, speeds * efficiency[i])

        return perf % 1000000007


SolutionFunc = Callable[[int, List[int], List[int], int], int]


def test_solution(
    n: int, speed: List[int], efficiency: List[int], k: int, expected: int
) -> None:
    def test_impl(
        func: SolutionFunc,
        n: int,
        speed: List[int],
        efficiency: List[int],
        k: int,
        expected: int,
    ) -> None:
        r = func(n, speed, efficiency, k)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Max performance of chosen {k} of the team with size: {n}, speeds: {speed} efficiencies: {efficiency} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Max performance of chosen {k} of the team with size: {n}, speeds: {speed} efficiencies: {efficiency} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(
        sln.maxPerformance_greedy_with_priorityq, n, speed, efficiency, k, expected
    )
    test_impl(sln.maxPerformance_fastest, n, speed, efficiency, k, expected)


if __name__ == "__main__":
    test_solution(
        n=6, speed=[2, 10, 3, 1, 5, 8], efficiency=[5, 4, 3, 9, 7, 2], k=2, expected=60
    )
    test_solution(
        n=6, speed=[2, 10, 3, 1, 5, 8], efficiency=[5, 4, 3, 9, 7, 2], k=3, expected=68
    )
    test_solution(
        n=6, speed=[2, 10, 3, 1, 5, 8], efficiency=[5, 4, 3, 9, 7, 2], k=4, expected=72
    )
