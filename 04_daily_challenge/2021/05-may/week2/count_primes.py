# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/599/week-2-may-8th-may-14th/3738/

# Count Primes
# Count the number of prime numbers less than a non-negative number, n.

# Example 1:
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Example 2:

# Input: n = 0
# Output: 0

# Example 3:
# Input: n = 1
# Output: 0

# Constraints:
# 0 <= n <= 5 * 10⁶

from typing import Callable, Dict
from termcolor import colored

from math import sqrt


class Solution:
    def countPrimes(self, n: int) -> int:
        return self.countPrimes_sieve_of_eratosthenes_optimized(n)

    # https://leetcode.com/problems/count-primes/discuss/153528/Python3-99-112-ms-Explained%3A-The-Sieve-of-Eratosthenes-with-optimizations
    def countPrimes_sieve_of_eratosthenes_optimized(self, n: int) -> int:
        if n < 3:
            return 0

        strikes = [1] * n
        strikes[0] = 0
        strikes[1] = 0

        for i in range(2, int(sqrt(n)) + 1):
            if strikes[i] != 0:
                strikes[i * i : n : i] = [0] * ((n - 1 - i * i) // i + 1)

        return sum(strikes)

    def countPrimes_sieve_of_eratosthenes_dictionary(self, n: int) -> int:
        if n < 3:
            return 0

        nums: Dict[int, int] = {}
        for p in range(2, int(sqrt(n)) + 1):
            if p not in nums:
                for multiple in range(p * p, n, p):
                    nums[multiple] = 1

        # Exclude "1" and the number "n" itself
        return n - len(nums) - 2

    def countPrimes_fastest_sieve_no_cheat(self, n: int) -> int:
        n -= 1

        if n < 2:
            return 0

        r = int(n ** 0.5)
        V = [n // d for d in range(1, r + 1)]
        V += list(range(V[-1] - 1, 0, -1))

        S = {v: v - 1 for v in V}

        for p in range(2, r + 1):
            if S[p] == S[p - 1]:
                continue
            p2 = p * p
            sp_1 = S[p - 1]
            for v in V:
                if v < p2:
                    break
                S[v] -= S[v // p] - sp_1

        return S[n]


SolutionFunc = Callable[[int], int]


def test_solution(n: int, expected: int) -> None:
    def test_impl(func: SolutionFunc, n: int, expected: int) -> None:
        r = func(n)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Num of primes less than {n} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Num of primes less than {n} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.countPrimes_sieve_of_eratosthenes_optimized, n, expected)
    test_impl(sln.countPrimes_sieve_of_eratosthenes_dictionary, n, expected)
    test_impl(sln.countPrimes_fastest_sieve_no_cheat, n, expected)


if __name__ == "__main__":
    test_solution(n=10, expected=4)