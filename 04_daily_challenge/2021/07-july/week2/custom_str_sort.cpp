// https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3813/

// Custom Sort String

// Solution
// order and str are strings composed of lowercase letters. In order, no letter occurs more than
// once.

// order was sorted in some custom order previously. We want to permute the characters of str so
// that they match the order that order was sorted. More specifically, if x occurs before y in
// order, then x should occur before y in the returned string.

// Return any permutation of str (as a string) that satisfies this property.

// Example:
// Input:
// order = "cba"
// str = "abcd"
// Output: "cbad"
// Explanation:
// "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
// Since "d" does not appear in order, it can be at any position in the returned string. "dcba",
// "cdba", "cbda" are also valid outputs.

// Note:

// order has length at most 26, and no character is repeated in order.
// str has length at most 200.
// order and str consist of lowercase letters only.

#include "stdafx.h"
#include <unordered_map>

using namespace std;

// Time complexity: O(N+26)
// Space complexity: O(26)
string customSortString_unorderedmap(string order, string s)
{
    unordered_map<char, int> counter;
    for (auto const chr : s) {
        counter[chr] += 1;
    }

    int i = 0;
    for (auto const chr : order) {
        if (counter.find(chr) != counter.end()) {
            auto cnt = counter[chr];
            while (cnt > 0) {
                s[i++] = chr;
                --cnt;
            }
            counter[chr] = 0;
        }
    }

    for (auto &[chr, cnt] : counter) {
        while (cnt > 0) {
            s[i++] = chr;
            --cnt;
        }
    }

    return s;
}

void test_solution(string order, string s, string expected)
{
    using SolutionFunc = function<string(string, string)>;

    auto const test_impl = [](SolutionFunc func, string_view func_name, string order, string s,
                              string expected) {
        auto const res = func(order, s);
        if (res == expected) {
            fmt::print(pass_color, "PASSED {} => Sorted string {} using order string {} is {}\n",
                       func_name, s, order, res);
        }
        else {
            fmt::print(fail_color,
                       "FAILED {} => Sorted string {} using order string {} is {} but expected\n",
                       func_name, s, order, res, expected);
        }
    };

    test_impl(customSortString_unorderedmap, "customSortString_unorderedmap", order, s, expected);
}

int main()
{
    test_solution("cba", "abcd", "cbad");

    return 0;
}