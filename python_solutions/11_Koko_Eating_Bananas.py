from typing import List

# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=QQcEIxK-snE
# Company Tags                : Google, Miscrosoft
# Leetcode Link               : https://leetcode.com/problems/koko-eating-bananas/


# Binary Search - Using same concept as "Leetcode-2187 : Minimum Time to Complete Trips"
class Solution:

    def canEatAll(self, piles: List[int], givenHour: int, h: int) -> bool:
        actualHour = 0

        for x in piles:
            actualHour += x // givenHour

            if x % givenHour != 0:
                actualHour += 1

        return actualHour <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)

        l, r = 1, max(piles)

        while l < r:
            mid = l + (r - l) // 2

            if self.canEatAll(piles, mid, h):
                r = mid
            else:
                l = mid + 1

        return l


if __name__ == "__main__":
    s = Solution()
    assert s.minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert s.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert s.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
    print("OK")
