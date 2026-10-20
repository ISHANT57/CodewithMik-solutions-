# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=Op07kT-LoH8
# Company Tags                : GOOGLE
# Leetcode Link               : https://leetcode.com/problems/peak-index-in-a-mountain-array/

# A very good Followup Qn on this - Leetcode - 1059 : Find in Mountain Array

from typing import List


# Approach-1 (Using Linear Search) - T.C : O(n)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)

        i = 0
        # You can remove i < n-1 check because array is gauranteed to be Mountain (given in qn)
        while i < n - 1 and arr[i] < arr[i + 1]:
            i += 1

        return i


# Approach-2 (Using Binary Search) - T.C : O(log(n))
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)

        l = 0
        r = n - 1

        while l < r:

            mid = l + (r - l) // 2

            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid

        return l


if __name__ == "__main__":
    # second class definition (Approach-2) is the active Solution
    s = Solution()
    assert s.peakIndexInMountainArray([0, 1, 0]) == 1
    assert s.peakIndexInMountainArray([0, 2, 1, 0]) == 1
    assert s.peakIndexInMountainArray([0, 10, 5, 2]) == 1
    print("ok")
