#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=iOBDwcfrAf0
#     Company Tags                : Will update soon
#     Leetcode Link               : https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/

from typing import List
from bisect import bisect_left  # lower_bound (used in Approach-2, as he used lower_bound)


# Approach-1 (Binary Search + Backtracking Brute Force)
# T.C : O(nCk * k * log side)
# S.C : O(k)
class Solution:
    def manhattanDist(self, p1: List[int], p2: List[int]) -> int:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def check(self, points: List[List[int]], k: int, mid: int, i: int, chosen: List[int]) -> bool:
        if len(chosen) == k:
            return True

        for p in range(i, len(points)):
            valid = True

            for idx in chosen:
                if self.manhattanDist(points[p], points[idx]) < mid:
                    valid = False
                    break

            if not valid:
                continue

            chosen.append(p)
            if self.check(points, k, mid, p + 1, chosen):
                return True
            chosen.pop()

        return False

    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        l = 0
        r = 2 * side

        result = 0

        while l <= r:
            mid = l + (r - l) // 2

            chosen = []

            if self.check(points, k, mid, 0, chosen):
                result = mid
                l = mid + 1
            else:
                r = mid - 1

        return result


Approach1 = Solution  # keep a handle, since Approach-2 below is also named Solution


# Approach-2 (Binary Search + Optimised check)
# T.C : O(nlogn+log(side)⋅n⋅klogn)
# S.C : O(n)
class Solution:
    # typedef long long ll;  (Python ints are arbitrary precision)

    def get1D(self, side: int, x: int, y: int) -> int:
        if y == 0:
            return x

        if x == side:
            return side + y

        if y == side:
            return 3 * side - x

        return 4 * side - y

    def check(self, doubled: List[int], n: int, k: int, side: int, mid: int) -> bool:
        perimeter = 4 * side

        for i in range(n):  # O(n)
            count = 1  # Picked one point
            idx = i

            lastPos = doubled[idx]

            for j in range(2, k + 1):  # O(k * log(n))
                target = lastPos + mid

                it = bisect_left(doubled, target, idx + 1, i + n)

                if it == i + n:
                    break

                idx = it
                lastPos = doubled[idx]
                count += 1

            if count == k and (doubled[i] + perimeter - lastPos >= mid):
                return True

        return False

    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        perimeter = 4 * side
        n = len(points)

        positions = [0] * n

        for i in range(n):
            positions[i] = self.get1D(side, points[i][0], points[i][1])

        positions.sort()

        # double the positions array to easily handle round wrap
        doubled = [0] * (2 * n)
        for i in range(n):
            doubled[i] = positions[i]
            doubled[i + n] = positions[i] + perimeter

        l = 0
        r = 2 * side

        result = 0

        # log(side) * n * klog(n)
        while l <= r:
            mid = l + (r - l) // 2

            if self.check(doubled, n, k, side, mid):
                result = mid
                l = mid + 1
            else:
                r = mid - 1

        return result


if __name__ == "__main__":
    for sol in (Approach1(), Solution()):
        print(sol.maxDistance(2, [[0, 2], [2, 0], [2, 2], [0, 0]], 4))  # 2
        print(sol.maxDistance(2, [[0, 0], [1, 2], [2, 0], [2, 2], [2, 1]], 4))  # 1
        print(sol.maxDistance(2, [[0, 0], [0, 1], [0, 2], [1, 2], [2, 0], [2, 2], [2, 1]], 5))  # 1
