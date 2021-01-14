
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst = (nums1 + nums2)
        lst.sort()
        n = len(lst)
        if n % 2:
            return lst[n//2]
        else:
            return (lst[n//2] + lst[(n-1)//2]) / 2


if __name__ == "__main__":
    s = Solution()
    m = s.findMedianSortedArrays([0, 1, 5], [4, 8, 9])
    print(f'median is {m}')
