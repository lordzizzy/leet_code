# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3616/

# Check If All 1's Are at Least Length K Places Away
# Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, otherwise return False.

# Example 1:
# Input: nums = [1,0,0,0,1,0,0,1], k = 2
# Output: true
# Explanation: Each of the 1s are at least 2 places away from each other.

# Example 2:
# Input: nums = [1,0,0,1,0,1], k = 2
# Output: false
# Explanation: The second 1 and third 1 are only one apart from each other.

# Example 3:
# Input: nums = [1,1,1,1,1], k = 0
# Output: true

# Example 4:
# Input: nums = [0,1,0,1], k = 1
# Output: true

# Constraints:
# 1 <= nums.length <= 10^5
# 0 <= k <= nums.length
# nums[i] is 0 or 1


# sample solution 
# class Solution:
#     def kLengthApart(self, nums: List[int], k: int) -> bool:
#         count = k
        
#         for num in nums:
#             # if the current integer is 1
#             if num == 1:
#                 # check that number of zeros in-between 1s
#                 # is greater than or equal to k
#                 if count < k:
#                     return False
#                 # reinitialize counter
#                 count = 0
#             # if the current integer is 0
#             else:
#                 # increase the counter
#                 count += 1
                
#         return True

from typing import List
from termcolor import colored


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        i = 0
        one = None
        while (i < n):
            num = nums[i]
            if num == 1:
                if one is None:
                    # print(f"first one at {i}")
                    one = i
                elif (one + k) >= i:
                    # print(f"previous one at index {one} spaced too near to the current one {i}")
                    return False
                else:
                    # print(f"new one at {i}")
                    one = i
            i += 1

        return True


def test_kLengthApart(nums: List[int], k: int, expected: bool):
    sln = Solution()
    r = sln.kLengthApart(nums, k)
    if r == expected:
        print(colored(
            f"PASSED - for {nums}: all 1s are at least {k} lengths away is {r}", "green"))
    else:
        print(colored(
            f"FAILED - for {nums}: all 1s are at least {k} lengths away is {r}, but expected: {expected}", "red"))


if __name__ == "__main__":
    test_kLengthApart(nums=[1, 1, 1, 1, 1], k=0, expected=True)
    test_kLengthApart(nums=[1,0,0,0,1,0,0,1], k=2, expected=True)
    test_kLengthApart(nums=[0,1,0,1], k=1, expected=True)
    test_kLengthApart(nums=[0,0,0], k=2, expected=True)
