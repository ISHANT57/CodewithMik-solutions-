# MY YOUTUBE VIDEO ON THIS Qn - https://www.youtube.com/watch?v=lGo6E8jiDB8
# Company Tags                - MICROSOFT
# Leetcode Link               - https://leetcode.com/problems/minimum-cost-to-make-array-equal/

from typing import List

INT_MAX = 2**31 - 1


class Solution:

    def getCost(self, nums: List[int], cost: List[int], target: int) -> int:
        result = 0
        for i in range(len(nums)):
            result += abs(nums[i] - target) * cost[i]
        return result

    def minCost(self, nums: List[int], cost: List[int]) -> int:

        answer = INT_MAX

        left = min(nums)   # 1
        right = max(nums)  # 5

        while left <= right:
            mid = left + (right - left) // 2

            cost1 = self.getCost(nums, cost, mid)
            cost2 = self.getCost(nums, cost, mid + 1)

            answer = min(cost1, cost2)
            if cost1 > cost2:
                left = mid + 1
            else:
                right = mid - 1
        return 0 if answer == INT_MAX else answer


if __name__ == "__main__":
    s = Solution()
    assert s.minCost([1, 3, 5, 2], [2, 3, 1, 14]) == 8
    assert s.minCost([2, 2, 2, 2, 2], [4, 2, 8, 1, 3]) == 0
    print("ok")
