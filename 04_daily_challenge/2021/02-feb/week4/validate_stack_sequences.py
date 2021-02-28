# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3653/

# Validate Stack Sequences
# Given two sequences pushed and popped with distinct values, return true if
# and only if this could have been the result of a sequence of push and pop
# operations on an initially empty stack.

# Example 1:
# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

# Example 2:
# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# Output: false
# Explanation: 1 cannot be popped before 2.


# Constraints:
# 0 <= pushed.length == popped.length <= 1000
# 0 <= pushed[i], popped[i] < 1000
# pushed is a permutation of popped.
# pushed and popped have distinct values.

from typing import Callable, List
from termcolor import colored


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        return self.validateStackSequences_simple_stack(pushed, popped)

    def validateStackSequences_simple_stack(
        self, pushed: List[int], popped: List[int]
    ) -> bool:
        n = len(pushed)
        if n == 0:
            return False
        i = 0
        stack = []
        for p in pushed:
            stack.append(p)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return not stack

    def validateStackSequences_o1_space(
        self, pushed: List[int], popped: List[int]
    ) -> bool:
        i = 0
        j = 0
        for x in pushed:
            pushed[i] = x
            while i >= 0 and pushed[i] == popped[j]:
                i, j = i - 1, j + 1
            i += 1
        return i == 0


SolutionFunc = Callable[[List[int], List[int]], bool]


def test_solution(pushed: List[int], popped: List[int], expected: bool) -> None:
    def test_impl(
        func: SolutionFunc, pushed: List[int], popped: List[int], expected: bool
    ) -> None:
        r = func(pushed, popped)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => {pushed} can be the popped by sequence {popped} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => {pushed} can be the popped by sequence {popped} is {r}, but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.validateStackSequences, pushed, popped, expected)


if __name__ == "__main__":
    test_solution(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1], expected=True)
    test_solution(pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2], expected=False)
