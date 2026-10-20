# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=9L7258j-enE
# Company Tags                : META
# Leetcode Link               : https://leetcode.com/problems/number-of-flowers-in-full-bloom/

from bisect import bisect_left, bisect_right  # C++ upper_bound = bisect_right, lower_bound = bisect_left
from typing import List
# (Java section of the original is not ported: this file is the Python 3 port of the C++ code)

# ******************************************* C++ (ported to Python) *******************************************
# Approach-1 (Brute Force) - TLE
# T.C : O(m*n)
# S.C : O(1)
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        m = len(flowers)
        n = len(people)

        result = [0] * n

        for i in range(n):

            for j in range(m):
                start = flowers[j][0]
                end = flowers[j][1]

                if people[i] >= start and people[i] <= end:
                    result[i] += 1

        return result


Approach1 = Solution  # alias so both approaches can be tested below


# Approach-2 (Using Binary Search)
# T.C : O((m+n) * log(n))
# S.C : O(m)
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        m = len(flowers)
        n = len(people)

        result = [0] * n

        start_time = [0] * m
        end_time = [0] * m

        for i in range(m):
            start_time[i] = flowers[i][0]
            end_time[i] = flowers[i][1]

        start_time.sort()
        end_time.sort()

        for i in range(n):
            # NOTE : bisect_right == C++ upper_bound, bisect_left == C++ lower_bound
            bloomed_already = bisect_right(start_time, people[i])

            died_already = bisect_left(end_time, people[i])

            result[i] = bloomed_already - died_already

        return result


Approach2 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2):
        assert S().fullBloomFlowers([[1, 6], [3, 7], [9, 12], [4, 13]], [2, 3, 7, 11]) == [1, 2, 2, 2]
        assert S().fullBloomFlowers([[1, 10], [3, 3]], [3, 3, 2]) == [2, 2, 1]
    print("ok")
