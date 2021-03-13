# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3670/

# Binary Trees With Factors
# Given an array of unique integers, arr, where each integer arr[i] is strictly
# greater than 1.

# We make a binary tree using these integers, and each number may be used for
# any number of times. Each non-leaf node's value should be equal to the
# product of the values of its children.

# Return the number of binary trees we can make. The answer may be too large so
# return the answer modulo 10⁹ + 7.


# Example 1:
# Input: arr = [2,4]
# Output: 3
# Explanation: We can make these trees: [2], [4], [4, 2, 2]

# Example 2:
# Input: arr = [2,4,5,10]
# Output: 7
# Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2,
# 5], [10, 5, 2].


# Constraints:
# 1 <= arr.length <= 1000
# 2 <= arr[i] <= 10⁹


from typing import Callable, DefaultDict, Dict, List
from termcolor import colored

import bisect
import math


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        return self.numFactoredBinaryTrees_dp_basic(arr)

    def numFactoredBinaryTrees_dp_basic(self, arr: List[int]) -> int:
        arr.sort()
        map = DefaultDict[int, int](lambda: 0)

        for num in arr:
            count = 1
            for divisor in map:
                if num % divisor == 0:
                    # use get to avoid potential runtime modification of dict
                    # during iteration
                    count += map[divisor] * map.get(num // divisor, 0)

            map[num] = count

        return sum(map.values()) % int(1e9 + 7)

    # sample 92 ms solution, try to understand this
    def numFactoredBinaryTrees_dp_optimized(self, arr: List[int]) -> int:
        mod = 1_000_000_007
        arr = sorted(set(arr))
        table: Dict[float, int] = {num : 1 for num in arr}
        
        for num in arr[1:] :
            for d in arr[:bisect.bisect(arr ,int(math.sqrt(num)))] :
                if num / d in table :
                    table[num] += table[d] * table[num / d] if d == num / d else table[d] * table[num / d] * 2
            table[num] %= mod
            
        return sum(table.values()) % mod


SolutionFunc = Callable[[List[int]], int]


def test_solution(arr: List[int], expected: int) -> None:
    def test_impl(func: SolutionFunc, arr: List[int], expected: int) -> None:
        r = func(arr)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Num of binary trees that can be built from {arr} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Num of binary trees that can be built from {arr} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.numFactoredBinaryTrees_dp_basic, arr, expected)
    test_impl(sln.numFactoredBinaryTrees_dp_optimized, arr, expected)


if __name__ == "__main__":
    test_solution(arr=[2, 4], expected=3)
    test_solution(arr=[2, 4, 5, 10], expected=7)
    test_solution(arr=[15, 13, 22, 7, 11], expected=5)
