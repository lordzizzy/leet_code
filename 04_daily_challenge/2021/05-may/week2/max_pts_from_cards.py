# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/599/week-2-may-8th-may-14th/3739/

# Maximum Points You Can Obtain from Cards
# There are several cards arranged in a row, and each card has an associated
# number of points The points are given in the integer array cardPoints.

# In one step, you can take one card from the beginning or from the end of the
# row. You have to take exactly k cards.

# Your score is the sum of the points of the cards you have taken.

# Given the integer array cardPoints and the integer k, return the maximum
# score you can obtain.

# Example 1:
# Input: cardPoints = [1,2,3,4,5,6,1], k = 3
# Output: 12
# Explanation: After the first step, your score will always be 1. However,
# choosing the rightmost card first will maximize your total score. The optimal
# strategy is to take the three cards on the right, giving a final score of 1 +
# 6 + 5 = 12.

# Example 2:
# Input: cardPoints = [2,2,2], k = 2
# Output: 4
# Explanation: Regardless of which two cards you take, your score will always
# be 4.

# Example 3:
# Input: cardPoints = [9,7,7,9,7,7,9], k = 7
# Output: 55
# Explanation: You have to take all the cards. Your score is the sum of points
# of all cards.

# Example 4:
# Input: cardPoints = [1,1000,1], k = 1
# Output: 1
# Explanation: You cannot take the card in the middle. Your best score is 1.

# Example 5:
# Input: cardPoints = [1,79,80,1,1,1,200,1], k = 3
# Output: 202

# Constraints:
# 1 <= cardPoints.length <= 10⁵
# 1 <= cardPoints[i] <= 10⁴
# 1 <= k <= cardPoints.length

from typing import Callable, List
from termcolor import colored


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        return self.maxScore_dp_approach1(cardPoints, k)

    def maxScore_dfs_TLE(self, cardPoints: List[int], k: int) -> int:
        def pick(l: int, r: int, k: int) -> int:
            if k == 0:
                return 0
            else:
                return max(
                    cardPoints[l] + pick(l + 1, r, k - 1),
                    cardPoints[r] + pick(l, r - 1, k - 1),
                )

        max_pts = pick(0, len(cardPoints) - 1, k)
        return max_pts

    # https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/discuss/893057/DFS-greater-DP-Progression-9725
    # more dp explanations
    # https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/discuss/598111/Java-dp-solution(explanation-with-picture)
    def maxScore_dp_approach1(self, cardPoints: List[int], k: int) -> int:
        def dp(k: int):
            A = [0 for _ in range(k + 1)]
            A[0] = sum(cardPoints[:k])
            for i in range(1, k + 1):
                A[i] = A[i - 1] - cardPoints[k - i] + cardPoints[-i]
            return max(A)

        return dp(k)

    def maxScore_fastest_dp_o1_space(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints) - k
        minSubArraySum = curr = sum(cardPoints[:size])

        for i in range(len(cardPoints) - size):
            curr += cardPoints[size + i] - cardPoints[i]
            minSubArraySum = min(minSubArraySum, curr)

        return sum(cardPoints) - minSubArraySum

    # https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/discuss/597883/Kt-Js-Py3-Cpp-Brute-Force-Sliding-Window
    def maxScore_sliding_window(self, cardPoints: List[int], k: int) -> int:
        N = len(cardPoints)
        i, j = 0, N - k
        best = total = sum(cardPoints[j:])
        for _ in range(k):
            total += cardPoints[i] - cardPoints[j]
            best = max(best, total)
            i += 1
            j += 1
        return best


SolutionFunc = Callable[[List[int], int], int]


def test_solution(cardPoints: List[int], k: int, expected: int) -> None:
    def test_impl(
        func: SolutionFunc, cardPoints: List[int], k: int, expected: int
    ) -> None:
        r = func(cardPoints, k)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Max points from cards {cardPoints} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Max points from cards {cardPoints} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.maxScore_dfs_TLE, cardPoints, k, expected)
    test_impl(sln.maxScore_dp_approach1, cardPoints, k, expected)
    test_impl(sln.maxScore_fastest_dp_o1_space, cardPoints, k, expected)
    test_impl(sln.maxScore_sliding_window, cardPoints, k, expected)


if __name__ == "__main__":
    test_solution(cardPoints=[2, 2, 2], k=2, expected=4)
    test_solution(cardPoints=[9, 7, 7, 9, 7, 7, 9], k=7, expected=55)
    test_solution(cardPoints=[1, 1000, 1], k=1, expected=1)
    test_solution(cardPoints=[1, 79, 80, 1, 1, 1, 200, 1], k=3, expected=202)
