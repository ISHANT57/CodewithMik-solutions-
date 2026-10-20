# MY YOUTUBE VIDEO ON THIS Qn   : https://www.youtube.com/watch?v=d4qAUbuEqvw
# Company Tags                  : Will update later
# Leetcode Link                 : https://leetcode.com/problems/minimum-removals-to-balance-array

from typing import List


# Approach (Using sorting and two pointers)
# T.C : O(nlogn)
# S.C : O(1)
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        maxEl = nums[0]
        minEl = nums[0]

        L = 1
        i = 0
        j = 0

        while j < n:
            maxEl = nums[j]
            minEl = nums[i]

            while i < j and maxEl > k * minEl:
                i += 1
                minEl = nums[i]

            L = max(L, j - i + 1)
            j += 1

        return n - L


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().minRemoval([2, 1, 5], 2) == 1
    assert Solution().minRemoval([1, 6, 2, 9], 3) == 2
    assert Solution().minRemoval([4, 6], 2) == 0
    print("ok")
