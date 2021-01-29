# https://leetcode.com/problems/student-attendance-record-ii/

# Given a positive integer n, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 10^9 + 7.

# A student attendance record is a string that only contains the following three characters:
# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.
# A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

# Example 1:
# Input: n = 2
# Output: 8
# Explanation:
# There are 8 records with length 2 will be regarded as rewardable:
# "PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# Only "AA" won't be regarded as rewardable owing to more than one absent times.

# Note: The value of n won't exceed 100,000.

# ---------------------------------------------------------------------
# sample 80ms O(log N)
# matrix multiplication sample
# some discussion
# https://leetcode.com/problems/student-attendance-record-ii/discuss/101633/Improving-the-runtime-from-O(n)-to-O(log-n)
# ---------------------------------------------------------------------
# import numpy as np

# class Solution:
#     def checkRecord(self, n: int) -> int:
#         MODULUS = 10**9 + 7

#         initial_counts = np.array(
#             [1, 0, 0, 0, 0, 0],
#             dtype=np.int64
#         )

#         adjacency_matrix = np.array([
#             [1, 1, 1, 0, 0, 0],
#             [1, 0, 0, 0, 0, 0],
#             [0, 1, 0, 0, 0, 0],
#             [1, 1, 1, 1, 1, 1],
#             [0, 0, 0, 1, 0, 0],
#             [0, 0, 0, 0, 1, 0],
#         ], dtype=np.int64)

#         def power(A, exp):
#             B = np.identity(len(A), dtype=np.int64)
#             for bit in reversed(bin(exp)[2:]):
#                 if bit == '1':
#                     B = B @ A
#                     B %= MODULUS
#                 A = A @ A
#                 A %= MODULUS
#             return B

#         final_counts = power(adjacency_matrix, n) @ initial_counts

#         return sum(final_counts) % MODULUS

from termcolor import colored


class Solution:
    def checkRecord(self, n: int) -> int:
        return self.checkRecord_dp(n)

    # DP -> time complexity: O(N), space complexity: O(N)
    # proof and explanation here
    # https://leetcode.com/problems/student-attendance-record-ii/discuss/101643/Share-my-O(n)-C%2B%2B-DP-solution-with-thinking-process-and-explanation
    def checkRecord_dp(self, n: int) -> int:
        if n == 1:
            return 3

        limit = int(1e9+7)

        p = [0] * n
        l = [0] * max(n, 2)
        a = [0] * max(n, 3)

        p[0] = 1
        l[0] = 1
        l[1] = 3
        a[0] = 1
        a[1] = 2
        a[2] = 4

        for i in range(1, n):
            p[i] = (a[i-1] + l[i-1] + p[i-1]) % limit
            if i > 1:
                l[i] = (p[i-1] + a[i-1] + p[i-2] + a[i-2]) % limit
            if i > 2:
                a[i] = (a[i-1] + a[i-2] + a[i-3]) % limit

        return (a[n-1] + p[n-1] + l[n-1]) % limit


def test_solution(n: int, expected: int):
    sln = Solution()
    r = sln.checkRecord(n)
    if r == expected:
        print(
            colored(f"PASSED => rewardable records for length {n} is {r}.", "green"))
    else:
        print(colored(
            f"FAILED => rewardable records for length {n} is {r}, but expected: {expected}", "red"))


if __name__ == "__main__":
    test_solution(n=2, expected=8)
    test_solution(n=3, expected=19)
