# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=V7ZmYjVdZSU
# Company Tag                 : will update later
# Leetcode Link               : https://leetcode.com/problems/maximum-erasure-value/

from typing import List

# Approach-1 (Sliding Window)
# T.C : O(n)
# S.C : O(n)
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        st = set()

        i = 0
        j = 0
        sum = 0
        result = 0

        while j < n:
            if nums[j] not in st:
                sum += nums[j]
                result = max(result, sum)
                st.add(nums[j])
                j += 1
            else:
                while i < n and nums[j] in st:
                    sum -= nums[i]
                    st.discard(nums[i])
                    i += 1

        return result


Approach1 = Solution


# Approach-2 (Using cumulative sum to find subarray sum)
# T.C : O(n)
# S.C : O(n)
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        cus = [0] * n
        cus[0] = nums[0]
        for i in range(1, n):
            cus[i] = cus[i - 1] + nums[i]

        mp = [-1] * 10001  # Using as a map 1 <= nums[i] <= 10^4
        maxS = 0
        i = 0
        j = 0

        while j < n:
            i = max(i, mp[nums[j]] + 1)
            jthSum = cus[j]
            ithSum = 0 if i - 1 < 0 else cus[i - 1]
            maxS = max(maxS, jthSum - ithSum)
            mp[nums[j]] = j

            j += 1

        return maxS


Approach2 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2):
        assert S().maximumUniqueSubarray([4, 2, 4, 5, 6]) == 17
        assert S().maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5]) == 8
    print("ok")
