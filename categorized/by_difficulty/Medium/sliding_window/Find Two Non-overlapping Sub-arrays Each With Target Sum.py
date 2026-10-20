# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=OozgrdhmWWA
# Company Tag                 : will update later
# Leetcode Link               : https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum

from typing import List


# Approach (Sliding Window)
# T.C : O(n)
# S.C : O(n)
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        INT_MAX = 2**31 - 1
        n = len(arr)

        i = 0
        j = 0

        currSum = 0
        minBestLenTillIdx = [INT_MAX] * n

        bestMinLen = INT_MAX
        result = INT_MAX

        while j < n:
            currSum += arr[j]

            while i < j and currSum > target:
                currSum -= arr[i]
                i += 1

            if currSum == target:
                len_ = j - i + 1

                if i > 0 and minBestLenTillIdx[i - 1] != INT_MAX:
                    result = min(result, len_ + minBestLenTillIdx[i - 1])

                bestMinLen = min(bestMinLen, len_)

            minBestLenTillIdx[j] = bestMinLen
            j += 1

        return -1 if result == INT_MAX else result


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().minSumOfLengths([3, 2, 2, 4, 3], 3) == 2
    assert Solution().minSumOfLengths([7, 3, 4, 7], 7) == 2
    assert Solution().minSumOfLengths([4, 3, 2, 6, 2, 3, 4], 6) == -1
    print("ok")
