# https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/827/

# Product of Array Except Self

# Solution
# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:
# Input:  [1,2,3,4]
# Output: [24,12,8,6]

# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).
#
# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

from typing import List
from termcolor import colored
from collections import defaultdict


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answers = [1] * n

        # build the left product for the first N iteration and store in answers
        for i in range(1, n):
            answers[i] = nums[i-1] * answers[i-1]
        
        # build right product and find the final answer by multiplying each with r-product
        R = 1
        for i in reversed(range(n)):
            answers[i] = answers[i] * R
            R *= nums[i]

        return answers


def test_Solution(nums: List[int], expected: List[int]):
    sln = Solution()
    r = sln.productExceptSelf(nums)
    if r == expected:
        print(
            colored(f"PASSED - {nums} product of array except self = {r}", "green"))
    else:
        print(colored(
            f"FAILED - {nums} product of array except self = {r}, but expected = {expected}", "red"))


if __name__ == "__main__":
    test_Solution(nums=[1, 2, 3, 4], expected=[24, 12, 8, 6])
