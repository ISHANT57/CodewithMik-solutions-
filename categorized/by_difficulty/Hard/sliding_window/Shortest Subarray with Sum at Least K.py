# MY YOUTUBE VIDEO ON THIS Qn   : https://www.youtube.com/watch?v=Z4tH40wH6JA
# Company Tags                  : Will update soon
# Leetcode Link                 : https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k
# Similar Easy Version Problem  : https://www.youtube.com/watch?v=D2MbogiFXWU
#
# Monotonic Data Structures Concepts Playlist - https://www.youtube.com/watch?v=yRyumGu_owg&list=PLpIkg8OmuX-IpUPXh3z8oeKSfRkKhjaTV

# Approach (Using sliding window + monotinic deque
# T.C : O(n)
# S.C : O(n)
from collections import deque
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], K: int) -> int:
        N = len(nums)

        deq = deque()
        cumulativeSum = [0] * N  # This stores the cumulative sum

        result = 2**31 - 1  # INT_MAX
        j = 0

        # Compute cumulative sum in the cumulativeSum array using while loop
        while j < N:
            if j == 0:
                cumulativeSum[j] = nums[j]
            else:
                cumulativeSum[j] = cumulativeSum[j - 1] + nums[j]

            # If the cumulative sum from the start to j is already >= K, update result
            if cumulativeSum[j] >= K:
                result = min(result, j + 1)

            # Remove indices from the deque where the subarray sum is >= K
            while deq and cumulativeSum[j] - cumulativeSum[deq[0]] >= K:
                result = min(result, j - deq[0])  # Calculate the length of the subarray
                deq.popleft()  # Remove the front index from the deque

            # Maintain the monotonic property of the deque (increasing order of cumulative sums)
            while deq and cumulativeSum[j] <= cumulativeSum[deq[-1]]:
                deq.pop()  # Remove indices that won't be useful

            # Add the current index to the deque
            deq.append(j)

            j += 1  # Increment j to move to the next index

        # Return the result if we found a valid subarray, otherwise return -1
        return -1 if result == 2**31 - 1 else result


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().shortestSubarray([1], 1) == 1
    assert Solution().shortestSubarray([1, 2], 4) == -1
    assert Solution().shortestSubarray([2, -1, 2], 3) == 3
    print("All tests passed")
