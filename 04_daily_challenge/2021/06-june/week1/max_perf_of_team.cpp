#include <iostream>
#include <sstream>
#include <format>
#include <vector>
#include <functional>
#include <queue>

using namespace std;

int maxPerformance_greedy_priorityQ(const int n, vector<int> const &speeds, vector<int> const &efficiencies, const int k)
{
    vector<pair<int, int>> candidates(n);
    for (int i = 0; i < n; i++)
    {
        candidates[i] = {efficiencies[i], speeds[i]};
    }
    sort(candidates.rbegin(), candidates.rend());

    auto speed_sum = 0, perf = 0;
    priority_queue<int, vector<int>, greater<int>> min_heap;

    for (auto const &[eff, spd] : candidates)
    {
        min_heap.emplace(spd);
        speed_sum += spd;
        if (min_heap.size() > k)
        {
            speed_sum -= min_heap.top();
            min_heap.pop();
        }
        perf = max(perf, speed_sum * eff);
    }

    return perf % int(1e9 + 7);
}

using SolutionFunc = std::function<int(int, vector<int> const &, vector<int> const &, int)>;

SolutionFunc f = maxPerformance_greedy_priorityQ;

constexpr auto to_str = [](vector<int> const &vec)
{
    stringstream ss;

    for (size_t i = 0; i < vec.size(); i++)
    {
        if (i != 0)
        {
            ss << ",";
        }
        ss << vec[i];
    }

    return ss.str();
};

void test_solution(int n, vector<int> const &speeds, vector<int> const &efficiencies, int k, int expected)
{
    auto test_impl = [](SolutionFunc func, int n, vector<int> const &speeds, vector<int> const &efficiencies, int k, int expected)
    {
        auto r = func(n, speeds, efficiencies, k);
        if (r == expected)
        {
            cout << format("PASSED => Max performance of chosen {} of team with size {}, speeds: {} and efficiencies: {} is {}.\n", k, n, to_str(speeds), to_str(efficiencies), r);
        }
        else
        {
            cout << format("FAILED => Max performance of chosen {} of team with size {}, speeds: {} and efficiencies: {} is {} but expected {}.\n", k, n, to_str(speeds), to_str(efficiencies), r, expected);
        }
        cout << endl;
    };

    test_impl(maxPerformance_greedy_priorityQ, n, speeds, efficiencies, k, expected);
}

int main()
{
    test_solution(
        6, {2, 10, 3, 1, 5, 8}, {5, 4, 3, 9, 7, 2}, 2, 60);

    test_solution(
        6, {2, 10, 3, 1, 5, 8}, {5, 4, 3, 9, 7, 2}, 3, 68);

    test_solution(
        6, {2, 10, 3, 1, 5, 8}, {5, 4, 3, 9, 7, 2}, 4, 72);

    return 0;
}
