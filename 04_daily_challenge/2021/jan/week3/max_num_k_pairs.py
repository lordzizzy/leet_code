# Max Number of K-Sum Pairs

# You are given an integer array nums and an integer k.
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
# Return the maximum number of operations you can perform on the array.


# Example 1:
# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.

# Example 2:
# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.


# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 109
# 1 <= k <= 109

from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # dict that maps number -> frequency
        lookup = {}        
        pairs = 0
        for n in nums:
            if n >= k:
                continue
            if lookup.get(k-n):
                lookup[k-n] -= 1
                pairs += 1
            else:
                if lookup.get(n):
                    lookup[n] += 1
                else:
                    lookup[n] = 1
        return pairs


def checkSolution(nums: List[int], k: int, expected: int):
    s = Solution()
    r = s.maxOperations(nums, k)
    assert r == expected, \
        f"Result: {r} but expected: {expected}"


if __name__ == "__main__":
    checkSolution(nums=[1, 2, 3, 4], k=5, expected=2)
    checkSolution(nums=[3, 1, 3, 4, 3], k=6, expected=1)
