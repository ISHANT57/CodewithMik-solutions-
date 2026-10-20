from typing import List

#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=5gtuhc-a_DQ
#     Company Tags                : Will update soon
#     Leetcode Link               : https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag


# Approach (Using Binary Search in Answer - See the problem statement : It asks to Minimize the Maximum which hints towards Binary Search On Answer)
# T.C : O(nlog(MAX)), where n = length of nums, MAX = max value in nums
# S.C : O(1)
class Solution:

    def isPossible(self, nums: List[int], maxOps: int, mid: int) -> bool:
        totalOps = 0  # to bring each number <= mid

        for num in nums:
            ops = num // mid

            if num % mid == 0:
                ops -= 1

            totalOps += ops

        return totalOps <= maxOps

    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l = 1
        r = max(nums)

        result = r  # we have to minimize this

        # O(n * log(MAX))
        while l <= r:
            mid = l + (r - l) // 2

            if self.isPossible(nums, maxOperations, mid) == True:
                result = mid
                r = mid - 1
            else:
                l = mid + 1

        return result


if __name__ == "__main__":
    print(Solution().minimumSize([9], 2))  # expected 3
    print(Solution().minimumSize([2, 4, 8, 2], 4))  # expected 2
