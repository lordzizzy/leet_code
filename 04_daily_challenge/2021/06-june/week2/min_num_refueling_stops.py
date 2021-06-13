# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3776/

# Minimum Number of Refueling Stops
# A car travels from a starting position to a destination which is target miles
# east of the starting position.

# Along the way, there are gas stations.  Each station[i] represents a gas
# station that is station[i][0] miles east of the starting position, and has
# station[i][1] liters of gas.

# The car starts with an infinite tank of gas, which initially has startFuel
# liters of fuel in it.  It uses 1 liter of gas per 1 mile that it drives.

# When the car reaches a gas station, it may stop and refuel, transferring all
# the gas from the station into the car.

# What is the least number of refueling stops the car must make in order to
# reach its destination?  If it cannot reach the destination, return -1.

# Note that if the car reaches a gas station with 0 fuel left, the car can
# still refuel there.  If the car reaches the destination with 0 fuel left, it
# is still considered to have arrived.

# Example 1:
# Input: target = 1, startFuel = 1, stations = []
# Output: 0
# Explanation: We can reach the target without refueling.

# Example 2:
# Input: target = 100, startFuel = 1, stations = [[10,100]]
# Output: -1
# Explanation: We can't reach the target (or even the first gas station).

# Example 3:
# Input: target = 100, startFuel = 10, stations =
# [[10,60],[20,30],[30,30],[60,40]]
# Output: 2
# Explanation:
# We start with 10 liters of fuel.
# We drive to position 10, expending 10 liters of fuel.  We refuel from 0
# liters to 60 liters of gas.

# Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
# and refuel from 10 liters to 50 liters of gas.  We then drive to and reach
# the target.

# We made 2 refueling stops along the way, so we return 2.

# Note:
# 1 <= target, startFuel, stations[i][1] <= 10^9
# 0 <= stations.length <= 500
# 0 < stations[0][0] < stations[1][0] < ... < stations[stations.length-1][0] <
# target

import heapq
from typing import Callable, List

from termcolor import colored


class Solution:
    #
    # let dp[t] = max distance that we can cover on t stops
    #
    # Time complexity: O(N²), Space complexity: O(N)
    def minRefuelStops_dp_bottom_up(
        self, target: int, startFuel: int, stations: List[List[int]]
    ) -> int:
        N = len(stations)
        dp = [startFuel] + [0] * N

        for i in range(N):
            for t in reversed(range(i + 1)):
                if dp[t] >= stations[i][0]:
                    dp[t + 1] = max(dp[t + 1], dp[t] + stations[i][1])

        for t, dist in enumerate(dp):
            if dist >= target:
                return t

        return -1

    # Time complexity: O(N * logN), Space complexity: O(N)
    def minRefuelStops_greedy_maxheap(
        self, target: int, start_fuel: int, stations: List[List[int]]
    ) -> int:
        if start_fuel >= target:
            return 0

        N = len(stations)
        max_heap: List[int] = []
        res = i = 0

        while start_fuel < target:
            while i < N and stations[i][0] <= start_fuel:
                heapq.heappush(max_heap, -stations[i][1])
                i += 1
            if not max_heap:
                return -1
            start_fuel += -heapq.heappop(max_heap)
            res += 1

        return res


SolutionFunc = Callable[[int, int, List[List[int]]], int]


def test_solution(
    target: int, startFuel: int, stations: List[List[int]], expected: int
) -> None:
    def test_impl(
        func: SolutionFunc,
        target: int,
        startFuel: int,
        stations: List[List[int]],
        expected: int,
    ) -> None:
        r = func(target, startFuel, stations)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Least number of stops for target={target}, startFuel={startFuel}, stations={stations} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Least number of stops for target={target}, startFuel={startFuel}, stations={stations} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.minRefuelStops_dp_bottom_up, target, startFuel, stations, expected)
    test_impl(sln.minRefuelStops_greedy_maxheap, target, startFuel, stations, expected)


if __name__ == "__main__":
    test_solution(target=1, startFuel=1, stations=[], expected=0)
    test_solution(target=100, startFuel=1, stations=[[10, 100]], expected=-1)
    test_solution(
        target=100,
        startFuel=10,
        stations=[[10, 60], [20, 30], [30, 30], [60, 40]],
        expected=2,
    )
