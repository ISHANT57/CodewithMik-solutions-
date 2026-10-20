from typing import List
from bisect import bisect_left, bisect_right  # lower_bound / upper_bound in C++

#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=r3EnymXRC9A
#     Company Tags                : Will update soon
#     Leetcode Link               : https://leetcode.com/problems/count-the-number-of-fair-pairs


# Approach (simple binary search trick)
# T.C : O(nlogn)
# S.C : O(1)
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)

        nums.sort()  # nlogn

        result = 0

        for i in range(n):  # O(n * logn)
            # o(n)
            idx = bisect_left(nums, lower - nums[i], i + 1, n)  # Gives the firstc element NOT LESS than (lower - nums[i]) #log(n)
            x = idx - 1 - i

            idx = bisect_right(nums, upper - nums[i], i + 1, n)  # Gives the firstc element GREATER than (upper - nums[i]) #log(n)

            y = idx - 1 - i

            result += (y - x)

        return result


if __name__ == "__main__":
    print(Solution().countFairPairs([0, 1, 7, 4, 4, 5], 3, 6))  # expected 6
    print(Solution().countFairPairs([1, 7, 9, 2, 5], 11, 11))  # expected 1
