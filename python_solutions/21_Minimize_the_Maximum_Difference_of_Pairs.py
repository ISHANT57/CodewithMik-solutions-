# SCROLL BELOW TO SEE JAVA CODE AS WELL (Java section not ported: this file is the Python 3 port of the C++ code)
# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=OsG2i00LXFc
# Company Tags                : META
# Leetcode Link               : https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/
# Similar Qn                  : https://www.youtube.com/watch?v=lWU1wI7koGk

from typing import List

INT_MAX = 2**31 - 1


# ************************************************************************ C++ (ported to Python) ******************************************************************
# Binary Search + Greedy (This is the same Qn of pattern "Applying binary search on answer" (Time Compplexity - O(m * log(n)) where m = max diff in pair
# How to identify -> Notice the keywords - "min max"
#
#     Whenever we see in Question to Find Min(Max) or Max(Min)
#     we will try to use Binary search on the result
#
# T.C : O(nlogn)
# S.c : O(1)
class Solution:

    def isValid(self, nums: List[int], mid: int, p: int) -> bool:

        n = self.n
        i = 0
        pairs = 0
        while i < n - 1:

            if nums[i + 1] - nums[i] <= mid:
                pairs += 1
                i += 2
            else:
                i += 1

        return pairs >= p

    def minimizeMax(self, nums: List[int], p: int) -> int:
        self.n = len(nums)
        n = self.n

        nums.sort()

        l = 0
        r = nums[n - 1] - nums[0]

        result = INT_MAX

        while l <= r:

            mid = l + (r - l) // 2

            if self.isValid(nums, mid, p):
                result = mid
                r = mid - 1
            else:
                l = mid + 1

        return result


if __name__ == "__main__":
    s = Solution()
    assert s.minimizeMax([10, 1, 2, 7, 1, 3], 2) == 1
    assert s.minimizeMax([4, 2, 1, 2], 1) == 0
    print("ok")
