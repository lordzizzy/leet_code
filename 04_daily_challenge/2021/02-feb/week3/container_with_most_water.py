# Container With Most Water
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of the line i is at (i, ai) and (i, 0). Find two lines, which, together with
# the x-axis forms a container, such that the container contains the most
# water.
#
# Notice that you may not slant the container.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array
# [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
# container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1

# Example 3:
# Input: height = [4,3,2,1,4]
# Output: 16

# Example 4:
# Input: height = [1,2,1]
# Output: 2

# Constraints:
# n == height.length
# 2 <= n <= 3 * 10⁴
# 0 <= height[i] <= 3 * 10⁴

from typing import Callable, List
from termcolor import colored


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        area = 0
        while l < r:
            area = max(area, (r - l) * min(heights[l], heights[r]))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return area


SolutionFunc = Callable[[List[int]], int]


def test_solution(heights: List[int], expected: int) -> None:
    def test_impl(func: SolutionFunc, heights: List[int], expected: int) -> None:
        r = func(heights)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => max area of {heights} is {r}", "green"
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => max area of {heights} is {r}, but expected: {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.maxArea, heights, expected)


if __name__ == "__main__":
    test_solution(heights=[1, 8, 6, 2, 5, 4, 8, 3, 7], expected=49)
    test_solution(heights=[1, 1], expected=1)
    test_solution(heights=[4, 3, 2, 1, 4], expected=16)
    test_solution(heights=[1, 2, 1], expected=2)
