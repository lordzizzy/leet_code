# https://leetcode.com/problems/push-dominoes/

# 838. Push Dominoes

# There are n dominoes in a line, and we place each domino vertically upright.
# In the beginning, we simultaneously push some of the dominoes either to the
# left or to the right.

# After each second, each domino that is falling to the left pushes the
# adjacent domino on the left. Similarly, the dominoes falling to the right
# push their adjacent dominoes standing on the right.

# When a vertical domino has dominoes falling on it from both sides, it stays
# still due to the balance of the forces.

# For the purposes of this question, we will consider that a falling domino
# expends no additional force to a falling or already fallen domino.

# You are given a string dominoes representing the initial state where:

# dominoes[i] = 'L', if the ith domino has been pushed to the left,
# dominoes[i] = 'R', if the ith domino has been pushed to the right, and
# dominoes[i] = '.', if the ith domino has not been pushed.
# Return a string representing the final state.

# Example 1:
# Input: dominoes = "RR.L"
# Output: "RR.L"
# Explanation: The first domino expends no additional force on the second
# domino.

# Example 2:
# Input: dominoes = ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."

# Constraints:
# n == dominoes.length
# 1 <= n <= 10^5
# dominoes[i] is either 'L', 'R', or '.'.

from typing import Callable, Literal, Optional, Union

from termcolor import colored


class Solution:
    # Time complexity: O(N)
    # Space complexity: O(N)
    def pushDominoes_adjacent_symbols(self, dominoes: str) -> str:
        # we need to define this func manually because python 3 does not have a
        # built-in cmp function anymore.
        def cmp(a: int, b: int) -> Union[Literal[-1], Literal[0], Literal[1]]:
            if a == b:
                return 0
            else:
                return -1 if a < b else 1

        symbols = [(i, d) for i, d in enumerate(dominoes) if d != "."]
        symbols = [(-1, "L")] + symbols + [(len(dominoes), "R")]

        ans = list(dominoes)

        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            if x == y:
                for k in range(i + 1, j):
                    ans[k] = x
            elif x > y:
                for k in range(i + 1, j):
                    ans[k] = ".LR"[cmp(k - i, j - k)]

        return "".join(ans)

    # Time complexity: O(N)
    # Space complexity: O(N)
    def pushDominoes_2passes(self, dominoes: str) -> str:
        N = len(dominoes)
        lst, dists = list(dominoes), [0] * N
        rDist: Optional[int] = None

        for i, val in enumerate(lst):
            if val == "R":
                rDist = 0
            elif val == "L":
                rDist = None
            elif rDist != None:
                rDist += 1
                dists[i] = rDist
                lst[i] = "R"

        lDist: Optional[int] = None

        for i in reversed(range(N)):
            if dominoes[i] == "L":
                lDist = 0
            elif dominoes[i] == "R":
                lDist = None
            elif lDist != None:
                lDist += 1
                if lDist < dists[i] or lst[i] == ".":
                    lst[i] = "L"
                elif lDist == dists[i]:
                    lst[i] = "."

        return "".join(lst)


SolutionFunc = Callable[[str], str]


def test_solution(dominoes: str, expected: str) -> None:
    def test_impl(func: SolutionFunc, dominoes: str, expected: str) -> None:
        res = func(dominoes)
        if res == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Dominoes final state with initial state {dominoes} is {res}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Dominoes final state with initial state {dominoes} is {res} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.pushDominoes_adjacent_symbols, dominoes, expected)
    test_impl(sln.pushDominoes_2passes, dominoes, expected)


if __name__ == "__main__":
    test_solution(dominoes="RR.L", expected="RR.L")
    test_solution(dominoes=".L.R...LR..L..", expected="LL.RR.LLRRLL..")
