from typing import List

# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=tUCVupA0lAc
# Company Tags                : Google, PhonePe, Meesho (SDE-2 Role, Year - 2025)
# Leetcode Link               : https://leetcode.com/problems/minimum-time-to-complete-trips/

# Brute Force - Simply check for each time (1, 2, 3...) if that will be able to satisfy totalTrips. This will cause TLE
# ************************************************************ Python (from C++) ************************************************************
# Approach - Using Binary Search - O(n * log(totalTrips * m)) -> where m = minimum time in the given array
# T.C : O(log(min(time) * totalTrips))
# S.C : O(1)
# (The Java version in the original file is not reproduced.)
class Solution:
    def possible(self, time: List[int], givenTime: int, totalTrips: int) -> bool:
        actualTrips = 0

        for t in time:
            actualTrips += givenTime // t

        return actualTrips >= totalTrips

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        n = len(time)

        l = 1
        r = min(time) * totalTrips  # Python ints don't overflow (C++ used long long)

        while l < r:

            mid_time = l + (r - l) // 2

            if self.possible(time, mid_time, totalTrips):
                r = mid_time
            else:
                l = mid_time + 1

        return l


if __name__ == "__main__":
    s = Solution()
    assert s.minimumTime([1, 2, 3], 5) == 3
    assert s.minimumTime([2], 1) == 2
    print("OK")
