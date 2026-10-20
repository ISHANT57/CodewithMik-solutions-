# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=yOZSUfL-DxQ
# Company Tags                : Will update soon
# Leetcode Link               : https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted

from typing import List


# Approach (simple two pointer approach)
# T.C : O(n) - We don't visit any element once inside the while loop
# S.C : O(1)
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        # step-1 - Find the jth pointer from right side
        j = n - 1
        while j > 0 and arr[j] >= arr[j - 1]:
            j -= 1

        i = 0
        result = j  # we are removing all elements left to index j  becasue index j to n-1 are sorted

        # step-2 start finding correct i and j and find deleted elements = j - i - 1
        while i < j and (i == 0 or arr[i] >= arr[i - 1]):  # increasing ordere of elements from i

            # arr[j] < arr[i]
            while j < n and arr[i] > arr[j]:
                j += 1

            # we have found correct jth element such that arr[i] <= arr[j]
            result = min(result, j - i - 1)
            i += 1

        return result


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().findLengthOfShortestSubarray([1, 2, 3, 10, 4, 2, 3, 5]) == 3
    assert Solution().findLengthOfShortestSubarray([5, 4, 3, 2, 1]) == 4
    assert Solution().findLengthOfShortestSubarray([1, 2, 3]) == 0
    print("ok")
