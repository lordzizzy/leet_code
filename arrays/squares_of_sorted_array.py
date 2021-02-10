# Squares of a Sorted Array

# Solution
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

# Constraints:
# 1 <= nums.length <= 10⁴
# -10⁴ <= nums[i] <= 10⁴
# nums is sorted in non-decreasing order.

# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

from typing import Callable, List
from termcolor import colored


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return self.sortSquares_o_n(nums)

    def sortSquares_trivial(self, nums: List[int]) -> List[int]:
        return sorted(n * n for n in nums)

    # https://leetcode.com/problems/squares-of-a-sorted-array/discuss/222079/Python-O(N)-10-lines-two-solutions-explained-beats-100
    def sortSquares_o_n(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        l, r = 0, len(nums) - 1
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                answer[r - l] = left * left
                l += 1
            else:
                answer[r - l] = right * right
                r -= 1
        return answer


def test_solution(nums: List[int], expected: List[int]):
    SolutionFunc = Callable[[List[int]], List[int]]

    def test_impl(func: SolutionFunc, nums: List[int], expected: List[int]):
        r = func(nums)
        if r == expected:
            print(colored(f"PASSED {func.__name__} => {nums} squares is {r}", "green"))
        else:
            print(
                colored(
                    f"PASSED {func.__name__} => {nums} squares is {r}, but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.sortSquares_trivial, nums, expected)
    test_impl(sln.sortSquares_o_n, nums, expected)


if __name__ == "__main__":
    test_solution(nums=[-4, -1, 0, 3, 10], expected=[0, 1, 9, 16, 100])
    test_solution(nums=[-7, -3, 2, 3, 11], expected=[4, 9, 9, 49, 121])
