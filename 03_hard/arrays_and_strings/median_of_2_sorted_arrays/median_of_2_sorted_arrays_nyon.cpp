#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;


void printList(const vector<int>& nums)
{
    for (const auto n : nums) {
        cout << n << ",";
    }

    cout << endl;
}


class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        const int len = nums1.size() + nums2.size();
        const int medianPos = len / 2;        

        int pos1 = 0;
        int pos2 = 0;

        int medianVal1 = 0;
        int medianVal2 = 0;

        while (pos1 + pos2 <= medianPos) {
            if (isNum1Smaller(nums1, pos1, nums2, pos2)) {
                medianVal2 = medianVal1;
                medianVal1 = nums1[pos1++];
            }
            else {
                medianVal2 = medianVal1;
                medianVal1 = nums2[pos2++];
            }
        }

        const bool isOdd = (len & 1) == 0;
        if (isOdd) {
            return (medianVal1 + medianVal2) / 2.0;
        }
        else {
            return medianVal1;
        }       
    }

    bool isNum1Smaller(vector<int>& nums1, int pos1, vector<int>& nums2, int pos2) {
        if (pos1 < nums1.size()) {
            if (pos2 < nums2.size() && nums1[pos1] > nums2[pos2]) {
                return false;
            }
            else {
                // num2 exhausted
                return true;
            }
        }

        // num1 exhausted
        return false;
    }
};


void printMedian(vector<int> nums1, vector<int> nums2)
{
    Solution s;    
    auto median = s.findMedianSortedArrays(nums1, nums2);

    cout << "median is " << median << endl;
}


int main()
{
    printMedian({1,3}, {2});
    printMedian({1,2}, {3,4});
    printMedian({0,0}, {0,0});
    printMedian({}, {1});
    printMedian({2}, {});
    printMedian({0,0}, {-1,0,1});
    printMedian({1,3}, {2, 7});
    printMedian({}, {1,2,3,4,5,6});

    return 0;
}