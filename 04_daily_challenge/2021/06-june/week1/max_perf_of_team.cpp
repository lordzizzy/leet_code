// https://leetcode.com/problems/maximum-performance-of-a-team/

// Maximum Performance of a Team

// You are given two integers n and k and two integer arrays speed and
// efficiency both of length n. There are n engineers numbered from 1 to n.
// speed[i] and efficiency[i] represent the speed and efficiency of the ith
// engineer respectively.

// Choose at most k different engineers out of the n engineers to form a team
// with the maximum performance.

// The performance of a team is the sum of their engineers' speeds multiplied
// by the minimum efficiency among their engineers.

// Return the maximum performance of this team. Since the answer can be a huge
// number, return it modulo 109 + 7.

// Example 1:
// Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
// Output: 60
// Explanation:
// We have the maximum performance of the team by selecting engineer 2 (with
// speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7).
// That is, performance = (10 + 5) * min(4, 7) = 60.

// Example 2:
// Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
// Output: 68
// Explanation:
// This is the same example as the first but k = 3. We can select engineer 1,
// engineer 2 and engineer 5 to get the maximum performance of the team. That
// is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.

// Example 3:
// Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
// Output: 72

// Constraints:
// 1 <= <= k <= n <= 10⁵
// speed.length == n
// efficiency.length == n
// 1 <= speed[i] <= 10⁵
// 1 <= efficiency[i] <= 10⁸

#include "stdafx.h"
#include <queue>
#include <vector>

using namespace std;
using namespace leetcode::format;

int maxPerformance_greedy_priorityQ(int const n, vector<int> const &speeds,
                                    vector<int> const &efficiencies, int const k)
{
    vector<pair<int, int>> candidates(n);
    for (int i = 0; i < n; i++) {
        candidates[i] = {efficiencies[i], speeds[i]};
    }
    sort(candidates.rbegin(), candidates.rend());

    auto speed_sum = 0, perf = 0;
    priority_queue<int, vector<int>, greater<int>> min_heap;

    for (auto const &[eff, spd] : candidates) {
        min_heap.emplace(spd);
        speed_sum += spd;
        if (min_heap.size() > k) {
            speed_sum -= min_heap.top();
            min_heap.pop();
        }
        perf = max(perf, speed_sum * eff);
    }

    return perf % int(1e9 + 7);
}

void test_solution(int n, vector<int> const &speeds, vector<int> const &efficiencies, int k,
                   int expected)
{
    using SolutionFunc = std::function<int(int, vector<int> const &, vector<int> const &, int)>;

    auto test_impl = [](SolutionFunc func, string_view func_name, int n, vector<int> const &speeds,
                        vector<int> const &efficiencies, int k, int expected) {
        auto const r = func(n, speeds, efficiencies, k);
        if (r == expected) {
            fmt::print(pass_color,
                       "PASSED {} => Max performance of chosen {} of team with size {}, speeds: "
                       "{} and efficiencies: {} is {}.\n",
                       func_name, k, n, to_str(speeds), to_str(efficiencies), r);
        }
        else {
            fmt::print(fail_color,
                       "FAILED {} => Max performance of chosen {} of team with size {}, speeds: "
                       "{} and efficiencies: {} is {} but expected {}.\n",
                       func_name, k, n, to_str(speeds), to_str(efficiencies), r, expected);
        }
    };

    test_impl(maxPerformance_greedy_priorityQ, "maxPerformance_greedy_priorityQ", n, speeds,
              efficiencies, k, expected);
}

int main()
{
    test_solution(6, {2, 10, 3, 1, 5, 8}, {5, 4, 3, 9, 7, 2}, 2, 60);
    test_solution(6, {2, 10, 3, 1, 5, 8}, {5, 4, 3, 9, 7, 2}, 3, 68);
    test_solution(6, {2, 10, 3, 1, 5, 8}, {5, 4, 3, 9, 7, 2}, 4, 72);

    return 0;
}
