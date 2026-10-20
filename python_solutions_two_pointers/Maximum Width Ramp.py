from typing import List

# Scroll below to see JAVA code also (Java section skipped in this Python port)
#
# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=mcJBhWXel-Y
# Company Tags                : Google, Amazon, Microsoft, Adobe
# Leetcode Link               : https://leetcode.com/problems/maximum-width-ramp


# ********************************************************************** C++ **********************************************************************
# Approach-1 (Using brute force) - Passes 95/101 test cases
# T.C : O(n^2)
# S.C : O(1)
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        ramp = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] <= nums[j]:
                    ramp = max(ramp, j - i)
        return ramp


Approach1 = Solution


# Approach-2 (early termination) - Passes 97/101 test cases
# T.C : O(n^2) in worst case
# S.C : O(1)
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)

        ramp = 0

        for i in range(n):
            for j in range(n - 1, i, -1):
                if nums[i] <= nums[j]:
                    ramp = max(ramp, j - i)
                    break
        return ramp


Approach2 = Solution


# Approach-3 : Two Pointer (Making use of hint from Approach-2, storing max to the right) - ACCEPTED
# T.C : O(n)
# S.C : O(n)
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        maxRight = [0] * n
        maxRight[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], nums[i])

        ramp = 0
        i = 0
        j = 0

        while j < n:
            while i < j and nums[i] > maxRight[j]:
                i += 1

            ramp = max(ramp, j - i)
            j += 1

        return ramp


Approach3 = Solution

if __name__ == "__main__":
    for S in (Approach1, Approach2, Approach3):
        assert S().maxWidthRamp([6, 0, 8, 2, 1, 5]) == 4
        assert S().maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]) == 7
    print("ok")
