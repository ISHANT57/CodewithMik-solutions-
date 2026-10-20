# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=8YdqvOKViWA
# Company Tags                : Amazon, Microsoft
# Leetcode Link               : https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance
#
# Using Dijkstra's - https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Graph/Dijkstra'a%20Based%20Problems/Find%20the%20City%20With%20the%20Smallest%20Number%20of%20Neighbors%20at%20a%20Threshold%20Distance.cpp
# Using Floyd Warshall - https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Graph/Floyd%20Warshall/Find%20the%20City%20With%20the%20Smallest%20Number%20of%20Neighbors%20at%20a%20Threshold%20Distance.cpp
# (Java duplicate section of the original file is skipped)

from typing import List

INT_MAX = 2 ** 31 - 1


# ***************************************************** C++ (Python port) *****************************************************
# Approach (Using Bellman-Ford)
# T.C : O(V * (V * E)) where E is the number of edges and V = number of vertices. We call Bellman(V*E) for each vertex.
#       In worst case , max edges = V*(V-1)/2
#       O(V * V*(V-1)/2 * log V)
#       Which is approximately equal to O(V^4)
# S.C : O(V^2)
class Solution:
    # (C++ had #define P pair<int, int>, unused)

    def bellmanFord(self, n, edges, shortestPathDistances, source):
        for k in range(len(shortestPathDistances)):  # fill with INT_MAX
            shortestPathDistances[k] = INT_MAX
        shortestPathDistances[source] = 0

        for i in range(1, n):
            for edge in edges:
                u = edge[0]
                v = edge[1]
                wt = edge[2]
                if (shortestPathDistances[u] != INT_MAX and
                        shortestPathDistances[u] + wt < shortestPathDistances[v]):
                    shortestPathDistances[v] = shortestPathDistances[u] + wt
                # bi-directional edge
                if (shortestPathDistances[v] != INT_MAX and
                        shortestPathDistances[v] + wt < shortestPathDistances[u]):
                    shortestPathDistances[u] = shortestPathDistances[v] + wt

    def getCityWithFewestReachable(self, n, shortestPathMatrix, distanceThreshold):
        cityWithFewestReachable = -1
        fewestReachableCount = INT_MAX

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
        shortestPathMatrix = [[INT_MAX] * n for _ in range(n)]

        for i in range(n):
            shortestPathMatrix[i][i] = 0  # Distance to itself is zero

        for edge in edges:
            u = edge[0]
            v = edge[1]
            wt = edge[2]
            shortestPathMatrix[u][v] = wt
            shortestPathMatrix[v][u] = wt

        # Compute shortest paths from each city using Bellman-Ford
        for i in range(n):
            self.bellmanFord(n, edges, shortestPathMatrix[i], i)

        return self.getCityWithFewestReachable(n, shortestPathMatrix, distanceThreshold)


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().findTheCity(4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4) == 3
    assert Solution().findTheCity(5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2) == 0
    print("ok")
