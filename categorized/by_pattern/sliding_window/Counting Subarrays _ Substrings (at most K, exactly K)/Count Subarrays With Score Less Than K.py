# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=wxd3SWgzoKA
# Company Tags                : will update soon
# Leetcode Link               : https://leetcode.com/problems/count-subarrays-with-score-less-than-k

from typing import List

# Approach  (Sliding Window)
# T.C : O(n)
# S.C : O(1)
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        result = 0
        sum = 0

        i = 0
        j = 0

        while j < n:
            sum += nums[j]

            while i <= j and sum * (j - i + 1) >= k:  # shrink the window
                sum -= nums[i]
                i += 1

            # i...j
            # i+1...j
            # i+2...j
            result += (j - i + 1)
            j += 1

        return result


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().countSubarrays([2, 1, 4, 3, 5], 10) == 6
    assert Solution().countSubarrays([1, 1, 1], 5) == 5
    print("ok")
