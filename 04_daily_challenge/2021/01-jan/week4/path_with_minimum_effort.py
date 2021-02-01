# https://leetcode.com/explore/featured/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3617/

# Path With Minimum Effort
# You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

# Example 1:
# Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
# Output: 2
# Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
# This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

# Example 2:
# Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
# Output: 1
# Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].

# Example 3:
# Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# Output: 0
# Explanation: This route does not require any effort.

# Constraints:
# rows == heights.length
# columns == heights[i].length
# 1 <= rows, columns <= 100
# 1 <= heights[i][j] <= 10^6

from typing import List
from termcolor import colored
from collections import defaultdict

import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        return self.minimumEffortPath_dijkstra_heap(heights)
        # return self.minimumEffortPath_dfs_with_binary_search(heights)

    def minimumEffortPath_dijkstra_heap(self, heights: List[List[int]]) -> int:
        R = len(heights)
        C = len(heights[0])
        efforts = defaultdict(lambda: 1e6)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = []
        # push goal into q
        heapq.heappush(q, (0, R-1, C-1))

        # start from goal, find way back to origin
        while q:
            value, r, c = heapq.heappop(q)
            if (r, c) == (0, 0):
                return value

            visited = set()
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < R and 0 <= nc < C and (nr, nc):
                    e = max(value, abs(heights[nr][nc] - heights[r][c]))
                    if e < efforts[(nr, nc)]:
                        efforts[(nr, nc)] = e
                        heapq.heappush(q, (e, nr, nc))

        return -1

    def minimumEffortPath_dfs_with_binary_search(self, heights: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/path-with-minimum-effort/discuss/1035940/Python-dfs-with-binary-search-explained
        """
        R = len(heights)
        C = len(heights[0])
        goal = (R-1, C-1)
        neigbours = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visited: set = None

        def dfs(limit: int, r: int, c: int):
            visited.add((r, c))
            for dr, dc in neigbours:
                nr = r+dr
                nc = c+dc
                if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited:
                    if abs(heights[r][c] - heights[nr][nc]) <= limit:
                        dfs(limit, nr, nc)

        begin = -1
        end = max(max(heights, key=max))

        # binary search
        while begin+1 < end:
            mid = (begin + end) // 2
            visited = set()
            dfs(mid, 0, 0)
            if goal in visited:
                end = mid
            else:
                begin = mid

        return end


def test_solution(heights: List[List[int]], expected: int):
    sln = Solution()
    r = sln.minimumEffortPath(heights)
    if r == expected:
        print(colored(f"PASSED - {heights} minimum effort is {r}", "green"))
    else:
        print(colored(
            f"FAILED - {heights} minimum effort is {r}, but expected: {expected}", "red"))


if __name__ == "__main__":
    test_solution(heights=[[1, 2], [3, 8], [5, 3]], expected=2)
    test_solution(heights=[[1, 2, 2], [3, 8, 2], [5, 3, 5]], expected=2)
    test_solution(heights=[[1, 2, 3], [3, 8, 4], [5, 3, 5]], expected=1)
    test_solution(heights=[[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [
                  1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]], expected=0)
    test_solution(heights=[[8, 6, 8, 1, 4, 1], [10, 3, 1, 8, 9, 10],
                           [1, 5, 6, 9, 8, 5], [10, 4, 6, 7, 3, 3],
                           [6, 6, 9, 1, 3, 3], [3, 1, 10, 3, 4, 1],
                           [6, 1, 6, 10, 7, 10]], expected=3)
