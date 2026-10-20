# MY YOUTUBE VIDEO ON THIS Qn   : https://www.youtube.com/watch?v=SWyGD8w_85E
# Company Tags                  : Will update soon
# Leetcode Link                 : https://leetcode.com/problems/continuous-subarrays

import heapq
from typing import List

# Approach-1 (Using Ordered Map)
# T.C : ~O(n) - Explained in the video why O(n) ?
# S.C : ~O(1) - Explained in the video why O(1) ?
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        # map<int, int> (ordered): emulated with dict; min/max keys found via min()/max()
        # (the window holds at most 3 distinct keys, so this is O(1))
        mp = {}

        i = 0
        j = 0

        count = 0

        while j < n:
            mp[nums[j]] = mp.get(nums[j], 0) + 1

            while abs(max(mp) - min(mp)) > 2:  # it means it is out of the bound
                # shrink window -move i index
                mp[nums[i]] -= 1
                if mp[nums[i]] == 0:
                    del mp[nums[i]]
                i += 1

            count += j - i + 1
            j += 1

        return count


Approach1 = Solution


# Approach-2 (Using Ordered Map)
# T.C : O(nlogn)
# S.C : O(n)
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        # heapq is a min-heap. maxHeap stores (-value, -index) so that
        # pop order matches C++ priority_queue<pair> (max by value, then by index).
        minHeap = []  # entries: (value, index)
        maxHeap = []  # entries: (-value, -index)

        i = 0
        j = 0
        count = 0

        while j < n:  # O(n)
            heapq.heappush(minHeap, (nums[j], j))  # Log(n)
            heapq.heappush(maxHeap, (-nums[j], -j))  # Log(n)

            while abs(-maxHeap[0][0] - minHeap[0][0]) > 2:
                i += 1

                while maxHeap and -maxHeap[0][1] < i:
                    heapq.heappop(maxHeap)

                while minHeap and minHeap[0][1] < i:
                    heapq.heappop(minHeap)

            count += j - i + 1
            j += 1
        # T.C: O(nlogn)
        return count


Approach2 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2):
        assert S().continuousSubarrays([5, 4, 2, 4]) == 8
        assert S().continuousSubarrays([1, 2, 3]) == 6
    print("ok")
