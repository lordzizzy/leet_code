# Longest Harmonious Subsequence
# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3628/

# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

# A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

# Example 1:
# Input: nums = [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].

# Example 2:
# Input: nums = [1,2,3,4]
# Output: 2

# Example 3:
# Input: nums = [1,1,1,1]
# Output: 0

# Constraints:
# 1 <= nums.length <= 2 * 10^4
# -10^9 <= nums[i] <= 10^9

# cool C hashmap solution to study
# https://leetcode.com/problems/longest-harmonious-subsequence/discuss/143853/Hashmap-based-C-solution/150916

# performant counter solution
# from collections import Counter
# class Solution:
#     def findLHS(self, nums: List[int]) -> int:
#         d = Counter(nums)
#         result = 0

#         for k, v in d.items():
#             if k+1 in d:
#                 length = d[k+1] + v
#                 result = max(result,length)

#         return result


from typing import DefaultDict, List
from termcolor import colored


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        return self.findLHS_dict(nums)
        # return self.findLHS_brute_force(nums)

    def findLHS_brute_force(self, nums: List[int]) -> int:
        n = len(nums)
        longest = 0
        for i in range(0, n):
            seq = 0
            found = False
            num = nums[i]
            candidate = num + 1
            # left range
            for j in reversed(range(0, i)):
                curr = nums[j]
                if curr == num or curr == candidate:
                    seq = seq + 1
                if curr == candidate:
                    found = True
            # right range
            for j in range(i+1, n):
                curr = nums[j]
                if curr == num or curr == candidate:
                    seq = seq + 1
                if curr == candidate:
                    found = True
            # update longest
            if found and seq > 0:
                longest = max(seq+1, longest)

        return longest

    def findLHS_dict(self, nums: List[int]) -> int:
        longest = 0
        dic = DefaultDict(int)
        for num in nums:
            dic[num] += 1
        for num in dic:
            if dic.get(num+1, 0) > 0:
                longest = max(dic[num] + dic[num+1], longest)
        return longest


def test_solution(nums: List[int], expected: int):
    def test_impl(func, nums, expected):
        r = func(nums)
        if r == expected:
            print(colored(
                f"PASSED {func.__name__}=> longest harmonious subsequence for {nums} is {r}", "green"))
        else:
            print(colored(
                f"FAILED {func.__name__}=> longest harmonious subsequence for {nums} is {r}, but expected: {expected}", "red"))
    sln = Solution()
    test_impl(sln.findLHS_brute_force, nums, expected)
    test_impl(sln.findLHS_dict, nums, expected)


if __name__ == "__main__":
    test_solution(nums=[1, 3, 2, 2, 5, 2, 3, 7], expected=5)
    test_solution(nums=[1, 2, 3, 4], expected=2)
    test_solution(nums=[1, 1, 1, 1], expected=0)
