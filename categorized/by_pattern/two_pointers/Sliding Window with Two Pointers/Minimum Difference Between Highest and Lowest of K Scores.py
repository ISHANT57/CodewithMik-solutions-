# MY YOUTUBE VIDEO ON THIS Qn   : https://www.youtube.com/watch?v=k-ZtDvayDys
# Company Tags                  : Will update later
# Leetcode Link                 : https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores

from typing import List


# Approach (Using sorting and two pointers)
# T.C : O(nlogn)
# S.C : O(1)
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)

        nums.sort()

        minDiff = float('inf')

        i = 0
        j = i + k - 1
        while j < n:
            minElement = nums[i]
            maxElement = nums[j]

            minDiff = min(minDiff, maxElement - minElement)
            i += 1
            j += 1

        return minDiff


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().minimumDifference([9, 4, 1, 7], 2) == 2
    assert Solution().minimumDifference([90], 1) == 0
    print("ok")
