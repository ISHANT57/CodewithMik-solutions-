#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=OVLW_XnOUQ4
#     Company Tags                : Will update soon
#     Leetcode Link               : https://leetcode.com/problems/avoid-flood-in-the-city/description/

from typing import List
import bisect  # used in place of C++ std::set (sorted list + bisect_left as lower_bound)


# Approach (Binary search along with map and set and greedy)
# T.C : O(n*logn)
# S.C : O(n)
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)

        map = {}  # lake -> last day it was filled
        dryDays = []  # indices of dry days (rains[day] == 0), kept sorted (set<int> equivalent)
        ans = [1] * n  # default all dry days to dry lake 1

        for day in range(n):
            lake = rains[day]

            if lake == 0:
                dryDays.append(day)  # record this dry day (days come in increasing order, so list stays sorted)
            else:
                ans[day] = -1  # raining day — can't dry any lake

                if lake in map:
                    # lake already filled previously
                    it = bisect.bisect_left(dryDays, map[lake] + 1)  # next dry day after it was last filled

                    if it == len(dryDays):
                        # no dry day available to empty this lake before raining again → flood
                        return []

                    ans[dryDays[it]] = lake  # use this dry day to dry the lake
                    del dryDays[it]

                map[lake] = day  # record latest day this lake was filled

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.avoidFlood([1, 2, 3, 4]))  # [-1,-1,-1,-1]
    print(s.avoidFlood([1, 2, 0, 0, 2, 1]))  # [-1,-1,2,1,-1,-1]
    print(s.avoidFlood([1, 2, 0, 1, 2]))  # []
