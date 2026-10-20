#     Scroll below to see JAVA code also
#
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=3jFf14bG2JU
#     Company Tags                : Will update soon
#     Leetcode Link               : https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/

from typing import List
from collections import defaultdict
import heapq

INT_MAX = 2**31 - 1

# Approach (Using Dijkstra's Algorithm)
# T.C : O(E * log(V)), E = number of edges, V = number of vertices
# S.C : O(V+E) for adjacency list
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)  # unordered_map<int, vector<P>>

        for edge in edges:
            u  = edge[0]
            v  = edge[1]
            wt = edge[2]

            adj[u].append((v, wt))
            adj[v].append((u, 2*wt))  # reversed edge

        result = [INT_MAX] * n
        result[0] = 0
        pq = []  # min-heap
        heapq.heappush(pq, (0, 0))  # distance = 0, sourceNode = 0

        while pq:
            d, node = heapq.heappop(pq)
            if node == n-1:
                return result[node]

            for adjNode, dist in adj[node]:
                if d + dist < result[adjNode]:
                    result[adjNode] = d + dist
                    heapq.heappush(pq, (d+dist, adjNode))

        return -1

Approach1 = Solution


if __name__ == "__main__":
    s = Solution()
    assert s.minCost(4, [[0, 1, 3], [3, 1, 1], [2, 3, 4], [0, 2, 2]]) == 5
    assert s.minCost(4, [[0, 2, 1], [2, 1, 1], [1, 3, 1], [2, 3, 3]]) == 3
    print("ok")
