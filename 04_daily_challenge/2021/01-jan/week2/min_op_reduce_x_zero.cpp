#include <vector>
#include <iostream>
#include <cassert>

using namespace std;


class Solution {
public:
    int minOperations(vector<int>& nums, int x) {

        int start = 0;
        int end = nums.size() - 1;
        int minOps = 0;

        traverse(nums, x, start, end, 0, minOps);

        return (minOps > 0) ? minOps : -1;
    }

    void traverse(vector<int>& nums, int rem, int start, int end, int ops, int& minOps) {

        if (start > end) {
            return;
        }

        const int remLeft = rem - nums[start];
        const int remRight = rem - nums[end];

        /*cout << "remLeft: " << remLeft << '\n';
        cout << "remRight: " << remRight << '\n';*/

        if (remLeft < 0 && remRight < 0) {
            // NO solution found for this operation
            return;
        }

        ++ops;

        if (remLeft == 0) {
            // a solution was found on left
            /*cout << "solution found for left side, start: " << start << ", end: " <<
                end << ", ops: " << ops << '\n';*/
            minOps = (minOps > 0) ? min(minOps, ops) : ops;
            if (minOps >= nums.size()) {
                return;
            }
            // go right
            if (remRight > 0) {
                traverse(nums, remRight, start, end - 1, ops, minOps);
            }
        }
        else if (remRight == 0) {
            // a solution was found on right
            //cout << "solution found for right side, start: " << start << ", end: " <<
            //    end << ", ops: " << ops << '\n';
            minOps = (minOps > 0) ? min(minOps, ops) : ops;
            if (minOps >= nums.size()) {
                return;
            }
            // go left
            if (remLeft > 0) {
                traverse(nums, remLeft, start + 1, end, ops, minOps);
            }
        }
        else {
            if (remLeft > 0) {
                traverse(nums, remLeft, start + 1, end, ops, minOps);
            }
            if (remRight > 0) {
                traverse(nums, remRight, start, end - 1, ops, minOps);
            }
        }

        return;
    }
};


void checkSolution(vector<int> nums, int x, int expected)
{
    Solution s;
    auto minOps = s.minOperations(nums, x);

    if (minOps == expected) {
        cout << "PASSED = minOps is: " << minOps << endl;
    }
    else {
        cout << "FAILED - min Ops is: " << minOps << ", expected: " << expected << endl;
    }
}

int main()
{
    // printSolution({1,2,4,2,3}, 5);
    // printSolution({5,6,7,8,9}, 4);

    //printSolution({ 3,2,20,1,1,3 }, 10);
    //checkSolution({ 1,1,4,2,3 }, 5, 2);

    checkSolution({8828, 9581, 49, 9818, 9974, 9869, 9991, 10000, 10000, 10000, 9999, 9993, 9904, 8819, 1231, 6309}, 134365, 16);

    return 0;
}