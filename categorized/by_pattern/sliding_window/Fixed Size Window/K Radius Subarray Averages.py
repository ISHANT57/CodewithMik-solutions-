from typing import List

#       MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=M_YXCATc4ro
#       Company Tags                : AMAZON
#       Leetcode Link               : https://leetcode.com/problems/k-radius-subarray-averages/

# My Approach-2 using Prefix Array is in Array/Cumulative_Sum(Prefix Array) folder Folde. Link below -
# Link - https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Arrays/Cumulative_Sum(Prefix%20Array)/K%20Radius%20Subarray%20Averages.cpp


# Approach-1 : Using Sliding Window
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        if k == 0:
            return nums

        result = [-1] * n

        if n < 2 * k + 1:
            return result

        windowSum = 0  # long long (Python ints do not overflow)

        left = 0
        right = 2 * k
        i = k

        for idx in range(left, right + 1):
            windowSum += nums[idx]

        result[i] = windowSum // (2 * k + 1)

        i += 1
        right += 1  # Shifting window

        while right < n:

            out_of_window = nums[left]
            came_to_window = nums[right]

            windowSum = windowSum - out_of_window + came_to_window

            result[i] = windowSum // (2 * k + 1)
            i += 1
            left += 1
            right += 1

        return result


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().getAverages([7, 4, 3, 9, 1, 8, 5, 2, 6], 3) == [-1, -1, -1, 5, 4, 4, -1, -1, -1]
    assert Solution().getAverages([100000], 0) == [100000]
    assert Solution().getAverages([8], 100000) == [-1]
    print("All tests passed")
