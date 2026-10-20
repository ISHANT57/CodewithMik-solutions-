# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=bvfBnQo5qiY
# Company Tags                : Will update soon
# Leetcode Link               : https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i

from typing import List
import heapq

INT_MAX = 2**31 - 1


# Approach (Using Dijkstra's Algorithm)
# T.C : O(mn log(mn))
# S.C : O(mn)
class Solution:
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    # {t, {i, j}} -> tuple (t, (i, j))

    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m = len(moveTime)
        n = len(moveTime[0])

        result = [[INT_MAX] * n for _ in range(m)]
        pq = []  # min-heap via heapq; all cells will be inserted in it (m*n)

        result[0][0] = 0
        heapq.heappush(pq, (0, (0, 0)))
        # S.C : O(m*n)
        while pq:  # O(m*n * log(m*n))
            currTime, cell = heapq.heappop(pq)
            i, j = cell

            if i == m - 1 and j == n - 1:
                return currTime

            for dir in self.directions:
                i_ = i + dir[0]
                j_ = j + dir[1]

                if i_ >= 0 and i_ < m and j_ >= 0 and j_ < n:
                    wait    = max(moveTime[i_][j_] - currTime, 0)
                    arrTime = currTime + wait + 1

                    if result[i_][j_] > arrTime:
                        result[i_][j_] = arrTime
                        heapq.heappush(pq, (arrTime, (i_, j_)))

        return -1


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().minTimeToReach([[0, 4], [4, 4]]) == 6
    assert Solution().minTimeToReach([[0, 0, 0], [0, 0, 0]]) == 3
    assert Solution().minTimeToReach([[0, 1], [1, 2]]) == 3
    print("ok")
