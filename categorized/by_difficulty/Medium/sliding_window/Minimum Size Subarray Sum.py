# Scroll below to see JAVA code also (Java section skipped in this Python port)
# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=D2MbogiFXWU
# Company Tags                : Google, Accolite, Amazon, Facebook, Goldman Sachs
# Leetcode Link               : https://leetcode.com/problems/minimum-size-subarray-sum/
# Similar GfG Link            : https://practice.geeksforgeeks.org/problems/smallest-subarray-with-sum-greater-than-x5651/1
# Similar Hard Version        : https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Sliding%20Window/Shortest%20Subarray%20with%20Sum%20at%20Least%20K.cpp

from typing import List


# Approach - Using Sliding Window
# T.C : O(n)
# S.C : O(1)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        i, j = 0, 0

        sum = 0
        minL = n + 1

        while j < n:
            sum += nums[j]

            while sum >= target:
                minL = min(minL, j - i + 1)
                sum -= nums[i]
                i += 1

            j += 1
        return 0 if minL == n + 1 else minL


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
    assert Solution().minSubArrayLen(4, [1, 4, 4]) == 1
    assert Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
    print("all tests passed")
