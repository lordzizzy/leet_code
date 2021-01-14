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
        const int m = nums1.size();
        const int n = nums2.size();

        // combine
        vector<int> v;
        v.reserve(m+n);
        v.insert(v.end(), nums1.begin(), nums1.end());
        v.insert(v.end(), nums2.begin(), nums2.end());
        
        // sort
        sort(v.begin(), v.end());

        // find median
        return findMedianSorted(v);
    }

    inline double findMedianSorted(vector<int>& nums1) {
        const int size = nums1.size();
        if ((size & 1) == 0) {
            // even
            return (nums1[(size-1)/2] + nums1[size/2]) / 2.0;
        }
        else {
            // odd
            return nums1[size/2];
        }
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