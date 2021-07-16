// https://leetcode.com/problems/valid-triangle-number/solution/

// 611. Valid Triangle Number

// Given an integer array nums, return the number of triplets chosen from the
// array that can make triangles if we take them as side lengths of a triangle.

// Example 1:
// Input: nums = [2,2,3,4]
// Output: 3
// Explanation: Valid combinations are:
// 2,3,4 (using the first 2)
// 2,3,4 (using the second 2)
// 2,2,3

// Example 2:
// Input: nums = [4,2,3,4]
// Output: 4

// Constraints:

// 1 <= nums.length <= 1000
// 0 <= nums[i] <= 1000

#include "stdafx.h"

using namespace std;

int triangleNumber_bruteforce(vector<int> const &nums)
{
    auto const N = nums.size();
    int count = 0;

    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j < N; ++j) {
            for (int k = j + 1; k < N; ++k) {
                if (nums[i] + nums[j] > nums[k] && nums[i] + nums[k] > nums[j] &&
                    nums[j] + nums[k] > nums[i]) {
                    ++count;
                }
            }
        }
    }

    return count;
}

int triangleNumber_sort_and_2ptrs(vector<int> const &nums)
{
    auto sorted_nums = vector<int>(nums);
    sort(begin(sorted_nums), end(sorted_nums));

    int count = 0;

    // given sides (a,b,c) for triangle
    for (int c = 2; c < sorted_nums.size(); ++c) {
        int a = 0, b = c - 1;

        while (a < b) {
            if (sorted_nums[a] + sorted_nums[b] > sorted_nums[c]) {
                count += b - a;
                b -= 1;
            }
            else {
                a += 1;
            }
        }
    }

    return count;
}

void test_solution(vector<int> const &nums, int expected)
{
    using SolutionFunc = function<int(vector<int> const &)>;

    auto const test_impl = [](SolutionFunc func, string_view func_name, vector<int> const &nums,
                              int expected) {
        auto const res = func(nums);
        if (res == expected) {
            fmt::print(pass_color,
                       "PASSED {} => Number of triplets that make a triangle in {} is {}\n",
                       func_name, fmt::join(nums, ","), res);
        }
        else {
            fmt::print(fail_color,
                       "FAILED {} => Number of triplets that make a triangle in {} is {} "
                       "but expected {}\n",
                       func_name, fmt::join(nums, ","), res, expected);
        }
    };

    test_impl(triangleNumber_bruteforce, "triangleNumber_bruteforce", nums, expected);
    test_impl(triangleNumber_sort_and_2ptrs, "triangleNumber_sort_and_2ptrs", nums, expected);
}

int main()
{
    test_solution({2, 2, 3, 4}, 3);
    test_solution({4, 2, 3, 4}, 4);

    return 0;
}
