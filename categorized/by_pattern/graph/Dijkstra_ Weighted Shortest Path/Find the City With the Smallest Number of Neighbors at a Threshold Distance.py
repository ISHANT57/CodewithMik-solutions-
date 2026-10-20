#     Scroll below to see JAVA code also
#
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=8YdqvOKViWA
#     Company Tags                : Amazon, Microsoft
#     Leetcode Link               : https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance
#
# Using Bellman Ford - https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Graph/Bellman-Ford%20Based%20Problems/Find%20the%20City%20With%20the%20Smallest%20Number%20of%20Neighbors%20at%20a%20Threshold%20Distance.cpp
# Using Floyd Warshall - https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Graph/Floyd%20Warshall/Find%20the%20City%20With%20the%20Smallest%20Number%20of%20Neighbors%20at%20a%20Threshold%20Distance.cpp

from typing import List
from collections import defaultdict
import heapq

INT_MAX = 2**31 - 1

# Approach (Using Dijkstra's)
# T.C : O(V * ElogV) where E is the number of edges and V = number of vertices. We call Dijkstra's for each vertex.
        # In worst case , max edges = V*(V-1)/2
        # O(V * V*(V-1)/2 * log V)
        # Which is approximately equal to O(V^3 * log V)
# S.C : O(V^2)
class Solution:
    # Khandaani Dijkstra's algorithm to find shortest paths from a source city
    def dijkstra(self, n: int, adj, result: List[int], S: int) -> None:
        pq = []  # min-heap of (dist, node)
        heapq.heappush(pq, (0, S))
        for i in range(len(result)):  # fill(result.begin(), result.end(), INT_MAX)
            result[i] = INT_MAX
        result[S] = 0  # Distance to source itself is zero

        # Process nodes in priority order
        while pq:
            d, node = heapq.heappop(pq)

            for adjNode, dist in adj[node]:
                if d + dist < result[adjNode]:
                    result[adjNode] = d + dist
                    heapq.heappush(pq, (d + dist, adjNode))

    def getCityWithFewestReachable(self, n: int, shortestPathMatrix: List[List[int]], distanceThreshold: int) -> int:
        cityWithFewestReachable = -1
        fewestReachableCount = INT_MAX

        # Count number of cities reachable within the distance threshold for each city
        for i in range(n):
            reachableCount = 0
            for j in range(n):
                if i != j and shortestPathMatrix[i][j] <= distanceThreshold:
                    reachableCount += 1

            if reachableCount <= fewestReachableCount:
                fewestReachableCount = reachableCount
                cityWithFewestReachable = i
        return cityWithFewestReachable

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = defaultdict(list)  # unordered_map<int, vector<P>>

        shortestPathMatrix = [[INT_MAX] * n for _ in range(n)]

        for i in range(n):
            shortestPathMatrix[i][i] = 0  # Distance to itself is zero

        for edge in edges:
            start = edge[0]
            end = edge[1]
            weight = edge[2]
            adj[start].append((end, weight))
            adj[end].append((start, weight))

        # Compute shortest paths from each city using Dijkstra's algorithm
        for i in range(n):
            self.dijkstra(n, adj, shortestPathMatrix[i], i)

        return self.getCityWithFewestReachable(n, shortestPathMatrix, distanceThreshold)

Approach1 = Solution


if __name__ == "__main__":
    s = Solution()
    assert s.findTheCity(4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4) == 3
    assert s.findTheCity(5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2) == 0
    print("ok")
