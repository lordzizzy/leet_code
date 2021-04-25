# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3719/

# Critical Connections in a Network

# There are n servers numbered from 0 to n-1 connected by undirected
# server-to-server connections forming a network where connections[i] = [a, b]
# represents a connection between servers a and b. Any server can reach any
# other server directly or indirectly through the network.

# A critical connection is a connection that, if removed, will make some server
# unable to reach some other server.

# Return all critical connections in the network in any order.


# Example 1:
# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.


# Constraints:
# 1 <= n <= 10⁵
# n-1 <= connections.length <= 10⁵
# connections[i][0] != connections[i][1]
# There are no repeated connections.

from typing import Callable, DefaultDict, List
from termcolor import colored

Edge = List[int]


class Solution:
    def criticalConnections(self, n: int, connections: List[Edge]) -> List[Edge]:
        return self.criticalConnections_tarjan(n, connections)

    def criticalConnections_tarjan(self, N: int, connections: List[Edge]) -> List[Edge]:
        graph = DefaultDict[int, List[int]](lambda: [])
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        NULL = -2 # did this to avoid fighting with type system for Optional's None checks

        lev = [NULL] * N
        low = [NULL] * N

        def dfs(node: int, par: int, level: int) -> None:
            # already visited
            if lev[node] != NULL:
                return

            lev[node] = low[node] = level
            for nei in graph[node]:
                if lev[nei] == NULL:
                    dfs(nei, node, level + 1)

            # minimal level in the neighbors, exclude the parent
            low[node] = min([level] + [low[nei] for nei in graph[node] if nei != par])

        dfs(node=0, par=NULL, level=0)

        res: List[List[int]] = []
        for u, v in connections:
            if low[u] > lev[v] or low[v] > lev[u]:
                res.append([u, v])
        return res


SolutionFunc = Callable[[int, List[Edge]], List[Edge]]


def test_solution(n: int, connections: List[Edge], expected: List[Edge]) -> None:
    def test_impl(
        func: SolutionFunc,
        n: int,
        connections: List[Edge],
        expected: List[Edge],
    ) -> None:
        r = func(n, connections)
        if sorted(r) == sorted(expected):
            print(
                colored(
                    f"PASSED {func.__name__} => Critical connections in {connections} with {n} servers are {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Critical connections in {connections} with {n} servers are {r}, but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.criticalConnections, n, connections, expected)


if __name__ == "__main__":
    test_solution(n=4, connections=[[0, 1], [1, 2], [2, 0], [1, 3]], expected=[[1, 3]])
