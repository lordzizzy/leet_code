# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3683/

# Advantage Shuffle
# Given two arrays A and B of equal size, the advantage of A with respect to B
# is the number of indices i for which A[i] > B[i].

# Return any permutation of A that maximizes its advantage with respect to B.

# Example 1:
# Input: A = [2,7,11,15], B = [1,10,4,11]
# Output: [2,11,7,15]

# Example 2:
# Input: A = [12,24,8,32], B = [13,25,32,11]
# Output: [24,32,8,12]

# Note:
# 1 <= A.length = B.length <= 10_000
# 0 <= A[i] <= 10⁹
# 0 <= B[i] <= 10⁹

from typing import Callable, DefaultDict, Dict, List
from termcolor import colored


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        return self.advantageCount_sort(A, B)

    def advantageCount_sort(self, A: List[int], B: List[int]) -> List[int]:
        sA = sorted(A)
        sB = sorted(B)

        assigned: Dict[int, List[int]] = {b: [] for b in B}
        rem: List[int] = []

        j = 0
        for a in sA:
            if a > sB[j]:
                assigned[sB[j]].append(a)
                j += 1
            else:
                rem.append(a)

        return [assigned[b].pop() if assigned[b] else rem.pop() for b in B]

    def advantageCount_sort_elegant(self, A: List[int], B: List[int]) -> List[int]:
        A = sorted(A)
        take = DefaultDict[int, List[int]](lambda: [])
        for b in sorted(B)[::-1]:
            if b < A[-1]:
                take[b].append(A.pop())
        return [(take[b] or A).pop() for b in B]


SolutionFunc = Callable[[List[int], List[int]], List[int]]


def test_solution(A: List[int], B: List[int], expected: List[int]) -> None:
    def test_impl(
        func: SolutionFunc, A: List[int], B: List[int], expected: List[int]
    ) -> None:
        r = func(A, B)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Max advantage permutation of {A} to {B} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Max advantage permutation of {A} to {B} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.advantageCount_sort, A, B, expected)
    test_impl(sln.advantageCount_sort_elegant, A, B, expected)


if __name__ == "__main__":
    test_solution(A=[2, 7, 11, 15], B=[1, 10, 4, 11], expected=[2, 11, 7, 15])
    test_solution(A=[12, 24, 8, 32], B=[13, 25, 32, 11], expected=[24, 32, 8, 12])
