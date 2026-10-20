# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=bO39iLSqvQY
# Company Tags                : will update soon
# Leetcode Link               : https://leetcode.com/problems/count-the-number-of-good-subarrays

from typing import List
from collections import defaultdict


# Approach-1 (Sliding Window)
# T.C : O(n)
# S.C : O(n)
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = 0
        j = 0

        result = 0

        mp = defaultdict(int)

        pairs = 0

        while j < n:
            pairs += mp[nums[j]]  # isse pehle kitni baar nums[j] dekha hai humne
            mp[nums[j]] += 1

            while pairs >= k:
                result += (n - j)
                mp[nums[i]] -= 1
                pairs -= mp[nums[i]]
                i += 1

            j += 1

        return result


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().countGood([1, 1, 1, 1, 1], 10) == 1
    assert Solution().countGood([3, 1, 4, 3, 2, 2, 4], 2) == 4
    print("ok")
