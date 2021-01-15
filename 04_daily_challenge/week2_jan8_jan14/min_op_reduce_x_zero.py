
# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3603/

# You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

# Return the minimum number of operations to reduce x to exactly 0 if it's possible, otherwise, return -1.

# Example 1:

# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
# Example 2:

# Input: nums = [5,6,7,8,9], x = 4
# Output: -1
# Example 3:

# Input: nums = [3,2,20,1,1,3], x = 10
# Output: 5
# Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
# 1 <= x <= 109

from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        rem = 0
        for y in nums:
            rem += y
        rem -= x

        if rem == 0:
            return n
        if rem < 0:
            return -1

        largest = 0
        start = end = 0
        total = 0

        for i in range(0, n):
            end = i
            total += nums[end]
            while rem < total and start < end:
                total -= nums[start]
                start += 1
            if total == rem:
                largest = max(largest, end - start + 1)

        if largest == 0:
            return -1

        return n - largest


if __name__ == "__main__":
    s = Solution()

    assert 16 == s.minOperations(nums=[8828, 9581, 49, 9818, 9974, 9869, 9991,
                                       10000, 10000, 10000, 9999, 9993, 9904, 8819, 1231, 6309], x=134365)
    assert -1 == s.minOperations(nums=[1, 1], x=3)
    assert 1 == s.minOperations(nums=[5, 2, 3, 1, 1], x=5)
    assert 2 == s.minOperations(nums=[1, 1, 4, 2, 3], x=5)
    assert -1 == s.minOperations(nums=[5, 6, 7, 8, 9], x=4)
    assert 5 == s.minOperations(nums=[3, 2, 20, 1, 1, 3], x=10)
