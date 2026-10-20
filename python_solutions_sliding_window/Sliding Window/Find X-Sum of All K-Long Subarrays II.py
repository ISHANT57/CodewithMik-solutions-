# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=ZyE1zCe_gSQ
# Company Tag                 : will update later
# Leetcode Link               : https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/

from typing import List
from bisect import insort, bisect_left
from collections import defaultdict


# Approach (Sliding Window using map)
# T.C : O(nlogn)
# S.C : O(k)
class Solution:
    # std::set<pair<int,int>> is emulated with a sorted Python list of (freq, element) tuples
    # (insort = insert, bisect_left + pop = erase/find, [0] = begin(), [-1] = rbegin()).
    def __init__(self):
        self.sum = 0  # maintains sum of top x elements from main set
        self.main = []  # contains top-x freq, elements   (sorted list acting as set)
        self.sec = []  # contains remaining freq, elements (sorted list acting as set)

    def _find(self, lst, p):
        pos = bisect_left(lst, p)
        return pos < len(lst) and lst[pos] == p

    def _erase(self, lst, p):
        pos = bisect_left(lst, p)
        if pos < len(lst) and lst[pos] == p:
            lst.pop(pos)

    def insertInSet(self, p, x: int) -> None:
        if len(self.main) < x or p > self.main[0]:
            self.sum += p[0] * p[1]
            insort(self.main, p)

            if len(self.main) > x:
                smallest = self.main[0]
                self.sum -= smallest[0] * smallest[1]
                self._erase(self.main, smallest)
                insort(self.sec, smallest)
        else:
            insort(self.sec, p)

    def removeFromSet(self, p, x: int) -> None:
        if self._find(self.main, p):
            self.sum -= p[0] * p[1]
            self._erase(self.main, p)

            if self.sec:
                largest = self.sec[-1]
                self._erase(self.sec, largest)
                insort(self.main, largest)
                self.sum += largest[0] * largest[1]
        else:
            self._erase(self.sec, p)

    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        self.sum = 0
        self.main = []
        self.sec = []

        result = []

        mp = defaultdict(int)  # element -> freq

        i = 0
        j = 0
        while j < n:
            if mp[nums[j]] > 0:
                self.removeFromSet((mp[nums[j]], nums[j]), x)

            mp[nums[j]] += 1  # new freq
            self.insertInSet((mp[nums[j]], nums[j]), x)

            if j - i + 1 == k:
                result.append(self.sum)

                self.removeFromSet((mp[nums[i]], nums[i]), x)
                mp[nums[i]] -= 1
                if mp[nums[i]] == 0:
                    del mp[nums[i]]
                else:
                    self.insertInSet((mp[nums[i]], nums[i]), x)
                i += 1

            j += 1

        return result


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().findXSum([1, 1, 2, 2, 3, 4, 2, 3], 6, 2) == [6, 10, 12]
    assert Solution().findXSum([3, 8, 7, 8, 7, 5], 2, 2) == [11, 15, 15, 15, 12]
    print("ok")
