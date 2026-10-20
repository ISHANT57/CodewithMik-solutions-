from typing import List

#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=9UxjDEBt8Vg
#     Company Tags                : Will update soon
#     Leetcode Link               : https://leetcode.com/problems/maximum-candies-allocated-to-k-children


# Approach-1 (Brute Force)
# T.C : O(n * maxC), maxC = maximum candy value
# S.C : O(1)
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        n = len(candies)

        maxC = 0
        total = 0
        for i in range(n):
            total += candies[i]
            maxC = max(maxC, candies[i])

        if total < k:
            return 0

        # Brute force try from maxC till 1
        for c in range(maxC, 0, -1):
            count = 0

            for i in range(len(candies)):
                count += candies[i] // c  # how many children can get c candies from this pile
            if count >= k:
                return c

        return 0


# Approach-2 (Binary Search on answer)
# T.C : O(n * log(maxC)), maxC = maximum candy value
# S.C : O(1)
class Solution:
    def canDistr(self, candies: List[int], mid: int, k: int) -> bool:
        n = len(candies)

        for i in range(n):
            k -= candies[i] // mid

            if k <= 0:  # all children got mid candies
                return True  # Early return

        return k <= 0  # all children got the mid candies

    def maximumCandies(self, candies: List[int], k: int) -> int:
        n = len(candies)

        maxC = 0
        total = 0
        for i in range(n):
            total += candies[i]
            maxC = max(maxC, candies[i])

        if total < k:
            return 0

        l = 1
        r = maxC
        result = 0
        while l <= r:
            mid = l + (r - l) // 2

            if self.canDistr(candies, mid, k):
                result = mid
                l = mid + 1
            else:
                r = mid - 1

        return result


if __name__ == "__main__":
    print(Solution().maximumCandies([5, 8, 6], 3))  # expected 5
    print(Solution().maximumCandies([2, 5], 11))  # expected 0
