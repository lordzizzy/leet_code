# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3682/

# 3Sum With Multiplicity
# Given an integer array arr, and an integer target, return the number of
# tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

# As the answer can be very large, return it modulo 10⁹ + 7.

# Example 1:
# Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
# Output: 20
# Explanation:
# Enumerating by the values (arr[i], arr[j], arr[k]):
# (1, 2, 5) occurs 8 times;
# (1, 3, 4) occurs 8 times;
# (2, 2, 4) occurs 2 times;
# (2, 3, 3) occurs 2 times.

# Example 2:
# Input: arr = [1,1,2,2,2,2], target = 5
# Output: 12
# Explanation:
# arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
# We choose one 1 from [1,1] in 2 ways,
# and two 2s from [2,2,2,2] in 6 ways.


# Constraints:
# 3 <= arr.length <= 3000
# 0 <= arr[i] <= 100
# 0 <= target <= 300

# https://leetcode.com/problems/3sum-with-multiplicity/discuss/181131/C%2B%2BJavaPython-O(N-%2B-101-*-101)


from itertools import combinations_with_replacement
from typing import Callable, Counter, List
from termcolor import colored


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        return self.threeSumMulti_counting(arr, target)

    def threeSumMulti_counting(self, arr: List[int], target: int) -> int:
        c = Counter[int](n for n in arr if n <= target)
        res = 0
        for i, j in combinations_with_replacement(c, 2):
            k = target - i - j
            if i == j == k:
                res += c[i] * (c[i] - 1) * (c[i] - 2) // 6
            elif i == j != k:
                res += c[i] * (c[i] - 1) // 2 * c[k]
            elif k > i and k > j:
                res += c[i] * c[j] * c[k]
        return res % int(1e9 + 7)


SolutionFunc = Callable[[List[int], int], int]


def test_solution(arr: List[int], target: int, expected: int) -> None:
    def test_impl(
        func: SolutionFunc, arr: List[int], target: int, expected: int
    ) -> None:
        r = func(arr, target)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Num of 3 Sum tuples that adds up to {target} with multiplicity in {arr} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Num of 3 Sum tuples that adds up to {target} with multiplicity in {arr} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.threeSumMulti, arr, target, expected)


if __name__ == "__main__":
    test_solution(arr=[1, 1, 2, 2, 3, 3, 4, 4, 5, 5], target=8, expected=20)
    test_solution(arr=[1, 1, 2, 2, 2, 2, 5], target=5, expected=12)
