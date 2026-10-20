#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=rl1TQduakTY
#     Company Tags                : Will update soon
#     Leetcode Link               : https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero

from typing import List
import math


# Approach (Binary search on answer)
# T.C : O(n * log(Tmax * mountainHeight^2), where Tmax = maximum time among all workers in the input, n = length of workerTimes
# S.C : O(1)
class Solution:
    # typedef long long ll;  (Python ints are arbitrary precision)

    def Check(self, mid: int, workerTimes: List[int], mH: int) -> bool:
        h = 0

        for t in workerTimes:
            h += int(math.sqrt(2.0 * mid / t + 0.25) - 0.5)

            if h >= mH:
                return True

        return h >= mH

    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        maxTime = max(workerTimes)
        l = 1
        r = maxTime * mountainHeight * (mountainHeight + 1) // 2

        result = 0

        while l <= r:
            mid = l + (r - l) // 2

            if self.Check(mid, workerTimes, mountainHeight):
                result = mid
                r = mid - 1
            else:
                l = mid + 1

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.minNumberOfSeconds(4, [2, 1, 1]))  # 3
    print(s.minNumberOfSeconds(10, [3, 2, 2, 4]))  # 12
    print(s.minNumberOfSeconds(5, [1]))  # 15
