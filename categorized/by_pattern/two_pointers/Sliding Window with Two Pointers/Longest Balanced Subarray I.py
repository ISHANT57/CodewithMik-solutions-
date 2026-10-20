from typing import List

# Scroll below to see JAVA code also (Java section skipped in this Python port)
#
# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=fZBdZ5TDKOw
# Company Tags                : Will update later
# Leetcode Link               : https://leetcode.com/problems/longest-balanced-subarray-i


# *************************************************************** C++ *************************************************
# Approach (try all subarrays)
# T.C : O(n^2)
# S.C : O(n)
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)

        maxLen = 0

        for i in range(n):
            even = set()  # unordered_set -> set
            odd = set()

            for j in range(i, n):
                if nums[j] % 2 == 0:
                    even.add(nums[j])
                else:
                    odd.add(nums[j])

                if len(even) == len(odd):
                    maxLen = max(maxLen, j - i + 1)

        return maxLen


Approach1 = Solution

if __name__ == "__main__":
    assert Solution().longestBalanced([2, 5, 4, 3]) == 4
    assert Solution().longestBalanced([3, 2, 2, 5, 4]) == 5
    assert Solution().longestBalanced([1, 2, 3, 2]) == 3
    print("ok")
