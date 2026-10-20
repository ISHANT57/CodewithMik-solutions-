# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=fZl7ymC0uaU
# Company Tag                 : will update later
# Leetcode Link               : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy

from typing import List

# Approach (Using khandani Sliding Window)
# T.C : O(n)
# S.C : O(n)
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        actualProfit = 0
        profit = [0] * n  # original Profit of each day

        for i in range(n):
            profit[i] = strategy[i] * prices[i]
            actualProfit += profit[i]

        originalWindowProfit = 0
        modifiedWindowProfit = 0
        maxGain = 0  # modifiedWindowProfit - originalWindowProfit

        i = 0
        j = 0

        # Khandani sliding window technique
        while j < n:

            originalWindowProfit += profit[j]

            # Second half of the window contributes to modifiedWindowProfit
            if j - i + 1 > k // 2:
                modifiedWindowProfit += prices[j]

            if j - i + 1 > k:
                originalWindowProfit -= profit[i]
                modifiedWindowProfit -= prices[i + k // 2]
                i += 1

            # Evaluate window of size k
            if j - i + 1 == k:
                maxGain = max(maxGain, modifiedWindowProfit - originalWindowProfit)

            j += 1

        return actualProfit + maxGain


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().maxProfit([4, 2, 8], [-1, 0, 1], 2) == 10
    assert Solution().maxProfit([5, 4, 3], [1, 1, 0], 2) == 9
    print("ok")
