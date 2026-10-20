# MY YOUTUBE VIDEO LINK ON THIS Qn : https://www.youtube.com/watch?v=29OnjVQ-fk4
# Company Tags                     : Media.Net (Directi, 2023 repeated), Google, Zenefits, Microsoft, Zoho, Flipkart, Amazon, Directi, SAP Labs
# Leetcode Link                    : https://leetcode.com/problems/sliding-window-maximum/
# GfG Link                         : Maximum of all subarrays of size k (https://practice.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1)
#
# NOTE : Please also see hard version of this question : Leetcode-1425
# Explained Solution Link : https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/DP/Constrained%20Subsequence%20Sum.cpp
#
# Monotonic Data Structures Concepts Playlist - https://www.youtube.com/watch?v=yRyumGu_owg&list=PLpIkg8OmuX-IpUPXh3z8oeKSfRkKhjaTV

# This is generally known as "Monotonic increasing/decreasing  Queue/Dequeue"
# Approach-1 (Using Deque) Every element is added(pushed) and popped only once,So it is O(n) time complexity.
# SEE MY COMMENT IN THE VIDEO where I have explained why we can't take QUEUE to solve this.
import heapq
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        deq = deque()

        result = []

        for i in range(n):
            # remove the max elements from front which are out of window size
            while deq and deq[0] <= i - k:
                deq.popleft()

            # we maintain the deque in descending order
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

            deq.append(i)

            if i >= k - 1:  # Only when the window size first gets equal or greater than k
                result.append(nums[deq[0]])  # front will have the max element (dequeue is maintained in descending order)
        return result


Approach1 = Solution


# Approach-2 (Using max-heap (priority_queue)) (worst case :O(n*log(n)) when elements are in ascending order)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # heapq is a min-heap; C++ max priority_queue<pair<int,int>> is emulated by
        # storing (-value, -index): max value first, and for ties the larger index first (as pair comparison does)
        pq = []
        result = []

        n = len(nums)

        for i in range(n):

            # remove the max elements which are out of window size
            while pq and -pq[0][1] <= i - k:
                heapq.heappop(pq)

            heapq.heappush(pq, (-nums[i], -i))  # we will always find the max element at top

            if i >= k - 1:
                result.append(-pq[0][0])
        return result


Approach2 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2):
        assert S().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
        assert S().maxSlidingWindow([1], 1) == [1]
    print("All tests passed")
