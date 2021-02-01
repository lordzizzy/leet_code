# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3618/

# Concatenation of Consecutive Binary Numbers
# Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 10^9 + 7.

# Example 1:
# Input: n = 1
# Output: 1
# Explanation: "1" in binary corresponds to the decimal value 1.

# Example 2:
# Input: n = 3
# Output: 27
# Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
# After concatenating them, we have "11011", which corresponds to the decimal value 27.

# Example 3:
# Input: n = 12
# Output: 505379714
# Explanation: The concatenation results in "1101110010111011110001001101010111100".
# The decimal value of that is 118505380540.
# After modulo 109 + 7, the result is 505379714.

# Constraints:
# 1 <= n <= 10^5

# generator expressions
# class Solution:
#     def concatenatedBinary(self, n: int) -> int:
#         MOD = 10 ** 9 + 7
#         str_num = ''.join(str(bin(i))[2:] for i in range(1, n + 1))
#         return int(str_num, 2) % MOD

# 52 ms sample
# dp=[0]
# mod = 1000000000 + 7
# class Solution:
#     def concatenatedBinary(self, n: int) -> int:
#         if n>len(dp)-1:
#             ans = dp[len(dp)-1]
#             l = floor(log2(len(dp)))+1
#             for i in range(len(dp), n+1):
#                 ans <<=l
#                 ans += i
#                 ans %= mod
#                 dp.append(ans)
#                 if (i & (i+1))==0: l+=1
#         return dp[n]

# best bit-shifting solution 44ms python
# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/discuss/1037348/Python-3-Bit-manipulation-4-solutions-1-line-O(n)-44ms


from typing import Callable, Generator
from typing import List
from termcolor import colored
from math import floor, log2


class Solution:
    def __init__(self) -> None:
        self._cache: List[int] = [0]

    def concatenatedBinary(self, n: int) -> int:
        # return self.concat_binary_chau_keng(n)
        return self.concat_binary_bitshift(n)

    def concat_binary_chau_keng(self, n: int) -> int:
        def genBinaryStr(n: int) -> Generator[str, None, None]:
            for i in range(1, n+1):
                yield f"{i:b}"
        bstr: str = "".join(genBinaryStr(n))
        ans = int(bstr, base=2) % int(1e9+7)
        return ans

    def concat_binary_bitshift(self, n: int) -> int:
        cache_size: int = len(self._cache)
        if n < cache_size:
            return self._cache[n]
        limit: int = int(1e9+7)
        ans: int = self._cache[-1]
        shift: int = floor(log2(cache_size))+1
        for i in range(cache_size, n+1):
            ans <<= shift
            ans %= limit
            ans += i
            self._cache.append(ans)
            # if we are about to overflow in the next iteration
            # then add 1 to shift, eg. 1, 11, 111
            if (i & (i+1)) == 0:
                shift += 1
        return ans


def test_concatenatedBinary(n: int, expected: int):
    def test_impl(func: Callable[[int], int], n: int, expected: int):
        r = func(n)
        if r == expected:
            print(colored(
                f"PASSED =>({func.__name__}) 1 to {n} concatenated binary mod 10^9+7's decimal value is: {r}", "green"))
        else:
            print(colored(
                f"FAILED =>({func.__name__}) 1 to {n} concatenated binary mod 10^9+7's decimal value is: {r}, but expected {expected}", "red"))

    sln = Solution()
    test_impl(sln.concat_binary_chau_keng, n, expected)
    test_impl(sln.concat_binary_bitshift, n, expected)


if __name__ == "__main__":
    test_concatenatedBinary(n=1, expected=1)
    test_concatenatedBinary(n=3, expected=27)
    test_concatenatedBinary(n=12, expected=505379714)
