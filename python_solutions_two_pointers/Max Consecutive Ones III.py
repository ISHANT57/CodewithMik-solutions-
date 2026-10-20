from typing import List

# Company Tags  : Google (With some Variations)
# Leetcode Link : https://leetcode.com/problems/max-consecutive-ones-iii/

# Approach-1 (Two Pointer Technique)
class Solution:
    # C++ took count, i, j by reference; here they are returned as (count, j) since i and k are not modified
    def moveUntilOneCount(self, nums: List[int], count: int, i: int, j: int, k: int):
        if count > k:
            while j <= i and count > k:
                if nums[j] == 0:
                    count -= 1
                j += 1
        return count, j

    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if k >= n:
            return n

        result = 0
        count = 0
        i, j = 0, 0
        while i < n:
            if nums[i] == 0:
                count += 1
                count, j = self.moveUntilOneCount(nums, count, i, j, k)
            result = max(result, i - j + 1)
            i += 1
        return result


Approach1 = Solution


# Approach-2 (2 pointer techinique with slight improvement)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if k >= n:
            return n

        result = 0
        count = 0
        i, j = 0, 0
        while i < n:
            if nums[i] == 0:
                count += 1
            if count > k:
                count -= 1 if nums[j] == 0 else 0  # decrement k only if you are crossing leaving 0 behind
                j += 1
            result = max(result, i - j + 1)
            i += 1
        return result


Approach2 = Solution

if __name__ == "__main__":
    for S in (Approach1, Approach2):
        assert S().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6
        assert S().longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3) == 10
    print("ok")
