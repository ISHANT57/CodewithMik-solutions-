# MY YOUTUBE VIDEO ON THIS Qn : Part-1 (Brute & Better) - https://www.youtube.com/watch?v=6D9T2ZY8h5c
#                               Part-1 (Binary Search)  - https://www.youtube.com/watch?v=7nABqJCEMuY
# Company Tags                : Google, Microsoft, Apple, Zenefits, Yahoo, Adobe, Dropbox
# Leetcode Link               : https://leetcode.com/problems/median-of-two-sorted-arrays/

from typing import List

INT_MIN = -2**31
INT_MAX = 2**31 - 1


# Approach-1 - Brute Force
# T.C : O(m+n)
# S.C : O(m+n)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        temp = [0] * (m + n)
        i = 0
        j = 0
        k = 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                temp[k] = nums1[i]
                k += 1
                i += 1
            else:
                temp[k] = nums2[j]
                k += 1
                j += 1

        while i < m:
            temp[k] = nums1[i]
            k += 1
            i += 1
        while j < n:
            temp[k] = nums2[j]
            k += 1
            j += 1

        size = m + n

        if size % 2 != 0:
            return temp[size // 2]

        return (temp[size // 2] + temp[(size // 2) - 1]) / 2.0


Approach1 = Solution  # alias so every approach can be tested below


# Approach-2 - Optimising Space from Approach-1
# T.C : O(m+n)
# S.C : O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        size = m + n

        idx1 = (size // 2) - 1
        element1 = -1
        idx2 = size // 2
        element2 = -1

        i = 0
        j = 0
        k = 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                if k == idx1:
                    element1 = nums1[i]
                if k == idx2:
                    element2 = nums1[i]
                i += 1
            else:
                if k == idx1:
                    element1 = nums2[j]
                if k == idx2:
                    element2 = nums2[j]
                j += 1
            k += 1

        while i < m:
            if k == idx1:
                element1 = nums1[i]
            if k == idx2:
                element2 = nums1[i]
            i += 1
            k += 1

        while j < n:
            if k == idx1:
                element1 = nums2[j]
            if k == idx2:
                element2 = nums2[j]
            j += 1
            k += 1

        if size % 2 == 1:
            return element2

        return (element1 + element2) / 2.0


Approach2 = Solution


# Approach-3 (Using Binary Search)
# T.C : O(log(min(m, n))
# S.C : O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m = len(nums1)
        n = len(nums2)

        low = 0
        high = m
        while low <= high:

            Px = low + (high - low) // 2
            Py = (m + n + 1) // 2 - Px

            x1 = INT_MIN if Px == 0 else nums1[Px - 1]
            x3 = INT_MAX if Px == m else nums1[Px]

            x2 = INT_MIN if Py == 0 else nums2[Py - 1]
            x4 = INT_MAX if Py == n else nums2[Py]

            if x1 <= x4 and x2 <= x3:
                if (m + n) % 2 == 0:
                    return (max(x1, x2) + min(x3, x4)) / 2.0

                return max(x1, x2)
            elif x1 > x4:
                high = Px - 1
            else:
                low = Px + 1

        return -1


Approach3 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2, Approach3):
        assert S().findMedianSortedArrays([1, 3], [2]) == 2.0
        assert S().findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    print("ok")
