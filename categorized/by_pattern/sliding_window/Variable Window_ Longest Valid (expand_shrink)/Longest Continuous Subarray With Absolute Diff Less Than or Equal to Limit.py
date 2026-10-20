from typing import List
import heapq
from bisect import insort, bisect_left

#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=xZDbcGB2PQs
#     Company Tags                : Uber
#     Leetcode Link               : https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/


# ******************************************************** C++ ****************************************************************
# Approach-1 (Using sliding window + heap)
# T.C : O(nlogn)
# S.C : O(n)
class Solution:
    # typedef pair<int, int> P;  -> tuple (value, index)
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        # heapq is a min-heap only. For C++ max priority_queue<P> we store (-value, -index)
        # so that the largest (value, index) pair comes out on top.
        maxPq = []
        minPq = []  # priority_queue<P, vector<P>, greater<P>> -> plain min-heap of (value, index)

        i = 0
        j = 0
        maxLength = 0

        while j < n:
            heapq.heappush(maxPq, (-nums[j], -j))
            heapq.heappush(minPq, (nums[j], j))

            # maxPq.top() = (-maxPq[0][0], -maxPq[0][1])
            while -maxPq[0][0] - minPq[0][0] > limit:
                i = min(-maxPq[0][1], minPq[0][1]) + 1

                while -maxPq[0][1] < i:
                    heapq.heappop(maxPq)
                while minPq[0][1] < i:
                    heapq.heappop(minPq)

            # Update maxLength with the length of the current valid window
            maxLength = max(maxLength, j - i + 1)
            j += 1

        return maxLength


Approach1 = Solution


# Approach-2 (Using sliding window + multiset)
# T.C : O(nlogn)
# S.C : O(n)
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)

        st = []  # multiset<int> -> sorted list maintained with bisect
        i = 0
        j = 0
        maxLength = 0

        while j < n:
            insort(st, nums[j])

            while st[-1] - st[0] > limit:  # *st.rbegin() - *st.begin()
                st.pop(bisect_left(st, nums[i]))  # st.erase(st.find(nums[i])) removes one occurrence
                i += 1

            maxLength = max(maxLength, j - i + 1)
            j += 1

        return maxLength


Approach2 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2):
        assert S().longestSubarray([8, 2, 4, 7], 4) == 2
        assert S().longestSubarray([10, 1, 2, 4, 7, 2], 5) == 4
        assert S().longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0) == 3
    print("All tests passed")
