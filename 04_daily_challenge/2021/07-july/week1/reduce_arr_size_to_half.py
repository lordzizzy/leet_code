# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/608/week-1-july-1st-july-7th/3804/

# Reduce Array Size to The Half

# Solution
# Given an array arr.  You can choose a set of integers and remove all the
# occurrences of these integers in the array.

# Return the minimum size of the set so that at least half of the integers of
# the array are removed.

# Example 1:
# Input: arr = [3,3,3,3,5,5,5,2,2,7]
# Output: 2
# Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has
# size 5 (i.e equal to half of the size of the old array).

# Possible sets of size 2 are {3,5},{3,2},{5,2}.
# Choosing set {2,7} is not possible as it will make the new array
# [3,3,3,3,5,5,5] which has size greater than half of the size of the old
# array.

# Example 2:
# Input: arr = [7,7,7,7,7,7]
# Output: 1
# Explanation: The only possible set you can choose is {7}. This will make the
# new array empty.

# Example 3:
# Input: arr = [1,9]
# Output: 1

# Example 4:
# Input: arr = [1000,1000,3,7]
# Output: 1

# Example 5:
# Input: arr = [1,2,3,4,5,6,7,8,9,10]
# Output: 5

# Constraints:

# 1 <= arr.length <= 10^5
# arr.length is even.
# 1 <= arr[i] <= 10^5

from typing import Callable, Counter, List

from termcolor import colored


class Solution:
    # Time complexity: O(N logN) * can be O(N) if we use bucket sort, refer to
    # https://leetcode.com/problems/top-k-frequent-elements/discuss/740374/Python-5-lines-O(n)-buckets-solution-explained.
    # Space complexity: O(N)
    def minSetSize_counter_and_sort(self, arr: List[int]) -> int:
        res, half = 0, len(arr) // 2
        c = Counter(arr)
        for i in sorted(c.values(), reverse=True):
            half -= i
            res += 1
            if half <= 0:
                break
        return res


SolutionFunc = Callable[[List[int]], int]


def test_solution(arr: List[int], expected: int) -> None:
    def test_impl(func: SolutionFunc, arr: List[int], expected: int) -> None:
        r = func(arr)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Min size of set so at least half of integers of the {arr} are removed is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Min size of set so at least half of integers of the {arr} are removed is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.minSetSize_counter_and_sort, arr, expected)


if __name__ == "__main__":
    test_solution(arr=[3, 3, 3, 3, 5, 5, 5, 2, 2, 7], expected=2)
    test_solution(arr=[7, 7, 7, 7, 7, 7], expected=1)
    test_solution(arr=[1, 9], expected=1)
    test_solution(arr=[1000, 1000, 3, 7], expected=1)
    test_solution(arr=[7, 3, 3, 1000, 1000], expected=1)
    test_solution(arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], expected=5)
