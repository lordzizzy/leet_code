# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/606/week-4-june-22nd-june-28th/3791/

# Redundant Connection
# In this problem, a tree is an undirected graph that is connected and has no
# cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to
# n, with one additional edge added. The added edge has two different vertices
# chosen from 1 to n, and was not an edge that already existed. The graph is
# represented as an array edges of length n where edges[i] = [ai, bi] indicates
# that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n
# nodes. If there are multiple answers, return the answer that occurs last in
# the input.

# Example 1:
# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]

# Example 2:
# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]

# Constraints:
# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ai < bi <= edges.length
# ai != bi
# There are no repeated edges.
# The given graph is connected.

from collections import defaultdict
from typing import Callable, DefaultDict, List, Set

from termcolor import colored


class Solution:
    # for each edge (u, v), traverse the graph with a depth-first search to see
    # if we can connect u to v. If we can, then it must be duplicate edge
    #
    # Time complexity:  O(N^2)
    # Space complexity: O(N)
    def findRedundantConnection_dfs_recursive(
        self, edges: List[List[int]]
    ) -> List[int]:
        def dfs(source: int, target: int) -> bool:
            if source not in seen:
                seen.add(source)
                if source == target:
                    return True
                return any(dfs(nei, target) for nei in graph[source])
            else:
                return False

        graph: DefaultDict[int, Set[int]] = defaultdict(set)

        for u, v in edges:
            seen: Set[int] = set()
            if u in graph and v in graph and dfs(u, v):
                return [u, v]
            graph[u].add(v)
            graph[v].add(u)

        return []

    # TODO: iterative version of dfs


SolutionFunc = Callable[[List[List[int]]], List[int]]


def test_solution(edges: List[List[int]], expected: List[int]) -> None:
    def test_impl(
        func: SolutionFunc, edges: List[List[int]], expected: List[int]
    ) -> None:
        r = func(edges)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Redundant connections in {edges} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Redundant connections in {edges} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.findRedundantConnection_dfs_recursive, edges, expected)


if __name__ == "__main__":
    test_solution(edges=[[1, 2], [1, 3], [2, 3]], expected=[2, 3])
    test_solution(edges=[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], expected=[1, 4])
