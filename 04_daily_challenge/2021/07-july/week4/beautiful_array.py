# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3829/

# Beautiful Array

# An array nums of length n is beautiful if:
# nums is a permutation of the integers in the range [1, n].

# For every 0 <= i < j < n, there is no index k with i < k < j where 2 *
# nums[k] == nums[i] + nums[j].

# Given the integer n, return any beautiful array nums of length n. There will
# be at least one valid answer for the given n.

# Example 1:
# Input: n = 4
# Output: [2,1,4,3]

# Example 2:
# Input: n = 5
# Output: [3,1,2,5,4]

# Constraints:
# 1 <= n <= 1000

#  explanations for this tricky problem
# https://leetcode.com/problems/beautiful-array/discuss/1368125/Detailed-Explanation-with-Diagrams.-A-Collection-of-Ideas-from-Multiple-Posts.-Python3


from typing import Callable, List

from termcolor import colored


class Solution:
    # Time complexity: O(N)
    # Space complexity: O(N)
    def beautifulArray_divide_and_conquer_oddeven_recursive(self, n: int) -> List[int]:
        def divide_and_conquer(l: List[int]) -> List[int]:
            if len(l) < 3:
                return l
            odd = l[::2]
            even = l[1::2]
            return divide_and_conquer(odd) + divide_and_conquer(even)

        return divide_and_conquer(list(range(1, n + 1)))

    # Time complexity: O(N)
    # Space complexity: O(N)
    def beautifulArray_divide_and_conquer_oddeven_iterative(self, n: int) -> List[int]:
        res = [1]
        while len(res) < n:
            res = [i * 2 - 1 for i in res] + [i * 2 for i in res]
        return [i for i in res if i <= n]


SolutionFunc = Callable[[int], List[int]]


def test_solution(n: int, expected: List[int]) -> None:
    def test_impl(func: SolutionFunc, n: int, expected: List[int]) -> None:
        res = func(n)
        if res == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Beatiful array of length {n} is {res}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Beatiful array of length {n} is {res} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.beautifulArray_divide_and_conquer_oddeven_recursive, n, expected)
    test_impl(sln.beautifulArray_divide_and_conquer_oddeven_iterative, n, expected)


def main() -> None:
    test_solution(n=3, expected=[1, 3, 2])
    test_solution(n=4, expected=[1, 3, 2, 4])
    test_solution(n=5, expected=[1, 5, 3, 2, 4])


if __name__ == "__main__":
    main()
