# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/610/week-3-july-15th-july-21st/3815/

# Valid Triangle Number
# Given an integer array nums, return the number of triplets chosen from the
# array that can make triangles if we take them as side lengths of a triangle.

# Example 1:
# Input: nums = [2,2,3,4]
# Output: 3
# Explanation: Valid combinations are:
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3

# Example 2:
# Input: nums = [4,2,3,4]
# Output: 4

# Constraints:
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000

from typing import Callable, List

from termcolor import colored


class Solution:
    # Time complexity: O(N^3)
    # Space complexity: O(1)
    def triangleNumber_bruteforce(self, nums: List[int]) -> int:
        ans, N = 0, len(nums)
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    if (
                        nums[i] + nums[j] > nums[k]
                        and nums[i] + nums[k] > nums[j]
                        and nums[j] + nums[k] > nums[i]
                    ):
                        ans += 1
        return ans

    # Time complexity: O(N^2)
    # Time complexity: O(1)
    def triangleNumber_sort_and_2ptrs(self, nums: List[int]) -> int:
        nums, ans, N = sorted(nums), 0, len(nums)

        # given sides (a,b,c)
        for c in range(2, N):
            a, b = 0, c - 1
            while a < b:
                if nums[a] + nums[b] > nums[c]:
                    ans += b - a
                    b -= 1
                else:
                    a += 1

        return ans


SolutionFunc = Callable[[List[int]], int]


def test_solution(nums: List[int], expected: int) -> None:
    def test_impl(func: SolutionFunc, nums: List[int], expected: int) -> None:
        r = func(nums)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Number of triplets that can make triangles in {nums} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Number of triplets that can make triangles in {nums} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.triangleNumber_bruteforce, nums, expected)
    test_impl(sln.triangleNumber_sort_and_2ptrs, nums, expected)


if __name__ == "__main__":
    test_solution(nums=[2, 2, 3, 4], expected=3)
    test_solution(nums=[4, 2, 3, 4], expected=4)
