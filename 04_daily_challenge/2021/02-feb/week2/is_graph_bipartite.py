# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3639/

# Is Graph Bipartite?
# Given an undirected graph, return true if and only if it is bipartite.

# Recall that a graph is bipartite if we can split its set of nodes into two
# independent subsets A and B, such  that every edge in the graph has one node
# in A and another node in B.

# The graph is given in the following form: graph[i] is a list of indexes j
# for which the edge between nodes i and j exists. Each node is an integer
# between 0 and graph.length - 1. There are no self edges or parallel edges:
# graph[i] does not contain i, and it doesn't contain any element twice.


# Example 1:
# Input: graph = [[1,3],[0,2],[1,3],[0,2]]
# Output: true
# Explanation: We can divide the vertices into two groups: {0, 2} and {1, 3}.

# Example 2:
# Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# Output: false
# Explanation: We cannot find a way to divide the set of nodes into two
# independent subsets.

# Constraints:
# 1 <= graph.length <= 100
# 0 <= graph[i].length < 100
# 0 <= graph[i][j] <= graph.length - 1
# graph[i][j] != i
# All the values of graph[i] are unique.
# The graph is guaranteed to be undirected.

# https://leetcode.com/problems/is-graph-bipartite/discuss/115493/Python-7-lines-DFS-graph-coloring-w-graph-and-Explanation

# https://leetcode.com/problems/is-graph-bipartite/discuss/119514/Python-3-BFS-DFS-solutions

from typing import Callable, DefaultDict, Deque, List
from termcolor import colored


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        return self.isBipartite_dfs_recursive(graph)

    def isBipartite_dfs_recursive(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = DefaultDict[int, int](
            lambda: 0
        )  # should have only 2 colors, 0 and 1 in values

        def dfs(node_i: int, color: int):
            if node_i in colors:
                return colors[node_i] == color
            colors[node_i] = color
            for nb in graph[node_i]:
                if not dfs(nb, 1 - color):
                    return False
            return True

        for node_i in range(n):
            if node_i not in colors:
                if not dfs(node_i, 0):
                    return False

        return True

    def isBipartite_bfs_iterative(self, graph: List[List[int]]) -> bool:
        colors = DefaultDict[int, int](lambda: 0)
        for i, neigbours in enumerate(graph):
            if i in colors:
                continue
            q = Deque([i])
            colors[i] = 1
            while q:
                node = q.popleft()
                for nb in neigbours:
                    if nb in colors:
                        if colors[nb] == colors[node]:
                            return False
                    else:
                        colors[nb] = 1 - colors[node]
                        q.append(nb)

        return True


SolutionFunc = Callable[[List[List[int]]], bool]


def test_solution(graph: List[List[int]], expected: bool) -> None:
    def test_impl(func: SolutionFunc, graph: List[List[int]], expected: bool) -> None:
        r = func(graph)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => {graph} is bi-partite = {r}", "green"
                )
            )
        else:
            print(
                colored(
                    f"PASSED {func.__name__} => {graph} is bi-partite = {r}, but expected: {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.isBipartite_dfs_recursive, graph, expected)


if __name__ == "__main__":
    test_solution(graph=[[1, 3], [0, 2], [1, 3], [0, 2]], expected=True)
    test_solution(graph=[[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]], expected=False)
