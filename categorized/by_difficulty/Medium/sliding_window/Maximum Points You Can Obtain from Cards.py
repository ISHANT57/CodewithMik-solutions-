# MY YOUTUBE VIDEO ON THIS Qn :
# Company Tags                : Media.net, Google (Most asked in 2021)
# Leetcode Link               : https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
# Also known as               : Pick From Both Sides

# Solution with explanation:
# Keywords : Minimum/Maximum , k cards (similar to k-size window)  (Hints towards Sliding Window Technique)

from typing import List


# Approach-1 (Sliding Window)
# NOTE: the original C++ body referred to `nums` while the parameter was named
# `cardPoints` (would not compile); `nums = cardPoints` alias is added below.
class Solution:
    def solve_sliding_window(self, cardPoints: List[int], k: int) -> int:
        # When we find max score of size k, we are left with subarray of size (n-k) which has minimum sum
        # so, we find total_sum and we find minimum_sum of subarrays of size (n-k)
        # choose best of (total_sum - minimum_sum)
        # Best way to use sliding window technique
        #
        #     Example : cardPoints{5, 7, 2, 100, 1}, k = 3
        #     total_sum = 115
        #     window_size = n-k = 5-3 = 2
        #     window_1 = {5, 7}  , sum = 12
        #     window_2 = {7, 2}  , sum = 9   -> minimum
        #     window_3 = {2, 100}, sum = 102
        #     window_4 = {100, 1}, sum = 101
        #
        #     return total_sum - 9 = 115 - 9 = 106
        nums = cardPoints
        n = len(nums)
        totalSum = 0
        l = n - k
        currSum = 0
        minSum = 2**31 - 1  # INT_MAX
        i, j = 0, 0

        while j < n:
            totalSum += nums[j]
            currSum += nums[j]
            if j - i + 1 == l:
                minSum = min(minSum, currSum)
                currSum -= nums[i]
                i += 1
            j += 1
        return totalSum if minSum == 2**31 - 1 else totalSum - minSum

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        return self.solve_sliding_window(cardPoints, k)


Approach1 = Solution


# Approach-2 (Recur + Memo) - TLE
class Solution:
    def solve(self, nums: List[int], i: int, j: int, count: int) -> int:
        if count == self.k:
            return 0
        if i >= self.n or j < 0:
            return 0

        key = str(i) + "_" + str(j) + "_" + str(count)
        if key in self.mp:
            return self.mp[key]

        take_i = nums[i] + self.solve(nums, i + 1, j, count + 1)
        take_j = nums[j] + self.solve(nums, i, j - 1, count + 1)

        self.mp[key] = max(take_i, take_j)
        return self.mp[key]

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        self.mp = {}  # unordered_map<string, int>
        self.k = k
        self.n = len(cardPoints)

        return self.solve(cardPoints, 0, self.n - 1, 0)


Approach2 = Solution


# Approach-3 (DP)
class Solution:
    def solve_dp(self, cardPoints: List[int], k: int) -> int:
        # Example : cardPoints{5, 7, 2, 100, 1}, k = 3
        front_card = [0] * k
        back_card = [0] * k
        n = len(cardPoints)
        front_card[0] = cardPoints[0]
        back_card[0] = cardPoints[n - 1]

        for i in range(1, k):
            front_card[i] = front_card[i - 1] + cardPoints[i]
            back_card[i] = back_card[i - 1] + cardPoints[n - i - 1]
        # front_card {5, 12, 14} ; front_card[i] = sum when we take (i+1) elements from front
        # back_card  {1, 101, 103}; back_card[i] = sum when we take (i+1) elements from back

        # let's suppose we took k elements front front or back whichever gives me max
        maxScr = max(back_card[k - 1], front_card[k - 1])  # max(103, 14)

        # You have following options (for k = 3)
        # front_elements              back_elements               maxScr
        # 0 elements                  3 elements (i.e.2, 100, 1)  103   -> back_card[k-1]
        #
        # 1 elements (i.e.5)          2 elements (i.e. 100, 1)    106   -> MAXIMUM :-)
        #
        # 2 elements (i.e.5, 7)       1 elements (i.e. 1)         13
        #
        # 3 elements (i.e.5, 7, 2)    0 elements                  14   -> front_card[k-1]

        for i in range(0, k - 1):  # we have already considered i = k-1 (to determine maxScr above)

            sum_front = front_card[i]       # front_card[0] = {5}       sum = 5
            sum_back = back_card[k - i - 2]  # back_card[1]  = {100, 1}  sum = 101

            if sum_front + sum_back > maxScr:
                maxScr = sum_front + sum_back

        return maxScr

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        return self.solve_dp(cardPoints, k)


Approach3 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2, Approach3):
        assert S().maxScore([1, 2, 3, 4, 5, 6, 1], 3) == 12
        assert S().maxScore([2, 2, 2], 2) == 4
        assert S().maxScore([9, 7, 7, 9, 7, 7, 9], 7) == 55
        assert S().maxScore([5, 7, 2, 100, 1], 3) == 106
    print("all tests passed")
