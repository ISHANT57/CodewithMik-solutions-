from typing import List

INT_MAX = 2**31 - 1

#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=YrRvP9720vY
#     Company Tags                : Will update soon
#     Leetcode Link               : https://leetcode.com/problems/house-robber-iv


# Approach-1 (Brute Force - Recursion + Memoization)
# T.C : O(n*k)
# S.C : O(n*k)
class Solution:
    def solve(self, nums: List[int], i: int, k: int, t: List[List[int]]) -> int:
        if k == 0:
            return 0  # no more house to be covered

        if i >= self.n:  # invalid path
            return INT_MAX

        if t[i][k] != -1:
            return t[i][k]

        take = max(nums[i], self.solve(nums, i + 2, k - 1, t))

        not_take = self.solve(nums, i + 1, k, t)

        t[i][k] = min(take, not_take)
        return t[i][k]

    def minCapability(self, nums: List[int], k: int) -> int:
        self.n = len(nums)
        t = [[-1] * (k + 1) for _ in range(self.n + 1)]
        return self.solve(nums, 0, k, t)


# Approach-2 (Binary Search on Answer "Minimize the Maximum Robbed Amount(capability)")
# T.C : O(n*log(maxC))
# S.C : O(1)
class Solution:
    def isPossible(self, nums: List[int], mid: int, k: int) -> bool:
        house = 0
        i = 0
        while i < len(nums):  # (C++ for-loop with extra i++ inside)
            if nums[i] <= mid:
                house += 1
                i += 1  # skipping adjacent house
            i += 1

        return house >= k  # we managed to rob atleast k houses

    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)

        l = min(nums)
        r = max(nums)

        result = r

        while l <= r:  # O(log(maxC) * n )
            mid = l + (r - l) // 2  # capability

            if self.isPossible(nums, mid, k) == True:
                result = mid
                r = mid - 1
            else:
                l = mid + 1

        return result


if __name__ == "__main__":
    print(Solution().minCapability([2, 3, 5, 9], 2))  # expected 5
    print(Solution().minCapability([2, 7, 9, 3, 1], 2))  # expected 2
