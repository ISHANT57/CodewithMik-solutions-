# MY YOUTUBE VIDEO ON THIS Qn :
# Company Tags                : Yatra
# Leetcode Link               : https://leetcode.com/problems/subarray-product-less-than-k/

# Approach  : Standard Sliding window Problem
# T.C : O(N)
# S.C : O(1)
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        n = len(nums)
        count = 0

        left = 0
        right = 0
        prod = 1

        while right < n:
            prod *= nums[right]

            while prod >= k:
                prod //= nums[left]
                left += 1

            count += (right - left) + 1
            right += 1
        return count


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100) == 8
    assert Solution().numSubarrayProductLessThanK([1, 2, 3], 0) == 0
    print("All tests passed")
