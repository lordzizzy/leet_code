# Letter Case Permutation
# Given a string S, we can transform every letter individually to be lowercase
# or uppercase to create another string.
# Return a list of all possible strings we could create. You can return the
# output in any order.

# Example 1:
# Input: S = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]

# Example 2:
# Input: S = "3z4"
# Output: ["3z4","3Z4"]

# Example 3:
# Input: S = "12345"
# Output: ["12345"]

# Example 4:
# Input: S = "0"
# Output: ["0"]

# Constraints:
# S will be a string with length between 1 and 12.
# S will consist only of letters or digits.

from typing import Callable, Deque, List
from termcolor import colored


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        return self.letterCasePermutation_bfs(S)

    def letterCasePermutation_bfs(self, S: str) -> List[str]:
        q = Deque[str]([S])
        for i, c in enumerate(S):
            if "0" <= c <= "9":
                continue
            for _ in range(len(q)):
                curr = q.popleft()
                q.append(curr[:i] + c.lower() + curr[i + 1 :])
                q.append(curr[:i] + c.upper() + curr[i + 1 :])
        return list(q)

    def letterCasePermutation_dfs(self, S: str) -> List[str]:
        raise NotImplementedError()

    def letterCasePermutation_build_from_base(self, S: str) -> List[str]:
        perms = [""]
        for c in S:
            if c.isdigit():
                perms = [p + c for p in perms]
            else:
                perms = [p + ch for p in perms for ch in (c.lower(), c.upper())]
        return perms


SolutionFunc = Callable[[str], List[str]]


def test_solution(S: str, expected: List[str]) -> None:
    def test_impl(func: SolutionFunc, S: str, expected: List[str]) -> None:
        r = func(S)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => '{S}' letter case permutations are {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"PASSED {func.__name__} => '{S}' letter case permutations are {r}, but expected: {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.letterCasePermutation_bfs, S, expected)
    test_impl(sln.letterCasePermutation_build_from_base, S, expected)


if __name__ == "__main__":
    test_solution(S="a1b2", expected=["a1b2", "a1B2", "A1b2", "A1B2"])
    test_solution(S="3z4", expected=["3z4", "3Z4"])
    test_solution(S="12345", expected=["12345"])
    test_solution(S="0", expected=["0"])
