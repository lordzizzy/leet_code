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
#include <array>
#include <vector>

using namespace std;

struct Box
{
    int box_num;
    int unit_num;
};

template <> struct fmt::formatter<Box> : formatter<string_view>
{
    template <typename FormatContext> auto format(Box const &box, FormatContext &ctx)
    {
        return fmt::format_to(ctx.out(), "{{{},{}}}", box.box_num, box.unit_num);
    }
};

// Time complexity: O(N * logN), Space complexity: O(N)
int maximumUnits_simplesort(vector<Box> const &boxes, int truckSize)
{
    auto total_units = 0;
    auto sorted_boxes = vector<Box>(boxes.size());

    partial_sort_copy(begin(boxes), end(boxes), begin(sorted_boxes), end(sorted_boxes),
                      [](auto const &a, auto const &b) { return a.unit_num > b.unit_num; });

    for (auto const &[box_num, unit_num] : boxes) {
        auto const take = min(truckSize, unit_num);
        total_units += take * unit_num;
        truckSize -= box_num;
        if (truckSize == 0) {
            break;
        }
    }

    return total_units;
}

// reference:
// https://leetcode.com/problems/maximum-units-on-a-truck/discuss/1271933/C%2B%2B-16ms-Fastest-to-Date-Simple-Vs.-Bucket-Sort-Solutions-Explained-100-Time-~95-Space
//
// Time complexity: O(N), Space complexity: O(N)
int maximumUnits_bucketsort(vector<Box> const &boxes, int truckSize)
{
    auto total_units = 0;
    auto buckets = array<int, 1001>({});
    auto max_bucket = INT_MIN;
    auto min_bucket = INT_MAX;

    // bucket sort using unit num as bucket index
    for (auto const &[box_num, unit_num] : boxes) {
        max_bucket = max(max_bucket, unit_num);
        min_bucket = min(min_bucket, unit_num);
        buckets[unit_num] += box_num;
    }

    for (int i = max_bucket, size, curr_batch; i >= min_bucket; i--) {
        size = buckets[i];
        if (size == 0) {
            continue;
        }
        curr_batch = min(size, truckSize);
        truckSize -= curr_batch;
        total_units += curr_batch * i;
        if (truckSize == 0) {
            break;
        }
    }

    return total_units;
}

void test_solution(vector<Box> const &boxes, int truckSize, int expected)
{
    using SolutionFunc = function<int(vector<Box> const &, int)>;

    auto const test_impl = [](SolutionFunc func, string_view func_name, vector<Box> const &boxes,
                              int truckSize, int expected) {
        auto const r = func(boxes, truckSize);
        if (r == expected) {
            fmt::print(pass_color,
                       "PASSED {} => Max units on a truck for {{{}}} with truck size {} is {}\n",
                       func_name, fmt::join(boxes, ","), truckSize, r);
        }
        else {
            fmt::print(fail_color,
                       "FAILED {} => Max units on a truck for {{{}}} with truck size {} is {} but "
                       "expected {}\n",
                       func_name, fmt::join(boxes, ","), truckSize, r, expected);
        }
    };

    test_impl(maximumUnits_simplesort, "maximumUnits_simplesort", boxes, truckSize, expected);
    test_impl(maximumUnits_bucketsort, "maximumUnits_bucketsort", boxes, truckSize, expected);
}

int main()
{
    test_solution({{1, 3}, {2, 2}, {3, 1}}, 4, 8);
    test_solution({{5, 10}, {2, 5}, {4, 7}, {3, 9}}, 10, 91);
}
