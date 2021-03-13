# Check If a String Contains All Binary Codes of Size K
# Given a binary string s and an integer k.

# Return True if every binary code of length k is a substring of s. Otherwise,
# return False.

# Example 1:
# Input: s = "00110110", k = 2
# Output: true
# Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They
# can be all found as substrings at indicies 0, 1, 3 and 2 respectively.

# Example 2:
# Input: s = "00110", k = 2
# Output: true

# Example 3:
# Input: s = "0110", k = 1
# Output: true
# Explanation: The binary codes of length 1 are "0" and "1", it is clear that
# both exist as a substring.

# Example 4:
# Input: s = "0110", k = 2
# Output: false
# Explanation: The binary code "00" is of length 2 and doesn't exist in the
# array.

# Example 5:
# Input: s = "0000000001011100", k = 4
# Output: false

# Constraints:
# 1 <= s.length <= 5 * 10⁵
# s consists of 0's and 1's only.
# 1 <= k <= 20

from typing import Callable, Set
from termcolor import colored


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return self.hasAllCodes_set_lookup(s, k)

    def hasAllCodes_set_lookup(self, s: str, k: int) -> bool:
        # todo: proof that this is really the min length a valid s with all the
        # binary codes of size k
        if len(s) < k - 1 + 2 ** k:
            return False

        exist: Set[str] = set()
        rem = 2 ** k

        # for each char in s, slide window of K from right to left
        # this is so that i can represent the size of the substring
        for i in range(len(s) - k, -1, -1):
            sub = s[i : (i + k)]
            if sub not in exist:
                exist.add(sub)
                rem -= 1
            # todo: prove why this optimization works
            if i < rem:
                return False
            if rem == 0:
                return True

        return False


SolutionFunc = Callable[[str, int], bool]


def test_solution(s: str, k: int, expected: bool) -> None:
    def test_impl(func: SolutionFunc, s: str, k: int, expected: bool) -> None:
        r = func(s, k)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => {s} contains all binary codes of size {k} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"PASSED {func.__name__} => {s} contains all binary codes of size {k} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.hasAllCodes_set_lookup, s, k, expected)


if __name__ == "__main__":
    test_solution(s="00110110", k=2, expected=True)
    test_solution(s="00110", k=2, expected=True)
    test_solution(s="0110", k=1, expected=True)
    test_solution(s="0110", k=2, expected=False)
    test_solution(s="0000000001011100", k=4, expected=False)
    test_solution(s="011100", k=3, expected=False)
