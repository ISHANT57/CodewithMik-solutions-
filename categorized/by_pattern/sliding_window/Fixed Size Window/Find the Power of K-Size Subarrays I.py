# MY YOUTUBE VIDEO ON THIS Qn : Approach-1 : https://www.youtube.com/watch?v=P1_yXMhqC50
#                               Approach-2 : https://www.youtube.com/watch?v=7xkCA80h5a4
# Company Tags                : Will update soon
# Leetcode Link               : https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i
#
# Monotonic Data Structures Concepts Playlist - https://www.youtube.com/watch?v=yRyumGu_owg&list=PLpIkg8OmuX-IpUPXh3z8oeKSfRkKhjaTV

from typing import List
from collections import deque


# Approach-1 (Using sliding window)
# T.C : O(n)
# S.C : O(1)
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        result = [-1] * (n - k + 1)

        count = 1  # count of consecutive elements

        # preprocess the first window
        for i in range(1, k):
            if nums[i] == nums[i - 1] + 1:
                count += 1
            else:
                count = 1

        if count == k:
            result[0] = nums[k - 1]

        i = 1
        j = k

        while j < n:
            if nums[j] == nums[j - 1] + 1:
                count += 1
            else:
                count = 1

            if count >= k:
                result[i] = nums[j]

            i += 1
            j += 1

        return result


Approach1 = Solution


# Approach-2 (Using monotonic deque)
# T.C : O(n)
# S.C : O(n)
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        deq = deque()  # Monotonic deque
        result = []

        for j in range(n):

            if len(deq) == k:
                deq.popleft()  # deq ka size ab k-1, ab jth element ko hum insert karne ka soch sakte hain deque me

            if deq and deq[-1] != nums[j] - 1:  # nums[j] is not consecutive to deq.back() element
                deq.clear()

            deq.append(nums[j])

            if j >= k - 1:
                if len(deq) == k:
                    result.append(deq[-1])  # max element hoga becau monotonic hai
                else:
                    result.append(-1)  # else -1

        return result


Approach2 = Solution


if __name__ == "__main__":
    for A in (Approach1, Approach2):
        assert A().resultsArray([1, 2, 3, 4, 3, 2, 5], 3) == [3, 4, -1, -1, -1]
        assert A().resultsArray([2, 2, 2, 2, 2], 4) == [-1, -1]
        assert A().resultsArray([3, 2, 3, 2, 3, 2], 2) == [-1, 3, -1, 3, -1]
    print("ok")
