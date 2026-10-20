# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=t8kDspIQyFQ
# Company Tags                : will update soon
# Leetcode Link               : https://leetcode.com/problems/count-complete-subarrays-in-an-array/

from typing import List

# Approach  (Sliding Window)
# T.C : O(n)
# S.C : O(n)
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        st = set(nums)

        c = len(st)

        i = 0
        j = 0
        res = 0

        mp = {}  # unordered_map<int, int>
        while j < n:
            mp[nums[j]] = mp.get(nums[j], 0) + 1

            while len(mp) == c:
                res += (n - j)

                mp[nums[i]] -= 1
                if mp[nums[i]] == 0:
                    del mp[nums[i]]
                i += 1

            j += 1

        return res


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().countCompleteSubarrays([1, 3, 1, 2, 2]) == 4
    assert Solution().countCompleteSubarrays([5, 5, 5, 5]) == 10
    print("ok")
