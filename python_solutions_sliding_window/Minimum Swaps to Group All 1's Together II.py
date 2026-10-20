# Scroll below to see JAVA code also (Java sections skipped in this Python port)
# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=t82KJaI1kNQ
# Company Tags                : Microsoft, Adobe
# Leetcode Link               : https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii

from typing import List


# Approach-1 (Using extra space + Khandani Sliding Window)
# T.C : O(n)
# S.C : O(2*n) ~ O(n)
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        temp = [0] * (2 * n)
        for i in range(2 * n):
            temp[i] = nums[i % n]

        countOnes = sum(nums)

        i = 0
        j = 0
        currCount = 0
        maxCount = 0

        while j < 2 * n:
            if temp[j] == 1:
                currCount += 1

            if j - i + 1 > countOnes:
                currCount -= temp[i]
                i += 1

            maxCount = max(maxCount, currCount)
            j += 1

        return countOnes - maxCount


Approach1 = Solution


# Approach-2 (Khandani Sliding Window without extra space)
# T.C : O(n)
# S.C : O(1)
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        countOnes = sum(nums)

        i = 0
        j = 0
        currCount = 0
        maxCount = 0

        while j < 2 * n:
            if nums[j % n] == 1:
                currCount += 1

            if j - i + 1 > countOnes:
                currCount -= nums[i % n]
                i += 1

            maxCount = max(maxCount, currCount)
            j += 1

        return countOnes - maxCount


Approach2 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2):
        assert S().minSwaps([0, 1, 0, 1, 1, 0, 0]) == 1
        assert S().minSwaps([0, 1, 1, 1, 0, 0, 1, 1, 0]) == 2
        assert S().minSwaps([1, 1, 0, 0, 1]) == 0
    print("all tests passed")
