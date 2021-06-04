# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/603/week-1-june-1st-june-7th/3766/

# Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

# Given a rectangular cake with height h and width w, and two arrays of
# integers horizontalCuts and verticalCuts where horizontalCuts[i] is the
# distance from the top of the rectangular cake to the ith horizontal cut and
# similarly, verticalCuts[j] is the distance from the left of the rectangular
# cake to the jth vertical cut.

# Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a huge number, return this modulo 10^9 + 7.


# Example 1:
# Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
# Output: 4
# Explanation: The figure above represents the given rectangular cake. Red
# lines are the horizontal and vertical cuts. After you cut the cake, the green
# piece of cake has the maximum area.

# Example 2:
# Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
# Output: 6
# Explanation: The figure above represents the given rectangular cake. Red
# lines are the horizontal and vertical cuts. After you cut the cake, the green
# and yellow pieces of cake have the maximum area.

# Example 3:
# Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
# Output: 9

# Constraints:

# 2 <= h, w <= 10⁹
# 1 <= horizontalCuts.length < min(h, 10⁵)
# 1 <= verticalCuts.length < min(w, 10⁵)
# 1 <= horizontalCuts[i] < h
# 1 <= verticalCuts[i] < w
# It is guaranteed that all elements in horizontalCuts are distinct.
# It is guaranteed that all elements in verticalCuts are distinct.

from typing import Callable, List
from termcolor import colored


class Solution:
    # https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/discuss/1248641/Python-simple-3-lines-math-solution-explained
    def maxArea(
        self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]
    ) -> int:
        H = sorted([0] + horizontalCuts + [h])
        V = sorted([0] + verticalCuts + [w])
        max_h = max(j - i for i, j in zip(H, H[1:]))
        max_w = max(j - i for i, j in zip(V, V[1:]))
        return (max_w * max_h) % (10 ** 9 + 7)


SolutionFunc = Callable[[int, int, List[int], List[int]], int]


def test_solution(
    h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int], expected: int
) -> None:
    def test_impl(
        func: SolutionFunc,
        h: int,
        w: int,
        horizontalCuts: List[int],
        verticalCuts: List[int],
        expected: int,
    ) -> None:
        r = func(h, w, horizontalCuts, verticalCuts)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Max area for rect height:{h}xwidth:{w} with h-cuts:{horizontalCuts} and v-cuts:{verticalCuts} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Max area for rect height:{h}xwidth:{w} with h-cuts:{horizontalCuts} and v-cuts:{verticalCuts} is {r}, but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.maxArea, h, w, horizontalCuts, verticalCuts, expected)


if __name__ == "__main__":
    test_solution(h=5, w=4, horizontalCuts=[1, 2, 4], verticalCuts=[1, 3], expected=4)
    test_solution(h=5, w=4, horizontalCuts=[3, 1], verticalCuts=[1], expected=6)
    test_solution(h=5, w=4, horizontalCuts=[3], verticalCuts=[3], expected=9)
