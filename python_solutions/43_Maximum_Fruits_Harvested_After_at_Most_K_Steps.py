#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=9biz4kxyVh8
#     Company Tags                : Will update soon
#     Leetcode Link               : https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/

from typing import List
from bisect import bisect_left, bisect_right  # lower_bound / upper_bound


# Approach (Binary Search and prefix sum)
# T.C : O(n+klogn)
# S.C : O(n)
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        prefixSum = [0] * n
        indices = [0] * n

        # Build prefix sum and extract indices
        for i in range(n):
            indices[i] = fruits[i][0]
            prefixSum[i] = fruits[i][1] + (prefixSum[i - 1] if i > 0 else 0)

        maxFrutis = 0

        for d in range(k // 2 + 1):
            # Move
            remain = k - 2 * d
            i = startPos - d
            j = startPos + remain

            left = bisect_left(indices, i)
            right = bisect_right(indices, j) - 1

            if left <= right:
                total = prefixSum[right] - (prefixSum[left - 1] if left > 0 else 0)
                maxFrutis = max(maxFrutis, total)

            # Second case: move right x, then left (k - 2x)
            i = startPos - remain
            j = startPos + d

            left = bisect_left(indices, i)
            right = bisect_right(indices, j) - 1

            if left <= right:
                total = prefixSum[right] - (prefixSum[left - 1] if left > 0 else 0)
                maxFrutis = max(maxFrutis, total)

        return maxFrutis


if __name__ == "__main__":
    s = Solution()
    print(s.maxTotalFruits([[2, 8], [6, 3], [8, 6]], 5, 4))  # 9
    print(s.maxTotalFruits([[0, 9], [4, 1], [5, 7], [6, 2], [7, 4], [10, 9]], 5, 4))  # 14
    print(s.maxTotalFruits([[0, 3], [6, 4], [8, 5]], 3, 2))  # 0
