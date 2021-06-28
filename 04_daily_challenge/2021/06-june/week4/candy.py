# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/606/week-4-june-22nd-june-28th/3793/

# Candy
# There are n children standing in a line. Each child is assigned a rating
# value given in the integer array ratings.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.

# Example 1:
# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1,
# 2 candies respectively.

# Example 2:
# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2,
# 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.


# Constraints:

# n == ratings.length
# 1 <= n <= 2 * 10⁴
# 0 <= ratings[i] <= 2 * 10⁴

from typing import Callable, List
from termcolor import colored


class Solution:
    # Time complexity: O(N), 2 passes of N to compares, + 1 pass to sum
    # Space complexity: O(N), 2 N for 2 array
    def candy_2_arrays(self, ratings: List[int]) -> int:
        N = len(ratings)
        left, right = [1] * N, [1] * N

        # go left to right and compare ratings and update left arr
        for i in range(1, N):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        # go right to left and compare ratings and update right arr
        for i in reversed(range(N - 1)):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1

        return sum(max(l, r) for l, r in zip(left, right))

    # Time complexity: O(N), 2 passes, 1 left to right + 1 right to left
    # Space complexity: O(N), 1 arr of size N
    def candy_1_array(self, ratings: List[int]) -> int:
        N = len(ratings)
        arr = [1] * N

        # go left to right, compare to left neighbour and update arr
        for i in range(1, N):
            if ratings[i] > ratings[i - 1]:
                arr[i] = arr[i - 1] + 1

        # save last element of arr, then
        # go right to left, compare with right neighbour and update arr and ans
        ans = arr[-1]
        for i in reversed(range(N - 1)):
            if ratings[i] > ratings[i + 1]:
                arr[i] = max(arr[i], arr[i + 1] + 1)
            ans += arr[i]

        return ans

    # Reference
    # https://leetcode.com/problems/candy/discuss/135698/Simple-solution-with-one-pass-using-O(1)-space
    # Time complexity: O(N), 1 pass
    # Space complextiy: O(1), 3 variables: up, down, peaks
    def candy_1pass_peaks(self, ratings: List[int]) -> int:
        N = len(ratings)
        up, down, peak = 0, 0, 0
        ans = 1

        for i in range(1, N):
            if ratings[i - 1] < ratings[i]:
                down = 0
                up += 1
                peak = up
                ans += 1 + up
            elif ratings[i - 1] == ratings[i]:
                peak = up = down = 0
                ans += 1
            else:
                up = 0
                down += 1
                ans += 1 + down + (-1 if peak >= down else 0)

        return ans


SolutionFunc = Callable[[List[int]], int]


def test_solution(ratings: List[int], expected: int) -> None:
    def test_impl(func: SolutionFunc, ratings: List[int], expected: int) -> None:
        r = func(ratings)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Minimum candy to distribute to children with ranks {ratings} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Minimum candy to distribute to children with ranks {ratings} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.candy_2_arrays, ratings, expected)
    test_impl(sln.candy_1_array, ratings, expected)
    test_impl(sln.candy_1pass_peaks, ratings, expected)


if __name__ == "__main__":
    test_solution(ratings=[1, 0, 2], expected=5)
    test_solution(ratings=[1, 2, 2], expected=4)
    test_solution(ratings=[1, 2, 87, 87, 87, 2, 1], expected=13)
    test_solution(
        ratings=[
            12,
            4,
            3,
            11,
            34,
            34,
            1,
        ],
        expected=14,
    )
