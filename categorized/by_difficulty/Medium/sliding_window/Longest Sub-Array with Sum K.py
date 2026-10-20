from typing import List

#     Company Tags : Amazon
#     Qn Link      : https://practice.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1#

# This is actually a variable sized "sliding window technique"
class Solution:
    def lenOfLongSubarr(self, nums: List[int], n: int, k: int) -> int:
        sum = 0
        mp = {}  # unordered_map<int, int>
        mp[0] = -1
        len = 0
        for i in range(n):
            sum += nums[i]
            required = sum - k
            if required in mp:
                len = max(len, i - mp[required])

            if sum not in mp:
                mp[sum] = i

        return len


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().lenOfLongSubarr([10, 5, 2, 7, 1, 9], 6, 15) == 4
    assert Solution().lenOfLongSubarr([-5, 8, -14, 2, 4, 12], 6, -5) == 5
    assert Solution().lenOfLongSubarr([10, -10, 20, 30], 4, 5) == 0
    print("All tests passed")
