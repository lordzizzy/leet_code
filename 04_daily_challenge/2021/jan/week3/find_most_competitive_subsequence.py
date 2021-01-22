# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3611/

# Find the Most Competitive Subsequence
# Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.
# An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.
# We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position where a and b differ, subsequence a has a number less than the corresponding number in b. For example, [1,3,4] is more competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.


# Example 1:
# Input: nums = [3,5,2,6], k = 2
# Output: [2,6]
# Explanation: Among the set of every possible subsequence: {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}, [2,6] is the most competitive.

# Example 2:
# Input: nums = [2,4,3,3,5,4,9,6], k = 4
# Output: [2,3,3,4]

# Constraints:
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9
# 1 <= k <= nums.length

# credits goes to the super guy person who did this:
# https://leetcode.com/problems/find-the-most-competitive-subsequence/discuss/1027495/Python-Stack-solution-explained

from typing import List
from termcolor import colored


class Solution:
    def mostCompetitive(self, nums, k):
        attempts = len(nums) - k
        stack = []
        for num in nums:
            while stack and num < stack[-1] and attempts > 0:
                stack.pop()
                attempts -= 1
            stack.append(num)

        return stack[:k]


def test_Solution(nums: List[int], k: int, expected: List[int]):
    sln = Solution()
    r = sln.mostCompetitive(nums, k)
    if r == expected:
        print(
            f"PASSED - most competitive subsquence for {nums} with k={k} is {r}")
    else:
        print(colored(
            f"FAILED - most competitive subsquence for {nums} with k={k} is {r} but expected {expected}", "red"))


if __name__ == '__main__':
    # test_Solution(nums=[3, 5, 2, 6], k=2, expected=[2, 6])
    test_Solution(nums=[2, 4, 3, 3, 5, 4, 9, 6], k=4, expected=[2, 3, 3, 4])
