# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/583/week-5-january-29th-january-31st/3622/

# Minimize Deviation in Array
# You are given an array nums of n positive integers.

# You can perform two types of operations on any element of the array any number of times:

# If the element is even, divide it by 2.
# For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
# If the element is odd, multiply it by 2.
# For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
# The deviation of the array is the maximum difference between any two elements in the array.

# Return the minimum deviation the array can have after performing some number of operations.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: 1
# Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.

# Example 2:
# Input: nums = [4,1,5,20,3]
# Output: 3
# Explanation: You can transform the array after two operations to [4,2,5,5,3], then the deviation will be 5 - 2 = 3.

# Example 3:
# Input: nums = [2,10,8]
# Output: 3

# Constraints:
# n == nums.length
# 2 <= n <= 10^5
# 1 <= nums[i] <= 10^9

# implmentation notes:
# 1. I missed the intuition that you can only multiply a odd number once by 2 and it will become even, and even numbers will eventually be odd at value 1 if you keep dividing it by 2

# intuitive solution
# https://leetcode.com/problems/minimize-deviation-in-array/discuss/955262/C%2B%2B-intuitions-and-flip


# 732ms fast solution
# class Solution:
#     def minimumDeviation(self, nums: List[int]) -> int:
#         n = len(nums)
#         ans = math.inf

#         maxV = max(nums)

#         heapify(nums)
#         while True:
#             ans = min(ans, maxV - nums[0])

#             if nums[0] % 2 == 1:
#                 x = heappop(nums)
#                 heappush(nums, x * 2)
#                 maxV = max(maxV, x * 2)
#             else:
#                 break

#         nums = [-x for x in nums]
#         maxV = max(nums)

#         heapify(nums)
#         while True:
#             ans = min(ans, maxV - nums[0])
#             if nums[0] % 2 == 0:
#                 x = heappop(nums)
#                 heappush(nums, x // 2)
#                 maxV = max(maxV, x // 2)
#             else:
#                 break

#         return ans

from typing import List
from termcolor import colored
from heapq import heapify, heappush, heappushpop


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        n: int = len(nums)
        pq: List[int] = []
        heapify(pq)
        min_n: int = int(1e9+7)
        dev: int = int(1e9+7)

        # multiply all the odd numbers by 2 to make them all even
        for i in range(0, n):
            n = nums[i] * 2 if nums[i] % 2 else nums[i]
            heappush(pq, -n)
            min_n = min(min_n, n)

        # while the top of the heapq is an even number
        while pq[0] % 2 == 0:
            dev = min(dev, -pq[0] - min_n)
            min_n = min(min_n, -pq[0]//2)
            heappushpop(pq, pq[0]//2)

        return min(dev, -pq[0] - min_n)


def test_solution(nums: List[int], expected: int):
    sln = Solution()
    r = sln.minimumDeviation(nums)
    if r == expected:
        print(colored(f"PASSED => min deviation of: {nums} is {r}", "green"))
    else:
        print(colored(
            f"FAILED => min deviation of: {nums} is {r}, expected is {expected}", "red"))


if __name__ == "__main__":
    test_solution(nums=[1, 2, 3, 4], expected=1)
    test_solution(nums=[4, 1, 5, 20, 3], expected=3)
