# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=hnj5JrPVqZk
# Company Tag                 : will update later
# Leetcode Link               : https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii

from typing import List
from bisect import insort, bisect_left


# Approach (Sliding Window using ordered sets)
# T.C : O(n * log(k)), set operations are logarithmic
# S.C : O(k), set stores (k-1) elements
class Solution:
    # std::set<pair> is emulated with a sorted Python list of (value, index) tuples
    # (bisect.insort for insert, bisect_left + pop for erase, [-1] == rbegin, [0] == begin)
    # Note: the list insert/erase is O(size) but the structure and logic is same as set.
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)

        kMinimum = []  # stores (k-1) minimum elements (sorted list of (val, idx))
        remaining = []

        def erase(lst, p):
            pos = bisect_left(lst, p)
            if pos < len(lst) and lst[pos] == p:
                lst.pop(pos)

        def count(lst, p):
            pos = bisect_left(lst, p)
            return 1 if pos < len(lst) and lst[pos] == p else 0

        sum_ = 0  # stores sum of (k-1) min elements

        i = 1
        while i - dist < 1:
            insort(kMinimum, (nums[i], i))
            sum_ += nums[i]
            if len(kMinimum) > k - 1:
                temp = kMinimum[-1]
                sum_ -= temp[0]
                insort(remaining, temp)
                erase(kMinimum, temp)
            i += 1

        result = 2**63 - 1  # LONG_MAX; stores min sum of (k-1) elements
        # 0, 1, ...... i
        while i < n:
            insort(kMinimum, (nums[i], i))
            sum_ += nums[i]

            if len(kMinimum) > k - 1:
                temp = kMinimum[-1]
                sum_ -= temp[0]
                insort(remaining, temp)
                erase(kMinimum, temp)

            result = min(result, sum_)

            # shift window
            # i-dist wala element will be removed
            remove = (nums[i - dist], i - dist)
            if count(kMinimum, remove):
                erase(kMinimum, remove)
                sum_ -= remove[0]

                if remaining:
                    temp = remaining[0]
                    insort(kMinimum, temp)
                    sum_ += temp[0]
                    erase(remaining, temp)
            else:
                erase(remaining, remove)

            i += 1

        return nums[0] + result


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().minimumCost([1, 3, 2, 6, 4, 2], 3, 3) == 5
    assert Solution().minimumCost([10, 1, 2, 2, 2, 1], 4, 3) == 15
    assert Solution().minimumCost([10, 8, 18, 9], 3, 1) == 36
    print("ok")
