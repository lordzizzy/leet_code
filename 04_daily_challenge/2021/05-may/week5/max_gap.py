# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/602/week-5-may-29th-may-31st/3761/

# Maximum Gap
# Given an integer array nums, return the maximum difference between two
# successive elements in its sorted form. If the array contains less than two
# elements, return 0.

# You must write an algorithm that runs in linear time and uses linear extra
# space.

# Example 1:
# Input: nums = [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9)
# has the maximum difference 3.

# Example 2:
# Input: nums = [10]
# Output: 0
# Explanation: The array contains less than 2 elements, therefore return 0.

# Constraints:
# 1 <= nums.length <= 10⁴
# 0 <= nums[i] <= 10⁹

# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/602/week-5-may-29th-may-31st/3761/

# Maximum Gap
# Given an integer array nums, return the maximum difference between two
# successive elements in its sorted form. If the array contains less than two
# elements, return 0.

# You must write an algorithm that runs in linear time and uses linear extra
# space.

# Example 1:

# Input: nums = [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9)
# has the maximum difference 3.

# Example 2:
# Input: nums = [10]
# Output: 0
# Explanation: The array contains less than 2 elements, therefore return 0.

# Constraints:
# 1 <= nums.length <= 10⁴
# 0 <= nums[i] <= 10⁵

from typing import Callable, DefaultDict, List
from termcolor import colored


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        return self.maximumGap_bucketsort(nums)

    # pigeonhole principle
    # https://leetcode.com/problems/maximum-gap/discuss/1240543/Python-Bucket-sort-explained
    def maximumGap_bucketsort(self, nums: List[int]) -> int:
        N = len(nums)
        lo, hi = min(nums), max(nums)
        if N <= 2 or lo == hi:
            return hi - lo
        B = DefaultDict[int, List[int]](list)
        for num in nums:
            idx = N - 2 if num == hi else (num - lo) * (N - 1) // (hi - lo)
            B[idx].append(num)

        cands = [(min(B[i]), max(B[i])) for i in range(N - 1) if B[i]]
        return max(y[0] - x[1] for x, y in zip(cands, cands[1:]))


SolutionFunc = Callable[[List[int]], int]


def test_solution(nums: List[int], expected: int) -> None:
    def test_impl(func: SolutionFunc, nums: List[int], expected: int) -> None:
        r = func(nums)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Maximum gap of {nums} is {r}", "green"
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Maximum gap of {nums} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.maximumGap_bucketsort, nums, expected)


if __name__ == "__main__":
    test_solution(nums=[3, 6, 9, 1], expected=3)
    test_solution(nums=[10], expected=0)
