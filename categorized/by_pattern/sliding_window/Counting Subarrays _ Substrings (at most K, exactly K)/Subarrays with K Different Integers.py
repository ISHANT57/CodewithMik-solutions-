# MY YOUTUBE VIDEO ON THIS Qn : Approach-1 -- https://www.youtube.com/watch?v=uJJSGxfzix8
#                               Approach-2 -- https://www.youtube.com/watch?v=0Kmbzm5nKqw
# Company Tags                : Amazon
# Leetcode Link               : https://leetcode.com/problems/subarrays-with-k-different-integers/

# Approach-1 (Standard Sliding Window twice - A very good Pattern of Sliding Window Problems)
# T.C : O(n)
# S.C : O(n)
from collections import defaultdict
from typing import List


class Solution:

    # Total count of subarrays having <= k distict elements
    def slidingWindow(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)  # unordered_map<int, int>

        n = len(nums)
        i = 0
        j = 0

        count = 0

        while j < n:

            mp[nums[j]] += 1

            while len(mp) > k:
                # shrink the window
                mp[nums[i]] -= 1
                if mp[nums[i]] == 0:
                    del mp[nums[i]]
                i += 1

            count += (j - i + 1)  # ending at j
            j += 1

        return count

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.slidingWindow(nums, k) - self.slidingWindow(nums, k - 1)


Approach1 = Solution


# Approach-2 (One Pass Flow)
# T.C : O(n)
# S.C : O(n)
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)

        mp = defaultdict(int)  # unordered_map<int, int>

        i_chota = 0
        j = 0
        i_bada = 0

        result = 0

        while j < n:
            mp[nums[j]] += 1

            while len(mp) > k:
                mp[nums[i_chota]] -= 1
                if mp[nums[i_chota]] == 0:
                    del mp[nums[i_chota]]
                i_chota += 1
                i_bada = i_chota

            while mp[nums[i_chota]] > 1:
                mp[nums[i_chota]] -= 1
                i_chota += 1

            if len(mp) == k:
                result += i_chota - i_bada + 1
            j += 1

        return result


Approach2 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2):
        assert S().subarraysWithKDistinct([1, 2, 1, 2, 3], 2) == 7
        assert S().subarraysWithKDistinct([1, 2, 1, 3, 4], 3) == 3
    print("All tests passed")
