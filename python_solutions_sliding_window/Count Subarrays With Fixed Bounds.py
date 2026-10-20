# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=z6LwIkEn9qc
# Company Tags                : Microsoft
# Leetcode Link               : https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

from typing import List

# Approach-1 (Brute Force)
# T.C : O(n^2)
# S.C : O(1)
# Find all subarrays and check if min is minK and max is maxK
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        count = 0

        for start in range(n):
            currentMin = nums[start]
            currentMax = nums[start]

            for end in range(start, n):
                currentMin = min(currentMin, nums[end])
                currentMax = max(currentMax, nums[end])

                if currentMin == minK and currentMax == maxK:
                    count += 1

        return count


Approach1 = Solution


# Approach-2 : Sliding Window
# T.C : O(n)
# S.C : O(1)
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0

        minPosition = -1
        maxPosition = -1
        leftBound = -1

        for i in range(len(nums)):

            if nums[i] < minK or nums[i] > maxK:
                leftBound = i

            if nums[i] == minK:
                minPosition = i
            if nums[i] == maxK:
                maxPosition = i

            count = min(maxPosition, minPosition) - leftBound

            ans += 0 if count <= 0 else count

        return ans


Approach2 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2):
        assert S().countSubarrays([1, 3, 5, 2, 7, 5], 1, 5) == 2
        assert S().countSubarrays([1, 1, 1, 1], 1, 1) == 10
    print("ok")
