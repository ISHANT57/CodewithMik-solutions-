# Scroll below to see JAVA code also (Java section not ported: this file is the Python 3 port of the C++ code)
# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=CdqZNsvVSS4
# Company Tags                : GOOGLE
# Leetcode Link               : https://leetcode.com/problems/maximum-running-time-of-n-computers/

from typing import List


# ****************************************************************** C++ (ported to Python) ******************************************************************
# Approach-1 (Using Linesr search from minute = max_limit till minute = 1 -- TLE
# T.C : O(m*k)
# S.C : O(1)
class Solution:

    def possible(self, batteries: List[int], time: int, n: int) -> bool:
        target = n * time

        for b in batteries:
            target -= min(b, time)
            if target <= 0:
                return True
        return False

    def maxRunTime(self, n: int, batteries: List[int]) -> int:

        sum = 0
        for b in batteries:
            sum += b

        # Max possible minutes if evenly distributed
        maxMinutes = sum // n

        # Linear search: from max -> 1
        for t in range(maxMinutes, 0, -1):
            if self.possible(batteries, t, n):
                return t
        return 0


Approach1 = Solution  # alias so both approaches can be tested below


# Approach-2 (Using Binary Search on the result minutes) . T.C. : O(m*logk) - m = input array length and k = range of minutes
# T.C : O(m*log(k))
# S.C : O(1)
class Solution:

    def possible(self, batteries: List[int], mid_time: int, n: int) -> bool:

        target = n * mid_time  # each computer will run mid_time minutes

        sum = 0

        for i in range(len(batteries)):

            target -= min(batteries[i], mid_time)

            if target <= 0:
                return True

        return target <= 0

    def maxRunTime(self, n: int, batteries: List[int]) -> int:

        l = min(batteries)

        sum_total_minutes = 0

        for mints in batteries:
            sum_total_minutes += mints

        r = sum_total_minutes // n

        result = 0

        while l <= r:

            mid_time = l + (r - l) // 2

            if self.possible(batteries, mid_time, n):
                result = mid_time
                l = mid_time + 1
            else:
                r = mid_time - 1

        return result


Approach2 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2):
        assert S().maxRunTime(2, [3, 3, 3]) == 4
        assert S().maxRunTime(2, [1, 1, 1, 1]) == 2
    print("ok")
