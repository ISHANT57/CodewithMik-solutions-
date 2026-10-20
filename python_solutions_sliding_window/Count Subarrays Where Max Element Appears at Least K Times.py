# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=06VaWkj8e-0
# Company Tags                : will update soon
# Leetcode Link               : https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

from typing import List

# Approach-1 (Classic sliding window)
# T.C : O(n)
# S.C : O(1)
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxE = max(nums)

        n = len(nums)
        i = 0
        j = 0

        result = 0
        countMax = 0

        while j < n:
            if nums[j] == maxE:
                countMax += 1

            while countMax >= k:
                result += n - j

                if nums[i] == maxE:
                    countMax -= 1
                i += 1
            j += 1

        return result


Approach1 = Solution


# Approach-2 (Without Sliding Window)
# T.C : O(n)
# S.C : O(n)
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxE = max(nums)

        n = len(nums)

        result = 0

        maxIndices = []

        for i in range(n):
            if nums[i] == maxE:
                maxIndices.append(i)

            size = len(maxIndices)
            if size >= k:
                last_i = maxIndices[size - k]
                result += last_i + 1

        return result


Approach2 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2):
        assert S().countSubarrays([1, 3, 2, 3, 3], 2) == 6
        assert S().countSubarrays([1, 4, 2, 1], 3) == 0
    print("ok")
