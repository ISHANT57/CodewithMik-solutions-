# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=eGqs55VTP3I
# Company Tags                : Amazon
# Leetcode Link               : https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

from typing import List


# Approach-1 (Produce all subsequences, find min and max and check)
# This will give TLE
# (No code in the original source for this approach)


# Approach-2 (Using Sorting + Two Pointer Approach)
# T.C : O(nlogn)
# S.C : O(n)
class Solution:
    M = 10**9 + 7

    def numSubseq(self, nums: List[int], target: int) -> int:
        M = self.M
        n = len(nums)

        # 1. Sort
        nums.sort()

        power = [0] * n
        power[0] = 1

        for i in range(1, n):
            power[i] = (power[i - 1] * 2) % M

        # 2. l = 0, r = n-1
        l, r = 0, n - 1
        result = 0
        while l <= r:

            if nums[l] + nums[r] <= target:
                diff = r - l
                result = (result % M + power[diff]) % M
                l += 1
            else:
                r -= 1

        return result


Approach2 = Solution


if __name__ == "__main__":
    assert Solution().numSubseq([3, 5, 6, 7], 9) == 4
    assert Solution().numSubseq([3, 3, 6, 8], 10) == 6
    assert Solution().numSubseq([2, 3, 3, 4, 6, 7], 12) == 61
    print("ok")
