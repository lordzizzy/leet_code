// https://leetcode.com/problems/reduce-array-size-to-the-half/

// 1338. Reduce Array Size to The Half

// Given an array arr.  You can choose a set of integers and remove all the
// occurrences of these integers in the array.

// Return the minimum size of the set so that at least half of the integers of
// the array are removed.

// Example 1:
// Input: arr = [3,3,3,3,5,5,5,2,2,7]
// Output: 2
// Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has
// size 5 (i.e equal to half of the size of the old array).

// Possible sets of size 2 are {3,5},{3,2},{5,2}.
// Choosing set {2,7} is not possible as it will make the new array
// [3,3,3,3,5,5,5] which has size greater than half of the size of the old
// array.

// Example 2:
// Input: arr = [7,7,7,7,7,7]
// Output: 1
// Explanation: The only possible set you can choose is {7}. This will make the
// new array empty.

// Example 3:
// Input: arr = [1,9]
// Output: 1

// Example 4:
// Input: arr = [1000,1000,3,7]
// Output: 1

// Example 5:
// Input: arr = [1,2,3,4,5,6,7,8,9,10]
// Output: 5

// Constraints:

// 1 <= arr.length <= 10^5
// arr.length is even.
// 1 <= arr[i] <= 10^5

// reference
// https://leetcode.com/problems/reduce-array-size-to-the-half/discuss/1319416/C%2B%2BJavaPython-HashMap-and-Sort-then-Counting-Sort-O(N)-Clean-and-Concise

#include "stdafx.h"
#include <unordered_map>
#include <vector>

using namespace std;

// Time complexity: O(N logN)
// Space complexity: O(N)
int minSetSize_unorderedmap_and_sort(vector<int> const &arr)
{
    auto const N = arr.size();
    unordered_map<int, int> cnt_map;
    for (auto x : arr) {
        ++cnt_map[x];
    }

    vector<int> freqs;
    for (auto const &[_, f] : cnt_map) {
        freqs.emplace_back(f);
    }
    sort(rbegin(freqs), rend(freqs));

    int half = N / 2;
    int ans = 0;
    for (auto const f : freqs) {
        half -= f;
        ans += 1;
        if (half <= 0) {
            break;
        }
    }

    return ans;
}

// Time complexity: O(N)
// Space complexity: O(N)
int minSetSize_unorderedmap_and_countingsort(vector<int> const &arr)
{
    auto const N = arr.size();
    unordered_map<int, int> cnt_map;
    for (auto x : arr) {
        ++cnt_map[x];
    }

    vector<int> counting(N + 1);
    for (auto const &[_, f] : cnt_map) {
        ++counting[f];
    }

    int ans = 0, removed = 0, half = N / 2, freq = N;
    while (removed < half) {
        ans += 1;
        while (counting[freq] == 0) {
            --freq;
        }
        removed += freq;
        --counting[freq];
    }

    return ans;
}

void test_solution(vector<int> const &arr, int expected)
{
    using SolutionFunc = function<int(vector<int> const &)>;

    auto const test_impl = [](SolutionFunc func, string_view func_name, vector<int> const &arr,
                              int expected) {
        auto const res = func(arr);
        if (res == expected) {
            fmt::print(pass_color,
                       "PASSED {} => Min size of set so at least half of integers of the {} are "
                       "removed is {}\n",
                       func_name, fmt::join(arr, ","), res);
        }
        else {
            fmt::print(fail_color,
                       "FAILED {} => Min size of set so at least half of integers of the {} are "
                       "removed is {} but expected {}\n",
                       func_name, fmt::join(arr, ","), res, expected);
        }
    };

    test_impl(minSetSize_unorderedmap_and_sort, "minSetSize_unorderedmap_and_sort", arr, expected);
    test_impl(minSetSize_unorderedmap_and_countingsort, "minSetSize_unorderedmap_and_countingsort",
              arr, expected);
}

int main()
{
    test_solution({3, 3, 3, 3, 5, 5, 5, 2, 2, 7}, 2);
    test_solution({7, 7, 7, 7, 7, 7}, 1);
    test_solution({1, 9}, 1);
    test_solution({1000, 1000, 3, 7}, 1);
    test_solution({7, 3, 3, 1000, 1000}, 1);
    test_solution({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 5);
}