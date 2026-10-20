# Company Tags  : Adobe
# Leetcode Link : https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/
#
# It's a premium question :
# Given a binary array data, return the minimum number of swaps required to group all 1's present in the array together in any place in the array.
#
#
# Example 1:
# Input: [1,0,1,0,1]
# Output: 1
# Explanation:
# There are 3 ways to group all 1's together:
# [1,1,1,0,0] using 1 swap
# [0,1,1,1,0] using 2 swaps
# [0,0,1,1,1] using 1 swap
# The minimum is 1.

# Solution with explanation:
# Keywords : Minimum swaps, together  (Hints towards Sliding Window Technique)
#
# To group all 1's together, we need a window of size equal to total number of 1's in it.
# Let, x = total no. of 1's in the array
# Now, Check for every window of size x
# We want a window which has maximum 1's so that we can swap minimum 0's (in that window) with 1's to get all 1's together
# In other words, we want a window with minimum 0's and then swap them.
# So, keep track of # 0's in every window of size x and find the minimum # 0's. That will be the minimum # swaps required.

from typing import List


# NOTE: the original C++ was broken (parameter is `data` but body uses undeclared
# `arr` and `n`); here `arr = data` and `n = len(arr)` are added, logic unchanged.
class Solution:
    def totalOnes(self, arr: List[int]) -> int:
        count = 0
        for i in range(len(arr)):
            if arr[i] == 1:
                count += 1
        return count

    def minSwaps(self, data: List[int]) -> int:
        arr = data
        n = len(arr)
        if n == 1:
            return 0 if arr[0] == 1 else -1
        windowSize = self.totalOnes(arr)

        # if there is no 1's , it's not possible
        if windowSize == 0: return -1

        # count 0's in first window size
        zeros = 0
        for i in range(windowSize):
            if arr[i] == 0:
                zeros += 1

        minZeros = zeros

        # find minimum 0's in otehr windows
        i, j = 1, windowSize
        while j < n:
            if arr[i - 1] == 0:
                zeros -= 1
            if arr[j] == 0:
                zeros += 1
            minZeros = min(minZeros, zeros)
            j += 1
            i += 1
        return minZeros


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().minSwaps([1, 0, 1, 0, 1]) == 1
    assert Solution().minSwaps([0, 0, 0, 1, 0]) == 0
    assert Solution().minSwaps([1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1]) == 3
    print("all tests passed")
