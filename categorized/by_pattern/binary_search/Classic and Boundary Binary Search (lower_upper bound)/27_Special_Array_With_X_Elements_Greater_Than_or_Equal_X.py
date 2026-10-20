from typing import List
from bisect import bisect_left  # lower_bound in C++

#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=pYqncHGUqh4
#     Company Tags                : AMAZON
#     Leetcode Link               : https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x


# Approach-1 (Using binary search)
# T.C : O(n*logn)
# S.C : O(1)
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        for x in range(0, n + 1):

            i = bisect_left(nums, x)  # lower_bound

            if n - i == x:
                return x

        return -1


# Approach-2 (Binary search on answer)
# T.C : O(nlogn)
# S.C : O(1)
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        l, r = 0, n
        while l <= r:
            mid_x = l + (r - l) // 2

            i = bisect_left(nums, mid_x)  # lower_bound

            if n - i == mid_x:
                return mid_x
            elif n - i > mid_x:
                l = mid_x + 1
            else:
                r = mid_x - 1

        return -1


# Approach-3 (Using counting Sort + Prefix Sum)
# T.C : O(n)
# S.C : O(n)
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)

        """
            Every number larger than N is useless for our purpose,
            and we can treat those numbers as N.
        """
        freq = [0] * (n + 1)

        for i in range(n):
            freq[min(n, nums[i])] += 1

        c_sum = 0
        for i in range(n, -1, -1):
            c_sum += freq[i]
            if i == c_sum:
                return i

        return -1


if __name__ == "__main__":
    print(Solution().specialArray([3, 5]))        # expected 2
    print(Solution().specialArray([0, 0]))        # expected -1
    print(Solution().specialArray([0, 4, 3, 0, 4]))  # expected 3
