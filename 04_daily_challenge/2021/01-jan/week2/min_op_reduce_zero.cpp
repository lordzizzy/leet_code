// https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

// Minimum Operations to Reduce X to Zero

// You are given an integer array nums and an integer x. In one operation, you
// can either remove the leftmost or the rightmost element from the array nums
// and subtract its value from x. Note that this modifies the array for future
// operations.

// Return the minimum number of operations to reduce x to exactly 0 if it is
// possible, otherwise, return -1.

// Example 1:
// Input: nums = [1,1,4,2,3], x = 5
// Output: 2
// Explanation: The optimal solution is to remove the last two elements to
// reduce x to zero.

// Example 2:
// Input: nums = [5,6,7,8,9], x = 4
// Output: -1

// Example 3:
// Input: nums = [3,2,20,1,1,3], x = 10
// Output: 5
// Explanation: The optimal solution is to remove the last three elements and
// the first two elements (5 operations in total) to reduce x to zero.

// Constraints:
// 1 <= nums.length <= 10⁵
// 1 <= nums[i] <= 10⁴
// 1 <= x <= 10⁹

#include "stdafx.h"

using namespace std;
using namespace leetcode::format;

using Vec = vector<int>;

int minOperations(Vec const &nums, int x)
{
    int start = 0;
    int end = nums.size() - 1;
    int minOps = 0;

    using Func = function<void(Vec const &, int, int, int, int)>;

    Func const traverse = [&traverse, &minOps](Vec const &nums, int rem, int start, int end,
                                               int ops) {
        if (start > end) {
            return;
        }
        auto const rem_left = rem - nums[start];
        auto const rem_right = rem - nums[end];

        if (rem_left < 0 && rem_right < 0) {
            // NO solution found for this operation
            return;
        }

        ++ops;

        if (rem_left == 0) {
            minOps = (minOps > 0) ? min(minOps, ops) : ops;
            if (minOps >= nums.size()) {
                return;
            }
            // go right
            if (rem_right > 0) {
                traverse(nums, rem_right, start, end - 1, ops);
            }
        }
        else if (rem_right == 0) {
            // a solution was found on right
            minOps = (minOps > 0) ? min(minOps, ops) : ops;
            if (minOps >= nums.size()) {
                return;
            }
            // go left
            if (rem_left > 0) {
                traverse(nums, rem_left, start + 1, end, ops);
            }
        }
        else {
            if (rem_left > 0) {
                traverse(nums, rem_left, start + 1, end, ops);
            }
            if (rem_right > 0) {
                traverse(nums, rem_right, start, end - 1, ops);
            }
        }

        return;
    };

    traverse(nums, x, start, end, 0);

    return (minOps > 0) ? minOps : -1;
}

void test_solution(Vec const &nums, int x, int expected)
{
    auto const r = minOperations(nums, x);

    if (r == expected) {
        fmt::print(pass_color,
                   "PASSED minOperations => Min ops to reduce {} to zero using {} is {}\n", x,
                   to_str(nums), r);
    }
    else {
        fmt::print(
            fail_color,
            "PASSED minOperations => Min ops to reduce {} to zero using {} is {} but expected {}\n",
            x, to_str(nums), r, expected);
    }
}

int main()
{
    test_solution({1, 1, 4, 2, 3}, 5, 2);

    test_solution({5, 6, 7, 8, 9}, 4, -1);

    test_solution({3, 2, 20, 1, 1, 3}, 10, 5);

    test_solution({8828, 9581, 49, 9818, 9974, 9869, 9991, 10000, 10000, 10000, 9999, 9993, 9904,
                   8819, 1231, 6309},
                  134365, 16);

    return 0;
}