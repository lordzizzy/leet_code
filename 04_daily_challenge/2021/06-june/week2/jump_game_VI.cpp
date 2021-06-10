// https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3773/

// Jump Game VI

// You are given a 0-indexed integer array nums and an integer k.

// You are initially standing at index 0. In one move, you can jump at most k
// steps forward without going outside the boundaries of the array. That is, you
// can jump from index i to any index in the range [i + 1, min(n - 1, i + k)]
// inclusive.

// You want to reach the last index of the array (index n - 1). Your score is
// the sum of all nums[j] for each index j you visited in the array.

// Return the maximum score you can get.

// Example 1:
// Input: nums = [1,-1,-2,4,-7,3], k = 2
// Output: 7
// Explanation: You can choose your jumps forming the subsequence [1,-1,4,3]
// (underlined above). The sum is 7.

// Example 2:
// Input: nums = [10,-5,-2,4,0,3], k = 3
// Output: 17
// Explanation: You can choose your jumps forming the subsequence [10,4,3]
// (underlined above). The sum is 17.

// Example 3:
// Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
// Output: 0

// Constraints:
// 1 <= nums.length, k <= 10⁵
// -10⁴ <= nums[i] <= 10⁴

//  references and ideas from
//  https://leetcode.com/problems/jump-game-vi/discuss/978497/Python-DP-%2B-Sliding-Window-Maximum-problem-combined

#include "stdafx.h"
#include <deque>
#include <vector>

using namespace std;
using namespace leetcode::format;

using Vec = vector<int>;
using Deq = deque<int>;

int maxResult_dp_monoqueue(Vec const &nums, int k)
{
    auto const N = nums.size();
    auto deq = Deq({0});
    auto dp = Vec(N, 0);
    dp[0] = nums[0];

    for (int i = 1; i < N; i++) {
        dp[i] = nums[i] + dp[deq.front()];

        while (deq.size() && dp[deq.back()] < dp[i]) {
            deq.pop_back();
        }

        deq.emplace_back(i);

        if (deq.front() == i - k) {
            deq.pop_front();
        }
    }

    return dp.back();
}

void test_solution(Vec const &nums, int k, int expected)
{
    using SolutionFunc = function<int(Vec const &, int)>;

    auto const test_impl = [](SolutionFunc func, string_view func_name, Vec const &nums, int k,
                              int expected) {
        auto const r = func(nums, k);
        if (r == expected) {
            fmt::print(pass_color, "PASSED {} => Max score from {} with {} steps is {}\n",
                       func_name, to_str(nums), k, r);
        }
        else {
            fmt::print(fail_color,
                       "FAILED {} => Max score from {} with {} steps is {} but expected {}\n",
                       func_name, to_str(nums), k, r, expected);
        }
    };

    test_impl(maxResult_dp_monoqueue, "maxResult_dp_monoqueue", nums, k, expected);
}

int main()
{
    test_solution({10, -5, -2, 4, 0, 3}, 3, 17);
    test_solution({1, -1, -2, 4, -7, 3}, 2, 7);
    test_solution({1, -5, -20, 4, -1, 3, -6, -3}, 2, 0);

    return 0;
}