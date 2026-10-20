# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=JPWBTUyGCnM
# Company Tags                : will update soon
# Leetcode Link               : https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i

# Approach  (Sliding Window)
# T.C : O(n)
# S.C : O(k)
from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        freeArray = []  # store durations of free gaps

        # ith event
        # ith start - i-1th ka end = free gap duration
        freeArray.append(startTime[0])

        for i in range(1, len(startTime)):
            freeArray.append(startTime[i] - endTime[i - 1])

        freeArray.append(eventTime - endTime[len(endTime) - 1])

        # Khandani sliding window

        i = 0
        j = 0
        maxSum = 0
        currSum = 0

        n = len(freeArray)
        while j < n:
            currSum += freeArray[j]

            if i < n and j - i + 1 > k + 1:
                currSum -= freeArray[i]
                i += 1

            maxSum = max(maxSum, currSum)
            j += 1

        return maxSum


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().maxFreeTime(5, 1, [1, 3], [2, 5]) == 2
    assert Solution().maxFreeTime(10, 1, [0, 2, 9], [1, 4, 10]) == 6
    assert Solution().maxFreeTime(5, 2, [0, 1, 2, 3, 4], [1, 2, 3, 4, 5]) == 0
    print("All tests passed")
