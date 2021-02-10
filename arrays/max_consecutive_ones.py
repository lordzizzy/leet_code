# https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/

# Max Consecutive Ones
# Solution
# Given a binary array, find the maximum number of consecutive 1s in this array.

# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
# Note:

# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000

from typing import List
from termcolor import colored


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        longest = 0
        for num in nums:
            if num == 1:
                count += 1
                longest = max(count, longest)
            else:
                count = 0
        return longest


def test_solution(nums: List[int], expected: int):
    sln = Solution()
    r = sln.findMaxConsecutiveOnes(nums)
    if r == expected:
        print(colored(f"PASSED => num of consecutive ones in {nums} is {r}", "green"))
    else:
        print(
            colored(
                f"PASSED => num of consecutive ones in {nums} is {r}, but expected: {expected}",
                "red",
            )
        )


if __name__ == "__main__":
    test_solution(nums=[1, 1, 0, 1, 1, 1], expected=3)
