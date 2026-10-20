# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=5Quv9nnZs34
# Company Tags                : will update soon
# Leetcode Link               : https://leetcode.com/problems/binary-subarrays-with-sum/
# Very Similar Problem        : https://github.com/MAZHARMIK/Interview_DS_Algo/blob/88b737d2c211842753dee8b6299f0e9aa690dcf9/Arrays/Subarray%20Sums%20Divisible%20by%20K%20.cpp#L74

from typing import List

# Approach-1 (Simple prefix sum) - These kind of Qns can always be solved using Map and cumulative sum technique
# T.C : O(n)
# S.C : O(n)
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)

        mp = {}  # unordered_map<int, int>

        count = 0
        currSum = 0
        mp[0] = 1
        for num in nums:

            currSum += num

            if (currSum - goal) in mp:
                count += mp[currSum - goal]

            mp[currSum] = mp.get(currSum, 0) + 1

        return count


Approach1 = Solution


# Approach-2 (Using Sliding Window)
# This could be a very easy sliding window but the presence of 0 makes it a little tricky.
# Example : [0, 0, 0, 1, 1] -> Total subarrays having goal = 2 will be 4 - {0, 0, 0, 1, 1},  {0, 0, 1, 1}, {0, 1, 1}, {1, 1}
# So, simply find the count of zeros before the sum has reached goal i.e. 3 (Now, 1+1 = goal, so total subarrays = prefix_zeros + 1 = 3 + 1 = 4)
# T.C : O(n)
# S.C : O(1)
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_zeros = 0
        window_sum = 0
        count = 0

        i = 0
        j = 0

        while j < len(nums):
            window_sum += nums[j]

            while i < j and (nums[i] == 0 or window_sum > goal):
                if nums[i] == 1:
                    prefix_zeros = 0
                else:
                    prefix_zeros += 1

                window_sum -= nums[i]
                i += 1

            if window_sum == goal:
                count += 1 + prefix_zeros
            j += 1

        return count


Approach2 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2):
        assert S().numSubarraysWithSum([1, 0, 1, 0, 1], 2) == 4
        assert S().numSubarraysWithSum([0, 0, 0, 0, 0], 0) == 15
    print("ok")
