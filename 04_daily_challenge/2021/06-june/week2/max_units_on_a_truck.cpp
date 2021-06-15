/*
#
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3778/

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
*/

#include "stdafx.h"
#include <algorithm>
#include <vector>

using namespace std;
using namespace leetcode::format;

// Time complexity: O(N * logN), Space complexity: O(N)
int maximumUnits_simplesort(vector<vector<int>> const &boxes, int truckSize)
{
    auto total_units = 0;
    auto sorted_boxes = vector<vector<int>>(boxes.size());

    partial_sort_copy(begin(boxes), end(boxes), begin(sorted_boxes), end(sorted_boxes),
                      [](auto const &a, auto const &b) { return a[1] > b[1]; });

    for (auto &box : boxes) {
        auto const take = min(truckSize, box[0]);
        total_units += take * box[1];
        truckSize -= box[0];
        if (truckSize == 0) {
            break;
        }
    }

    return total_units;
}

void test_solution(vector<vector<int>> const &boxes, int truckSize, int expected)
{
    using SolutionFunc = function<int(vector<vector<int>> const &, int)>;

    auto const test_impl = [](SolutionFunc func, string_view func_name,
                              vector<vector<int>> const &boxes, int truckSize, int expected) {
        auto const r = func(boxes, truckSize);
        if (r == expected) {
            fmt::print(pass_color,
                       "PASSED {} => Max units on a truck for {} with truck size {} is {}\n",
                       func_name, to_str(boxes[0]), truckSize, r);
        }
        else {
            fmt::print(fail_color,
                       "FAILED {} => Max units on a truck for {} with truck size {} is {} but "
                       "expected {}\n",
                       func_name, to_str(boxes[0]), truckSize, r, expected);
        }
    };

    test_impl(maximumUnits_simplesort, "maximumUnits_simplesort", boxes, truckSize, expected);
}

int main()
{
    test_solution({{1, 3}, {2, 2}, {3, 1}}, 4, 8);
    test_solution({{5, 10}, {2, 5}, {4, 7}, {3, 9}}, 10, 91);
}
