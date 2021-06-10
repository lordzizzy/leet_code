# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3773/

# Jump Game VI

# You are given a 0-indexed integer array nums and an integer k.

# You are initially standing at index 0. In one move, you can jump at most k
# steps forward without going outside the boundaries of the array. That is, you
# can jump from index i to any index in the range [i + 1, min(n - 1, i + k)]
# inclusive.

# You want to reach the last index of the array (index n - 1). Your score is
# the sum of all nums[j] for each index j you visited in the array.

# Return the maximum score you can get.

# Example 1:
# Input: nums = [1,-1,-2,4,-7,3], k = 2
# Output: 7
# Explanation: You can choose your jumps forming the subsequence [1,-1,4,3]
# (underlined above). The sum is 7.

# Example 2:
# Input: nums = [10,-5,-2,4,0,3], k = 3
# Output: 17
# Explanation: You can choose your jumps forming the subsequence [10,4,3]
# (underlined above). The sum is 17.

# Example 3:
# Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
# Output: 0

# Constraints:
# 1 <= nums.length, k <= 10⁵
# -10⁴ <= nums[i] <= 10⁴

from collections import deque
from typing import Callable, List
from termcolor import colored

# references and ideas from
# https://leetcode.com/problems/jump-game-vi/discuss/978497/Python-DP-%2B-Sliding-Window-Maximum-problem-combined


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        return self.maxResult_dp_monoqueue(nums, k)

    # dp stores max score at index i
    # dp[i] = nums[i] +  max(dp[i-k], dp[i-k+1], .. dp[i-1])
    #
    # deq is monotone queue that hold the index of "max dp score between i to i-k" in its
    # first element
    #
    # Time complexity = O(N), Space complexity = O(N+K)
    def maxResult_dp_monoqueue(self, nums: List[int], k: int) -> int:
        deq, N = deque([0]), len(nums)
        dp = [0] * N
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = nums[i] + dp[deq[0]]

            while deq and dp[deq[-1]] < dp[i]:
                deq.pop()

            deq.append(i)

            if deq[0] == i - k:
                deq.popleft()

        return dp[-1]

    # using in-place array "nums" as dp storage
    #
    # Time complexity = O(N), Space complexity = O(K)
    def maxResult_dp_inplace_monoqueue(self, nums: List[int], k: int) -> int:
        deq, N = deque([0]), len(nums)

        for i in range(1, N):
            nums[i] += nums[deq[0]]
            while deq and nums[i] >= nums[deq[-1]]:
                deq.pop()

            deq.append(i)

            if deq[0] == i - k:
                deq.popleft()

        return nums[-1]

    # Leetcode's fastest solution
    def maxResult_dp_fastest(self, nums: List[int], k: int) -> int:
        dp = [0] * len(nums)
        l = r = 0
        for i in range(len(nums)):
            if i > l + k:
                l, r = r, r + 1
            dp[i] = dp[l] + nums[i]
            if dp[i] >= dp[l]:
                l, r = i, i + 1
            elif dp[i] >= dp[r]:
                r = i
        return dp[-1]


SolutionFunc = Callable[[List[int], int], int]


def test_solution(nums: List[int], k: int, expected: int) -> None:
    def test_impl(func: SolutionFunc, nums: List[int], k: int, expected: int) -> None:
        r = func(nums, k)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Max score from {nums} with {k} steps is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Max score from {nums} with {k} steps is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.maxResult_dp_monoqueue, nums, k, expected)
    test_impl(sln.maxResult_dp_inplace_monoqueue, nums.copy(), k, expected)
    test_impl(sln.maxResult_dp_fastest, nums, k, expected)


if __name__ == "__main__":
    test_solution(nums=[10, -5, -2, 4, 0, 3], k=3, expected=17)
    test_solution(nums=[1, -1, -2, 4, -7, 3], k=2, expected=7)
    test_solution(nums=[1, -5, -20, 4, -1, 3, -6, -3], k=2, expected=0)
