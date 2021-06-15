# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3778/

# Maximum Units on a Truck
# You are assigned to put some amount of boxes onto one truck. You are given a
# 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi,
# numberOfUnitsPerBoxi]:

# numberOfBoxesi is the number of boxes of type i.
# numberOfUnitsPerBoxi is the number of units in each box of the type i.

# You are also given an integer truckSize, which is the maximum number of boxes
# that can be put on the truck. You can choose any boxes to put on the truck as
# long as the number of boxes does not exceed truckSize.

# Return the maximum total number of units that can be put on the truck.

# Example 1:
# Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
# Output: 8
# Explanation: There are:
# - 1 box of the first type that contains 3 units.
# - 2 boxes of the second type that contain 2 units each.
# - 3 boxes of the third type that contain 1 unit each.
# You can take all the boxes of the first and second types, and one box of
# the third type.
# The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.

# Example 2:
# Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
# Output: 91

# Constraints:
# 1 <= boxTypes.length <= 1000
# 1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
# 1 <= truckSize <= 10⁶

from typing import Callable, List
from termcolor import colored


class Solution:
    # Time complexity: O(N logN), Space complexity: O(N)
    def maximumUnits_simplesort(self, boxTypes: List[List[int]], truckSize: int) -> int:
        total_units = 0
        sorted_boxes = sorted(boxTypes, key=lambda b: b[1], reverse=True)

        for box_cnt, unit_cnt in sorted_boxes:
            take = min(truckSize, box_cnt)
            total_units += take * unit_cnt
            truckSize -= take
            if truckSize == 0:
                break

        return total_units


SolutionFunc = Callable[[List[List[int]], int], int]


def test_solution(boxTypes: List[List[int]], truckSize: int, expected: int) -> None:
    def test_impl(
        func: SolutionFunc, boxTypes: List[List[int]], truckSize: int, expected: int
    ) -> None:
        r = func(boxTypes, truckSize)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Max units on truck from {boxTypes} with truck size {truckSize} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Max units on truck from {boxTypes} with truck size {truckSize} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.maximumUnits_simplesort, boxTypes, truckSize, expected)


if __name__ == "__main__":
    test_solution(boxTypes=[[1, 3], [2, 2], [3, 1]], truckSize=4, expected=8)
    test_solution(boxTypes=[[5, 10], [2, 5], [4, 7], [3, 9]], truckSize=10, expected=91)
