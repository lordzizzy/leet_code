# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3647/

# Broken Calculator
# On a broken calculator that has a number showing on its display, we can
# perform two operations:

# Double: Multiply the number on the display by 2, or;
# Decrement: Subtract 1 from the number on the display.
# Initially, the calculator is displaying the number X.
# Return the minimum number of operations needed to display the number Y.


# Example 1:
# Input: X = 2, Y = 3
# Output: 2
# Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.

# Example 2:
# Input: X = 5, Y = 8
# Output: 2
# Explanation: Use decrement and then double {5 -> 4 -> 8}.

# Example 3:
# Input: X = 3, Y = 10
# Output: 3
# Explanation:  Use double, decrement and double {3 -> 6 -> 5 -> 10}.

# Example 4:
# Input: X = 1024, Y = 1
# Output: 1023
# Explanation: Use decrement operations 1023 times.

# Note:
# 1 <= X <= 10⁹
# 1 <= Y <= 10⁹

# Reasoning and greedy proof of concept notes

# https://leetcode.com/problems/broken-calculator/discuss/236565/Detailed-Proof-Of-Correctness-Greedy-Algorithm

# By working with Y we can guess more about how to proceed. More specifically, if
# Y is odd, we know for sure that we'll have to increment it. Yes, if Y is
# even, we're stuck initially (I believe this greedy algorithm is quite
# ingenious, and it's hard to come up with it quickly), but at least we know
# something. With X this does not work this way, we have no clue whether to
# multiply or to decrement.



# Approach 1: Work Backwards
# Intuition
# Instead of multiplying by 2 or subtracting 1 from X, we could divide by 2
# (when Y is even) or add 1 to Y.

# The motivation for this is that it turns out we always greedily divide by 2:

# If say Y is even, then if we perform 2 additions and one division, we could
# instead perform one division and one addition for less operations [(Y+2) / 2
# vs Y/2 + 1].

# If say Y is odd, then if we perform 3 additions and one division, we could
# instead perform 1 addition, 1 division, and 1 addition for less operations
# [(Y+3) / 2 vs (Y+1) / 2 + 1].

# Algorithm
# While Y is larger than X, add 1 if it is odd, else divide by 2. After, we
# need to do X - Y additions to reach X.

# Approach 2: Recursion
# https://leetcode.com/problems/broken-calculator/discuss/234526/Simple-recursive-solution-considering-only-last-bit-(and-proof-why-it's-guranteed-shortest-path)


from typing import Callable
from termcolor import colored


class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        return self.brokenCalc_work_backwards(X, Y)

    def brokenCalc_work_backwards(self, x: int, y: int) -> int:
        count = 0
        while y > x:
            count += 1
            if y % 2:
                y += 1
            else:
                y //= 2
        return count + (x - y)


SolutionFunc = Callable[[int, int], int]


def test_solution(X: int, Y: int, expected: int):
    def test_impl(func: SolutionFunc, X: int, Y: int, expected: int) -> None:
        r = func(X, Y)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => min operations to transform {X} to {Y} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => min operations to transform {X} to {Y} is {r}, but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.brokenCalc_work_backwards, X, Y, expected)


if __name__ == "__main__":
    test_solution(X=2, Y=3, expected=2)
    test_solution(X=5, Y=8, expected=2)
    test_solution(X=3, Y=10, expected=3)
    test_solution(X=1024, Y=1, expected=1023)
