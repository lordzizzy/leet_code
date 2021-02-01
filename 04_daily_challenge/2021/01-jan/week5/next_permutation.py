
# https://leetcode.com/explore/featured/card/january-leetcoding-challenge-2021/583/week-5-january-29th-january-31st/3623/

# Next Permutation
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
# The replacement must be in place and use only constant extra memory.


# Example 1:
# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:

# Input: nums = [3,2,1]
# Output: [1,2,3]

# Example 3:
# Input: nums = [1,1,5]
# Output: [1,5,1]

# Example 4:
# Input: nums = [1]
# Output: [1]


# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100

from termcolor import colored
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n: int = len(nums)
        if (n == 1):
            return
        # find the first decreasing index
        first = n-2
        while first >= 0 and nums[first+1] <= nums[first]:
            first -= 1

        if first >= 0:
            # starting from the end, find the value that is bigger than nums[first] and swap them
            for i in range(n-1, -1, -1):
                if nums[i] > nums[first]:
                    nums[i], nums[first] = nums[first], nums[i]
                    break
        # reverse numbers from first to last
        first += 1
        last = n-1
        while first < last:
            nums[first], nums[last] = nums[last], nums[first]
            first += 1
            last -= 1


def test_solution(nums: List[int], expected: List[int]):
    original: List[int] = list(nums)
    sln = Solution()
    sln.nextPermutation(nums)
    if nums == expected:
        print(
            colored(f"PASSED => next permutation for {original} is {nums}.", "green"))
    else:
        print(colored(
            f"FAILED => next permutation for {original} is {nums}, but expected: {expected}", "red"))


if __name__ == "__main__":
    test_solution(nums=[1, 2, 3], expected=[1, 3, 2])
    test_solution(nums=[3, 2, 1], expected=[1, 2, 3])
    test_solution(nums=[1, 1, 5], expected=[1, 5, 1])
    test_solution(nums=[1], expected=[1])
    test_solution(nums=[1, 3, 2], expected=[2, 1, 3])
