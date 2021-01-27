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

from typing import Generator
from termcolor import colored


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        def genBinaryStr(n: int) -> Generator[str, None, None]:
            for i in range(1, n+1):
                yield f"{i:b}"            
        
        bstr: str = "".join(genBinaryStr(n))
        ans = int(bstr, base=2) % int(1e9+7)
        return ans


def test_concatenatedBinary(n: int, expected: int):
    sln = Solution()
    r = sln.concatenatedBinary(n)
    if r == expected:
        print(colored(
            f"PASSED => 1 to {n} concatenated binary mod 10^9+7's decimal value is: {r}", "green"))
    else:
        print(colored(
            f"FAILED => 1 to {n} concatenated binary mod 10^9+7's decimal value is: {r}, but expected {expected}", "red"))


if __name__ == "__main__":
    test_concatenatedBinary(n=1, expected=1)
    test_concatenatedBinary(n=3, expected=27)
