# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/601/week-4-may-22nd-may-28th/3753/

# Find the Shortest Superstring
# Given an array of strings words, return the smallest string that contains
# each string in words as a substring. If there are multiple valid strings of
# the smallest length, return any of them.

# You may assume that no string in words is a substring of another string in
# words.

# Example 1:
# Input: words = ["alex","loves","leetcode"]
# Output: "alexlovesleetcode"
# Explanation: All permutations of "alex","loves","leetcode" would also be
# accepted.

# Example 2:
# Input: words = ["catg","ctaagt","gcta","ttca","atgcatc"]
# Output: "gctaagttcatgcatc"

# Constraints:
# 1 <= words.length <= 12
# 1 <= words[i].length <= 20
# words[i] consists of lowercase English letters.
# All the strings of words are unique.

# Self notes:
# this is basically the travelling salesman problem, where the order of the
# words to be concatenated to form the shortest string

from typing import Callable, List
from termcolor import colored
from itertools import product
from heapq import heappush, heappop


class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        return self.shortestSuperstring_dp_iterative(words)

    def shortestSuperstring_dp_iterative(self, A: List[str]) -> str:
        # construct a directed graph
        # node i => A[i]
        # weights are represented as an adjacency matrix:
        # shared[i][j] => length saved by concatenating A[i] and A[j]
        N = len(A)
        shared = [[0] * N for _ in range(N)]
        for i, j in product(range(N), range(N)):
            for k in range(min(len(A[i]), len(A[j])), 0, -1):
                if A[i][-k:] == A[j][:k]:
                    shared[i][j] = k
                    break

        # The problem becomes finding the shortest path that visits all nodes exactly once.
        # Brute force DFS would take O(n!) time.
        # A DP solution costs O(n^2 2^n) time.
        #
        # Let's consider integer from 0 to 2^n - 1.
        # Each i contains 0-n 1 bits. Hence each i selects a unique set of strings in A.
        # Let's denote set(i) => {A[j] | j-th bit of i is 1}
        # dp[i][k] => shortest superstring of set(i) ending with A[k]
        #
        # e.g.
        #   if i = 6 i.e. 110 in binary. dp[6][k] considers superstring of A[2] and A[1].
        #   dp[6][1] => the shortest superstring of {A[2], A[1]} ending with A[1].
        #   For this simple case dp[6][1] = concatenate(A[2], A[1])
        dp = [[""] * 12 for _ in range(1 << 12)]
        for i in range(1 << N):
            for k in range(N):
                # skip if A[k] is not in set(i)
                if not (i & (1 << k)):
                    continue
                # if set(i) == {A[k]}
                if i == 1 << k:
                    dp[i][k] = A[k]
                    continue
                for j in range(N):
                    if j == k:
                        continue
                    if i & (1 << j):
                        # the shortest superstring if we remove A[k] from the
                        # set(i)
                        s = dp[i ^ (1 << k)][j]
                        s += A[k][shared[j][k] :]
                        if dp[i][k] == "" or len(s) < len(dp[i][k]):
                            dp[i][k] = s

        min_len = float("inf")
        result = ""

        # find the shortest superstring of all candidates ending with different
        # string
        for k in range(N):
            s = dp[(1 << N) - 1][k]
            if len(s) < min_len:
                min_len, result = len(s), s

        return result

    # https://leetcode.com/problems/find-the-shortest-superstring/discuss/221181/A*-search-python-implementation-64ms-pass
    def shortestSuperstring_astar(self, A: List[str]) -> str:
        def dist(v: str, w: str, eq: bool) -> int:
            if eq:
                return 10000
            else:
                for i in range(1, len(w)):
                    if v.endswith(w[:-i]):
                        return i
                return len(w)

        def construct_seq(s, d, w) -> str:
            t = w[s[0]]
            for i in range(1, len(s)):
                t = t + w[s[i]][-d[s[i - 1]][s[i]] :]
            return t

        def heuristic(x, mdj):
            return sum(mdj[i] for i in range(len(x)) if x[i] == 0)

        def adjacent_nodes(x):
            for i in range(len(x)):
                if x[i] == 0:
                    y = list(x)
                    y[i] = 1
                    yield (i, tuple(y))

        n = len(A)

        # special case
        if n == 1:
            return A[0]
        # assert n > 1

        # distance between words
        # dij := the cost in addition to add j after i
        dij = [[dist(A[i], A[j], i == j) for j in range(n)] for i in range(n)]

        # minimum cost to add j
        mdj = [min(dij[i][j] for i in range(n)) for j in range(n)]

        # A* search
        # init
        q = []  # priority queue with estimated cost
        for i in range(n):
            x = tuple(1 if j == i else 0 for j in range(n))
            g = len(A[i])  # actual cost from start
            h = heuristic(x, mdj)  # lower bound of cost till the goal
            heappush(q, (g + h, g, h, x, [i]))

        best_f = None
        best_p = None
        while len(q) > 0:
            # f, g, h, node, path
            f, g, h, x, p = heappop(q)

            if best_f is not None and f >= best_f:
                break

            for j, y in adjacent_nodes(x):
                gy = g + dij[p[-1]][j]
                py = p + [j]

                if sum(y) == n:  # is goal
                    if best_f is None or gy < best_f:
                        best_f = gy
                        best_p = py
                else:
                    hy = heuristic(y, mdj)
                    heappush(q, (gy + hy, gy, hy, y, py))

        return construct_seq(best_p, dij, A)


SolutionFunc = Callable[[List[str]], str]


def test_solution(words: List[str], expected: str) -> None:
    def test_impl(func: SolutionFunc, words: List[str], expected: str) -> None:
        r = func(words)
        if len(r) == len(expected):
            print(
                colored(
                    f"PASSED {func.__name__} => Shortest superstring of {words} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Shortest superstring of {words} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.shortestSuperstring_dp_iterative, words, expected)
    test_impl(sln.shortestSuperstring_astar, words, expected)


if __name__ == "__main__":
    test_solution(words=["alex", "loves", "leetcode"], expected="alexlovesleetcode")
    test_solution(
        words=["catg", "ctaagt", "gcta", "ttca", "atgcatc"], expected="gctaagttcatgcatc"
    )
