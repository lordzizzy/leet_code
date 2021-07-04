# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/608/week-1-july-1st-july-7th/3800/

# Find K Closest Elements
# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b


# Example 1:

# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
# Example 2:

# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]


# Constraints:

# 1 <= k <= arr.length
# 1 <= arr.length <= 10⁴
# arr is sorted in ascending order.
# -10⁴ <= arr[i], x <= 10⁴


from typing import Callable, List

from termcolor import colored


class Solution:
    # Time complexity: O(log(N-k) + k)
    # Space complexity: O(1)
    def findClosestElements_binarysearch_leftbound(
        self, arr: List[int], k: int, x: int
    ) -> List[int]:
        l, r = 0, len(arr) - k

        # custom binary search
        # if arr[m] is closer to x than arr[m+k]
        # we can shift the right ptr to the left
        while l < r:
            m: int = (l + r) // 2
            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else:
                r = m

        return arr[l : l + k]


SolutionFunc = Callable[[List[int], int, int], List[int]]


def test_solution(arr: List[int], k: int, x: int, expected: List[int]) -> None:
    def test_impl(
        func: SolutionFunc, arr: List[int], k: int, x: int, expected: List[int]
    ) -> None:
        r = func(arr, k, x)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Closest {k} elements in {arr} to {x} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Closest {k} elements in {arr} to {x} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.findClosestElements_binarysearch_leftbound, arr, k, x, expected)


if __name__ == "__main__":
    test_solution(arr=[1, 2, 3, 4, 5], k=4, x=3, expected=[1, 2, 3, 4])
    test_solution(arr=[1, 2, 3, 4, 5], k=4, x=-1, expected=[1, 2, 3, 4])
