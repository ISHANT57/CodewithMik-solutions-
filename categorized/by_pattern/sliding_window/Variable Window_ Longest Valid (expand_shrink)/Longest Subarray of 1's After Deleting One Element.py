# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=SQ8tY9nxeZU
# Company Tags                : Google, Meta
# Leetcode Link               : https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
#
# Similar Problem             : Leetcode - 1004, 487, 485

from typing import List


# Approach-1 (Simple Brute Force) - T.C : O(n^2)
class Solution:
    def findMax(self, nums: List[int], skip_idx: int) -> int:

        currLength = 0
        maxLength = 0

        for i in range(self.n):
            if i == skip_idx:
                continue

            if nums[i] == 1:
                currLength += 1
                maxLength = max(maxLength, currLength)
            else:
                currLength = 0

        return maxLength

    def longestSubarray(self, nums: List[int]) -> int:
        self.n = len(nums)
        n = self.n
        result = 0

        countZero = 0
        for i in range(n):

            if nums[i] == 0:
                countZero += 1
                result = max(result, self.findMax(nums, i))

        if countZero == 0:
            return n - 1

        return result


Approach1 = Solution


# Approach-2 (Using Traditional Sliding Window) - O(n)
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        zeroCount = 0
        longestWindow = 0

        i = 0

        for j in range(len(nums)):
            zeroCount += (nums[j] == 0)

            # Shrink the window until the zero counts come under the limit.
            while zeroCount > 1:
                zeroCount -= (nums[i] == 0)
                i += 1

            longestWindow = max(longestWindow, j - i)

        return longestWindow


Approach2 = Solution


# Approach-3 (Using Better Sliding Window) - O(n))
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i, j = 0, 0

        last_zero_idx = -1

        result = 0

        while j < len(nums):

            if nums[j] == 0:
                i = last_zero_idx + 1
                last_zero_idx = j

            result = max(result, j - i)
            j += 1

        return result


Approach3 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2, Approach3):
        assert S().longestSubarray([1, 1, 0, 1]) == 3
        assert S().longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]) == 5
        assert S().longestSubarray([1, 1, 1]) == 2
    print("all tests passed")
