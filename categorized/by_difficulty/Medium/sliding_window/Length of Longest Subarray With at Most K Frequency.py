from typing import List
from collections import defaultdict

#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=txSMzRMREKA
#     Company Tags                :
#     Leetcode Link               : https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/

# *********************************************************************** C++ **********************************************************
# Approach-1 (With Nested Loop - Classic Sliding Window Template)
# T.C : O(n)
# S.C : O(n)
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)

        mp = defaultdict(int)  # unordered_map<int, int>

        i = 0
        j = 0
        result = 0

        while j < n:

            mp[nums[j]] += 1

            while i < j and mp[nums[j]] > k:
                mp[nums[i]] -= 1
                i += 1

            result = max(result, j - i + 1)
            j += 1

        return result


Approach1 = Solution


# Approach-2 (Without nested loop)
# T.C : O(n)
# S.C : O(n)
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mp = defaultdict(int)  # unordered_map<int, int>

        i = 0
        j = 0
        result = 0

        culprit = 0

        while j < n:

            mp[nums[j]] += 1
            if mp[nums[j]] == k + 1:
                culprit += 1

            if culprit > 0:
                mp[nums[i]] -= 1
                if mp[nums[i]] == k:
                    culprit -= 1
                i += 1

            if culprit == 0:
                result = max(result, j - i + 1)
            j += 1

        return result


Approach2 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2):
        assert S().maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], 2) == 6
        assert S().maxSubarrayLength([1, 2, 1, 2, 1, 2, 1, 2], 1) == 2
        assert S().maxSubarrayLength([5, 5, 5, 5, 5, 5, 5], 4) == 4
    print("All tests passed")
