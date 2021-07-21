# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/610/week-3-july-15th-july-21st/3820/

# Given an integer array nums, design an algorithm to randomly shuffle the
# array. All permutations of the array should be equally likely as a result of
# the shuffling.

# Implement the Solution class:

# Solution(int[] nums) Initializes the object with the integer array nums.
# int[] reset() Resets the array to its original configuration and returns it.
# int[] shuffle() Returns a random shuffling of the array.

# Example 1:
# Input
# ["Solution", "shuffle", "reset", "shuffle"]
# [[[1, 2, 3]], [], [], []]
# Output
# [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

# Explanation
# Solution solution = new Solution([1, 2, 3]);
# solution.shuffle();    // Shuffle the array [1,2,3] and return its result.
#                        // Any permutation of [1,2,3] must be equally likely to be returned.
#                        // Example: return [3, 1, 2]
# solution.reset();      // Resets the array back to its original configuration
# [1,2,3]. Return [1, 2, 3]

# solution.shuffle();    // Returns the random shuffling of array [1,2,3].
# Example: return [1, 3, 2]

# Constraints:

# 1 <= nums.length <= 200
# -10^6 <= nums[i] <= 10^6
# All the elements of nums are unique.
# At most 5 * 10^4 calls in total will be made to reset and shuffle.

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

import random
from itertools import permutations
from typing import List, Protocol

from termcolor import colored


class Solution(Protocol):
    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        ...

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        ...


# Time complexity: O(N)
# Space complexity: O(N)
class Solution_FisherYatesAlgo(Solution):
    def __init__(self, nums: List[int]):
        self._arr = nums
        self._original = list(self._arr)

    def reset(self) -> List[int]:
        self._arr = self._original
        self._original = list(self._original)

        return self._arr

    def shuffle(self) -> List[int]:
        N = len(self._arr)
        arr = self._arr
        # ensure N! permutations
        for i in range(N):
            idx = random.randrange(i, N)
            arr[i], arr[idx] = arr[idx], arr[i]

        return arr


# Time complexity: O(N)
# Space complexity: O(N)
class Solution_Pythonic(Solution):
    def __init__(self, nums: List[int]):
        self._original = nums
        self._shuffled = None

    def reset(self) -> List[int]:
        return self._original

    def shuffle(self) -> List[int]:
        try:
            return list(next(self._shuffled))
        except (TypeError, StopIteration):
            self._shuffled = permutations(self._original)
            return list(next(self._shuffled))
