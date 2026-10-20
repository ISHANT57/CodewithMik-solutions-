from typing import List
import math

#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=tOo5RX2pt0g
#     Company Tags                : Will update soon
#     Leetcode Link               : https://leetcode.com/problems/minimum-time-to-repair-cars


# Approach (Binary Search on Answer)
# T.C : O(n * log(maxRank * cars * cars))
# S.C : O(1)
class Solution:
    # typedef long long ll  (Python ints are arbitrary precision)

    def isPossible(self, ranks: List[int], mid: int, cars: int) -> bool:
        carsFixed = 0

        for i in range(len(ranks)):
            # math.isqrt on integer floor gives same value as C++ (ll) sqrt(mid/ranks[i]) without float error
            carsFixed += math.isqrt(mid // ranks[i])  # ignoring this

        return carsFixed >= cars

    def repairCars(self, ranks: List[int], cars: int) -> int:
        n = len(ranks)

        l = 1
        maxR = max(ranks)
        r = 1 * maxR * cars * cars

        result = -1
        # T.C: O(n * log(maxR*cars*cars));
        while l <= r:  # log(maxR * cars * cars)
            mid = l + (r - l) // 2

            if self.isPossible(ranks, mid, cars):  # O(n)
                result = mid
                r = mid - 1
            else:
                l = mid + 1

        return result


if __name__ == "__main__":
    print(Solution().repairCars([4, 2, 3, 1], 10))  # expected 16
    print(Solution().repairCars([5, 1, 8], 6))  # expected 16
