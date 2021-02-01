# Number of 1 Bits
# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

# Note:

# Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above, the input represents the signed integer. -3.
# Follow up: If this function is called many times, how would you optimize it?


# Example 1:
# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

# Example 2:
# Input: n = 00000000000000000000000010000000
# Output: 1
# Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

# Example 3:
# Input: n = 11111111111111111111111111111101
# Output: 31
# Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.


# Constraints:
# The input must be a binary string of length 32

from termcolor import colored


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n-1
            count += 1
        return count


def test_solution(n: int, expected: int):
    sln = Solution()
    r = sln.hammingWeight(n)
    if r == expected:
        print(colored(
            f"PASSED => hamming weight (num of \"1\" bits) for {n:b} is {r}", "green"))
    else:
        print(colored(
            f"PASSED => hamming weight (num of \"1\" bits) for {n:b} is {r}", "red"))


if __name__ == "__main__":
    test_solution(n=0b00000000000000000000000000001011, expected=3)
    test_solution(n=0b00000000000000000000000010000000, expected=1)
    test_solution(n=0b11111111111111111111111111111101, expected=31)
