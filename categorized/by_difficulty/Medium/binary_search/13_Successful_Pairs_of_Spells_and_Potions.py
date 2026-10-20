from typing import List
import bisect  # used only in Approach-1 (C++ lower_bound)
import math

# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=QZI4TCVckpA
# Company Tags                : MICROSOFT
# Leetcode Link               : https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
# (The Java version in the original file is not reproduced.)


# ****************************************************************** Python (from C++) ******************************************************************
# Approach-1 : Using lower_bound STL  -> bisect.bisect_left
# T.C : O(nlogn)
# S.C : O(1)
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        m = len(spells)

        n = len(potions)

        potions.sort()

        maxPotion = potions[n - 1]

        answer = []

        for i in range(m):

            spell = spells[i]

            minPotion = math.ceil((1.0 * success) / spell)

            if minPotion > maxPotion:
                answer.append(0)
                continue

            index = bisect.bisect_left(potions, minPotion)

            answer.append(n - index)

        return answer


Approach1 = Solution


# Approach-2 : Using self written Binary Search for lower bound
# T.C : O(nlogn)
# S.C : O(1)
class Solution:

    def BinarySearch(self, l: int, r: int, potions: List[int], target: int) -> int:

        # we have to find the index of first element greater than or equal to target (minPotion)

        index = -1
        mid = 0

        while l <= r:

            mid = l + (r - l) // 2

            if potions[mid] >= target:
                index = mid
                r = mid - 1
            else:
                l = mid + 1

        return index

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        m = len(spells)

        n = len(potions)

        potions.sort()

        maxPotion = potions[n - 1]

        answer = []

        for i in range(m):

            spell = spells[i]

            minPotion = math.ceil((1.0 * success) / spell)

            if minPotion > maxPotion:
                answer.append(0)
                continue

            index = self.BinarySearch(0, n - 1, potions, minPotion)  # lower_bound(begin(potions), end(potions), minPotion) - begin(potions);

            answer.append(n - index)

        return answer


Approach2 = Solution

# Approach-3 (Using 2 pointers - It will be posted in Two Pointer sub-repository)
# Two Pointer Sub-repo - https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Arrays/Two%20Pointer/Successful%20Pairs%20of%20Spells%20and%20Potions.cpp


if __name__ == "__main__":
    for sol in (Approach1(), Approach2()):
        assert sol.successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7) == [4, 0, 3]
        assert sol.successfulPairs([3, 1, 2], [8, 5, 8], 16) == [2, 0, 2]
    print("OK")
