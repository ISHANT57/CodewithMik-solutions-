from typing import List

# Scroll below to see JAVA code also (Java section skipped in this Python port)
#
# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=1L9C3a38fHU
# Company Tags                : AMAZON
# Leetcode Link               : https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/description/
# Similar Leetcode Porblem    : Leetcode 881. Boats to Save People

# ***************************************************************** C++ ******************************************************************************
# Simple 2-pointer approach
# T.C : O(nlogn) due to sorting
# S.C : O(1)
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        maxResult = 0

        i, j = 0, len(nums) - 1

        while i < j:
            sum = nums[i] + nums[j]

            maxResult = max(maxResult, sum)
            i += 1
            j -= 1

        return maxResult


Approach1 = Solution

if __name__ == "__main__":
    assert Solution().minPairSum([3, 5, 2, 3]) == 7
    assert Solution().minPairSum([3, 5, 4, 2, 4, 6]) == 8
    print("ok")
