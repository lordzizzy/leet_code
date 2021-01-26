# https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/828/

# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

from typing import List
from termcolor import colored


class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # return self.spiralOrder_simulation(matrix)
        return self.spiralOrder_layer(matrix)

    def spiralOrder_simulation(self, matrix: List[List[int]]) -> List[int]:
        """
        Approach 1: Simulation
        Intuition

        Draw the path that the spiral makes. We know that the path should turn clockwise whenever it would go out of bounds or into a cell that was previously visited.

        Algorithm

        Let the array have R rows and C columns. seen[r][c] denotes that the cell on the r-th row and c-th column was previously visited. Our current position is (r, c), facing direction di, and we want to visit RxC total cells.

        As we move through the matrix, our candidate next position is (cr, cc). If the candidate is in the bounds of the matrix and unseen, then it becomes our next position; otherwise, our next position is the one after performing a clockwise turn.

        Complexity Analysis
        Time Complexity: O(N), where N is the total number of elements in the input matrix. We add every element in the matrix to our final answer.

        Space Complexity: O(N), the information stored in seen and in ans.
        """
        if not matrix:
            return []

        R = len(matrix)
        C = len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0

        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]

        return ans

    def spiralOrder_layer(self, matrix: List[List[int]]) -> List[int]:
        """
        Approach 2: Layer-by-Layer
        Intuition

        The answer will be all the elements in clockwise order from the first-outer layer, followed by the elements from the second-outer layer, and so on.

        Algorithm

        We define the k-th outer layer of a matrix as all elements that have minimum distance to some border equal to k. For example, the following matrix has all elements in the first-outer layer equal to 1, all elements in the second-outer layer equal to 2, and all elements in the third-outer layer equal to 3.

        [[1, 1, 1, 1, 1, 1, 1],
        [1, 2, 2, 2, 2, 2, 1],
        [1, 2, 3, 3, 3, 2, 1],
        [1, 2, 2, 2, 2, 2, 1],
        [1, 1, 1, 1, 1, 1, 1]]

        For each outer layer, we want to iterate through its elements in clockwise order starting from the top left corner. Suppose the current outer layer has top-left coordinates (r1, c1) and bottom-right coordinates (r2, c2).

        Then, the top row is the set of elements (r1, c) for c = c1,...,c2, in that order. The rest of the right side is the set of elements (r, c2) for r = r1+1,...,r2, in that order. Then, if there are four sides to this layer (ie., r1 < r2 and c1 < c2), we iterate through the bottom side and left side as shown in the solutions below.

        Complexity Analysis
        Time Complexity: O(N), where N is the total number of elements in the input matrix. We add every element in the matrix to our final answer.

        Space Complexity:
        O(1) without considering the output array, since we don't use any additional data structures for our computations.
        O(N) if the output array is taken into account.
        """
        def spiralOrder(r1, c1, r2, c2):
            for c in range(c1, c2+1):
                yield r1, c
            for r in range(r1+1, r2+1):
                yield r, c2
            if r1 < r2 and c1 < c2:
                for c in range(c2-1, c1, -1):
                    yield r2, c
                for r in range(r2, r1, -1):
                    yield r, c1

        if not matrix:
            return []

        ans = []
        r1, r2 = 0, len(matrix)-1
        c1, c2 = 0, len(matrix[0])-1

        while r1 <= r2 and c1 <= c2:
            for r, c in spiralOrder(r1, c1, r2, c2):
                ans.append(matrix[r][c])
            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1

        return ans


def test_solution(matrix: List[List[int]], expected: List[int]):
    sln = Solution()
    r = sln.spiralOrder(matrix)
    if r == expected:
        print(colored(f"PASSED - {matrix} in spiral order is {r}", "green"))
    else:
        print(colored(
            f"FAILED - {matrix} in spiral order is {r}, but expected: {expected}", "red"))


if __name__ == "__main__":

    test_solution(matrix=[[1,2],[3, 4]], expected=[1,2,4,3])

    test_solution(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], expected=[
                  1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
