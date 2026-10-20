# MY YOUTUBE VIDEO ON THIS Qn        : https://www.youtube.com/watch?v=AyiGBwFlMb8
# Company Tags                       : Airbnb, Palantir Technologies
# Leetcode Link                      : https://leetcode.com/problems/contains-duplicate-ii/
# Using Map (without sliding window) : https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Arrays/Contains%20Duplicate%20II.cpp

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        st = set()

        i = 0
        j = 0

        while j < n:

            # step-1
            if abs(i - j) > k:  # abs(i-j) <= k
                st.discard(nums[i])
                i += 1  # shrink

            # past me dekha hai nums[j] ?
            if nums[j] in st:
                return True

            st.add(nums[j])
            j += 1

        return False


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().containsNearbyDuplicate([1, 2, 3, 1], 3) is True
    assert Solution().containsNearbyDuplicate([1, 0, 1, 1], 1) is True
    assert Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) is False
    print("ok")
