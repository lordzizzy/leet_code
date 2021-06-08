// #
// https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/603/week-1-june-1st-june-7th/3770/

// # Min Cost Climbing Stairs
// # You are given an integer array cost where cost[i] is the cost of ith step on
// # a staircase. Once you pay the cost, you can either climb one or two steps.

// # You can either start from the step with index 0, or the step with index 1.

// # Return the minimum cost to reach the top of the floor.

// # Example 1:
// # Input: cost = [10,15,20]
// # Output: 15
// # Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.

// # Example 2:
// # Input: cost = [1,100,1,1,1,100,1,1,100,1]
// # Output: 6
// # Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping
// # cost[3].

// # Constraints:
// # 2 <= cost.length <= 1000
// # 0 <= cost[i] <= 999

// REALLY good reference on dynamic programming here
// https://leetcode.com/problems/min-cost-climbing-stairs/discuss/110111/The-ART-of-dynamic-programming

#include "stdafx.h"
#include <vector>

using namespace std;
using namespace leetcode::format;

using Vec = vector<int>;

int mainCostClimbingStairs_dfs_bruteforce(Vec const &costs)
{
    using Func = function<int(int)>;

    Func const get_cost = [&](size_t step) {
        if (step >= costs.size()) {
            return 0;
        }
        return costs[step] + min(get_cost(step + 1), get_cost(step + 2));
    };

    return min(get_cost(0), get_cost(1));
}

int minCostClimbingStairs_dp_topdown_with_memoization(Vec const &costs)
{
    auto constexpr sentinel = -1;
    auto const N = costs.size();
    auto dp = Vec(N, sentinel);

    using Func = function<int(int)>;

    Func const get_cost = [&](size_t step) {
        if (step >= N) {
            return 0;
        }
        if (dp[step] != sentinel) {
            return dp[step];
        }
        return dp[step] = costs[step] + min(get_cost(step + 1), get_cost(step + 2));
    };

    return min(get_cost(0), get_cost(1));
}

int minCostClimbingStairs_dp_bottomup(Vec const &costs)
{
    auto const N = costs.size();
    auto dp = Vec(N + 1, 0);

    for (auto i = 2; i < N + 1; i++) {
        dp[i] = min(dp[i - 1] + costs[i - 1], dp[i - 2] + costs[i - 2]);
    }

    return dp[N];
}

// fastest, constant space, only care about n-1 and n-2 steps at step n =>
// only 2 variables needed, + 1 to store result from callstack c = cost[i] + min(a,b)
int minCostClimbingStairs_dp_bottomup_optimized(Vec const &costs)
{
    auto const N = costs.size();
    auto a = 0, b = 0, c = 0;

    for (int i = N - 1; i >= 0; --i) {
        c = costs[i] + min(a, b);
        a = b, b = c;
    }

    return min(a, b);
}

void test_solution(Vec const &costs, int expected)
{
    using SolutionFunc = function<int(Vec const &)>;

    auto const test_impl = [](SolutionFunc func, string_view func_name, Vec const &costs,
                              int expected) {
        auto const r = func(costs);
        if (r == expected) {
            cout << format("PASSED {} => Min cost to reach top floor with costs {} is {}\n",
                           func_name, to_str(costs), r);
        }
        else {
            cout << format(
                "FAILED {} => Min cost to reach top floor with costs {} is {} but expected {}\n",
                func_name, to_str(costs), r, expected);
        }
        cout << endl;
    };

    test_impl(mainCostClimbingStairs_dfs_bruteforce, "mainCostClimbingStairs_dfs_bruteforce", costs,
              expected);

    test_impl(minCostClimbingStairs_dp_topdown_with_memoization,
              "minCostClimbingStairs_dp_topdown_with_memoization", costs, expected);

    test_impl(minCostClimbingStairs_dp_bottomup, "minCostClimbingStairs_dp_bottomup", costs,
              expected);

    test_impl(minCostClimbingStairs_dp_bottomup_optimized,
              "minCostClimbingStairs_dp_bottomup_optimized", costs, expected);
}

int main()
{
    test_solution({10, 15, 20}, 15);
    test_solution({1, 100, 1, 1, 1, 100, 1, 1, 100, 1}, 6);
}