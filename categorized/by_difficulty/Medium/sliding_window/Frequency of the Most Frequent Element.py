# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=iOqH_JnXIOQ
# Company Tags                : META, Amazon(most frequently asked in year 2023)
# Leetcode Link               : https://leetcode.com/problems/frequency-of-the-most-frequent-element/

from typing import List


# Approach-1 (Using Binary Search)
# T.C : O(nlogn)
# S.C : O(n) for prefixSum for effienctly calculating windowSum
class Solution:

    def findBest(self, target_idx: int, k: int, nums: List[int], prefixSum: List[int]) -> int:
        target = nums[target_idx]

        i = 0
        j = target_idx
        result = target_idx

        while i <= j:
            mid = i + (j - i) // 2

            count = (target_idx - mid + 1)
            windowSum = (count * target)
            currSum = prefixSum[target_idx] - prefixSum[mid] + nums[mid]

            ops = windowSum - currSum

            if ops > k:
                i = mid + 1
            else:
                result = mid
                j = mid - 1

        return target_idx - result + 1

    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)

        nums.sort()
        prefixSum = [0] * n
        prefixSum[0] = nums[0]

        for i in range(1, n):
            prefixSum[i] = prefixSum[i - 1] + nums[i]

        result = 0

        for i in range(n):
            result = max(result, self.findBest(i, k, nums, prefixSum))

        return result


Approach1 = Solution


# Approach-2 (Using sliding window)
# T.C : O(nlogn)
# S.C : O(1)
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        n = len(nums)

        result = 0

        i = 0
        currSum = 0

        for j in range(n):

            target = nums[j]
            currSum += nums[j]

            while (j - i + 1) * target - currSum > k:
                currSum -= nums[i]
                i += 1

            result = max(result, j - i + 1)

        return result


Approach2 = Solution


# Approach-3 (Improved sliding window)
# T.C : O(nlogn)
# S.C : O(1)
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        n = len(nums)

        result = 0

        i = 0
        currSum = 0

        for j in range(n):

            target = nums[j]
            currSum += nums[j]

            if (j - i + 1) * target - currSum > k:
                currSum -= nums[i]
                i += 1

            result = max(result, j - i + 1)

        return result


Approach3 = Solution


if __name__ == "__main__":
    for A in (Approach1, Approach2, Approach3):
        assert A().maxFrequency([1, 2, 4], 5) == 3
        assert A().maxFrequency([1, 4, 8, 13], 5) == 2
        assert A().maxFrequency([3, 9, 6], 2) == 1
    print("ok")
