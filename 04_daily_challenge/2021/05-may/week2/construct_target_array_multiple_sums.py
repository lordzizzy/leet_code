# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/599/week-2-may-8th-may-14th/3737/

# Construct Target Array With Multiple Sums
# Given an array of integers target. From a starting array, A consisting of all
# 1's, you may perform the following procedure :


# let x be the sum of all elements currently in your array.
# choose index i, such that 0 <= i < target.size and set the value of A at
# index i to x.

# You may repeat this procedure as many times as needed.
# Return True if it is possible to construct the target array from A otherwise
# return False.

# Example 1:
# Input: target = [9,3,5]
# Output: true
# Explanation: Start with [1, 1, 1]
# [1, 1, 1], sum = 3 choose index 1
# [1, 3, 1], sum = 5 choose index 2
# [1, 3, 5], sum = 9 choose index 0
# [9, 3, 5] Done

# Example 2:
# Input: target = [1,1,1,2]
# Output: false
# Explanation: Impossible to create target array from [1,1,1,1].

# Example 3:
# Input: target = [8,5]
# Output: true

# Constraints:
# N == target.length
# 1 <= target.length <= 5 * 10⁴
# 1 <= target[i] <= 10⁹

from typing import Callable, List
from termcolor import colored

import heapq


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        return self.isPossible_backtrack_maxheap(target)

    # https://leetcode.com/problems/construct-target-array-with-multiple-sums/discuss/1199298/Python-Start-from-the-end-with-heaps-explained
    def isPossible_backtrack_maxheap(self, target: List[int]) -> bool:
        heap: List[int] = []
        for num in target:
            heapq.heappush(heap, -num)
        s = sum(target)
        while True:
            max_num = -heapq.heappop(heap)
            if max_num == 1:
                return True
            if s == max_num:
                return False
            cand = (max_num - 1) % (s - max_num) + 1
            if cand == max_num:
                return False
            s = s - max_num + cand
            heapq.heappush(heap, -cand)


SolutionFunc = Callable[[List[int]], bool]


def test_solution(target: List[int], expected: bool) -> None:
    def test_impl(func: SolutionFunc, target: List[int], expected: bool) -> None:
        r = func(target)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Possible to construct {target} from A is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Possible to construct {target} from A is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.isPossible, target, expected)


if __name__ == "__main__":
    test_solution(target=[9, 3, 5], expected=True)
    test_solution(target=[1, 1, 1, 2], expected=False)
    test_solution(target=[8, 5], expected=True)