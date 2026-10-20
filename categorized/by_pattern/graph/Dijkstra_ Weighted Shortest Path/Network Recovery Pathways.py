#    Scroll below to see JAVA code also
#
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=sDdQ1-9TNP0
#     Company Tags                : will update soon
#     Leetcode Link               : https://leetcode.com/problems/network-recovery-pathways/

from typing import List
from collections import defaultdict
import heapq

INT_MAX = 2**31 - 1
LLONG_MAX = 2**63 - 1

# Appoach Using Dijkstra's + Binary Search on Answer
# T.C : O((E+V)log(V) * log(U)), E = number of edges, V = number of vertices, (E+V)log(V) is for Dijkstra and log(U) is for Binary Search, U = r-l;
# S.C : O(V+E)
class Solution:
    def check(self, mid: int, n: int, k: int, adj) -> bool:
        result = [LLONG_MAX] * n

        pq = []  # min-heap of (dist, node)

        result[0] = 0

        heapq.heappush(pq, (0, 0))

        while pq:
            d, node = heapq.heappop(pq)

            if d > k:
                return False

            if node == n - 1:
                return True

            if d > result[node]:
                continue

            for vec in adj[node]:
                adjNode  = vec[0]
                edgeCost = vec[1]

                if edgeCost < mid:  # because I want the score to be mid
                    continue

                if d + edgeCost < result[adjNode]:
                    result[adjNode] = d + edgeCost
                    heapq.heappush(pq, (d + edgeCost, adjNode))

        return False

    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        adj = defaultdict(list)

        l, r = INT_MAX, 0

        for edge in edges:
            u = edge[0]
            v = edge[1]
            w = edge[2]

            if not online[u] or not online[v]:
                continue

            adj[u].append([v, w])
            l = min(l, w)
            r = max(r, w)

        answer = -1

        while l <= r:
            mid = l + (r - l) // 2

            if self.check(mid, n, k, adj):
                answer = mid
                l = mid + 1
            else:
                r = mid - 1

        return answer

Approach1 = Solution


if __name__ == "__main__":
    s = Solution()
    assert s.findMaxPathScore([[0, 1, 5], [1, 3, 10], [0, 2, 3], [2, 3, 4]], [True, True, True, True], 10) == 3
    assert s.findMaxPathScore([[0, 1, 7], [1, 4, 5], [0, 2, 6], [2, 3, 6], [3, 4, 2], [2, 4, 6]], [True, True, True, False, True], 12) == 6
    assert s.findMaxPathScore([[0, 1, 5]], [True, False], 10) == -1
    print("ok")
