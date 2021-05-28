# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/601/week-4-may-22nd-may-28th/3758/

# Maximum Erasure Value
# You are given an array of positive integers nums and want to erase a subarray
# containing unique elements. The score you get by erasing the subarray is
# equal to the sum of its elements.

# Return the maximum score you can get by erasing exactly one subarray.

# An array b is called to be a subarray of a if it forms a contiguous
# subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some
# (l,r).

# Example 1:
# Input: nums = [4,2,4,5,6]
# Output: 17
# Explanation: The optimal subarray here is [2,4,5,6].

# Example 2:
# Input: nums = [5,2,1,2,5,2,1,2,5]
# Output: 8
# Explanation: The optimal subarray here is [5,2,1] or [1,2,5].

# Constraints:
# 1 <= nums.length <= 10⁵
# 1 <= nums[i] <= 10⁴

from typing import Callable, List, Set
from termcolor import colored


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        return self.maximumUniqueSubarray_sliding_window_TLE(nums)

    # notes: summing set to get max does not seem to be faster than keeping a
    # cur value and updating it
    def maximumUniqueSubarray_sliding_window_TLE(self, nums: List[int]) -> int:
        ans = 0
        seen: Set[int] = set()
        # sliding window: [l, r]
        l = 0
        for r in range(len(nums)):
            # keep shifting the left window right and remove number from seen
            # until there is no num[r] in seen set
            while nums[r] in seen:
                seen.remove(nums[l])
                l += 1
            seen.add(nums[r])
            ans = max(ans, sum(seen))
        return ans

    def maximumUniqueSubarray_sliding_window_pass(self, nums: List[int]) -> int:
        ans = 0
        seen: Set[int] = set()
        cur = 0
        # sliding window: [l, r]
        l = 0
        for r in range(len(nums)):
            # keep shifting the left window right and remove number from seen
            # until there is no num[r] in seen set
            while nums[r] in seen:
                seen.remove(nums[l])
                cur -= nums[l]
                l += 1
            seen.add(nums[r])
            cur += nums[r]
            ans = max(ans, cur)
        return ans


SolutionFunc = Callable[[List[int]], int]


def test_solution(nums: List[int], expected: int) -> None:
    def test_impl(func: SolutionFunc, nums: List[int], expected: int) -> None:
        r = func(nums)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Maximum erasure value for {nums} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Maximum erasure value for {nums} is {r} bur expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.maximumUniqueSubarray_sliding_window_pass, nums, expected)
    test_impl(sln.maximumUniqueSubarray_sliding_window_TLE, nums, expected)


if __name__ == "__main__":
    test_solution(nums=[4, 2, 4, 5, 6], expected=17)
    test_solution(nums=[5, 2, 1, 2, 5, 2, 1, 2, 5], expected=8)
