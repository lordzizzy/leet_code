#include "stdafx.h"
#include <unordered_set>
#include <vector>

using namespace std;
using namespace leetcode::format;

using Vec = std::vector<int>;

int longestConsecutive_set(Vec const &nums)
{
    if (nums.size() == 0) {
        return 0;
    }
    auto s = unordered_set(nums.begin(), nums.end());
    auto longest = 0;
    for (auto const num : nums) {
        if (s.find(num - 1) == s.end()) {
            auto next = num + 1;
            while (s.find(next) != s.end()) {
                next += 1;
            }
            longest = max(longest, next - num);
        }
    }
    return longest;
}

void test_solution(Vec const &nums, int const expected)
{
    using SolutionFunc = std::function<int(Vec const &)>;

    auto constexpr test_impl = [](SolutionFunc func, string_view func_name, Vec const &nums,
                                  int const expected) {
        auto const r = func(nums);
        if (r == expected) {
            fmt::print(pass_color, "PASSED {} => Longest consecutive sequence in {} is {}\n",
                       func_name, to_str(nums), r);
        }
        else {
            fmt::print(fail_color,
                       "FAILED {} => Longest consecutive sequence in {} is {} but expected {}\n",
                       func_name, to_str(nums), r, expected);
        }
    };

    test_impl(longestConsecutive_set, "longestConsecutive_set", nums, expected);
}

int main()
{
    test_solution({100, 4, 200, 1, 3, 2}, 4);
    test_solution({0, 3, 7, 2, 5, 8, 4, 6, 0, 1}, 9);

    return 0;
}
