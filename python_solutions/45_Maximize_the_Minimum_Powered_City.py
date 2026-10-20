#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=CAvYhc74Eio
#     Company Tags                : Will update soon
#     Leetcode Link               : https://leetcode.com/problems/maximize-the-minimum-powered-city

from typing import List


# Approach (Binary search along with Difference Array Technique for optimisation
# T.C : O(n * log(sum+k)), sum = sum of station values
# S.C : O(n)
class Solution:

    def check(self, mid: int, diff: List[int], r: int, k: int, n: int) -> bool:
        tempDiff = diff[:]

        cumSum = 0  # it will give power of a city at any point of time

        for i in range(n):
            cumSum += tempDiff[i]

            if cumSum < mid:
                need = mid - cumSum
                if need > k:
                    return False

                k -= need
                cumSum += need  # gredily I had chosen to add station on the city which can cover more range

                # i......X.....i+2*r
                if i + 2 * r + 1 < n:
                    tempDiff[i + 2 * r + 1] -= need  # applying difference array technique

        return True

    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)

        diff = [0] * n

        for i in range(n):
            diff[max(0, i - r)] += stations[i]

            if i + r + 1 < n:
                diff[i + r + 1] -= stations[i]

        left = min(stations)
        right = sum(stations) + k

        result = 0

        # T.C : n * log(sum)
        while left <= right:
            mid = left + (right - left) // 2

            if self.check(mid, diff, r, k, n):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.maxPower([1, 2, 4, 5, 0], 1, 2))  # 5
    print(s.maxPower([4, 4, 4, 4], 0, 3))  # 4
