from typing import List

# Scroll below to see JAVA code also (Java section skipped in this Python port)
#
# MY YOUTUBE VIDEO ON THIS Qn   : https://www.youtube.com/watch?v=-wI7ee4D8KU
# Company Tags                  : Will update later
# Leetcode Link                 : https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/


# *************************************************************** C++ *************************************************
# Approach (2 pointers)
# T.C : O(m+n)
# S.C : O(1)
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)

        i = 0  # nums1
        j = 0  # nums2

        result = 0

        while i < m and j < n:
            if nums1[i] > nums2[j]:
                i += 1
            else:
                result = max(result, j - i)
                j += 1

        return result


Approach1 = Solution

if __name__ == "__main__":
    assert Solution().maxDistance([55, 30, 5, 4, 2], [100, 20, 10, 10, 5]) == 2
    assert Solution().maxDistance([2, 2, 2], [10, 10, 1]) == 1
    assert Solution().maxDistance([30, 29, 19, 5], [25, 25, 25, 25, 25]) == 2
    print("ok")
