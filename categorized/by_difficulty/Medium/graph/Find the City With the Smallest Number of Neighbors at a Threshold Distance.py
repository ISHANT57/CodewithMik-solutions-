#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=8YdqvOKViWA
#     Company Tags                : Amazon, Microsoft
#     Leetcode Link               : https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance

from typing import List

INT_MAX = 2**31 - 1

# Using Dijkstra's - https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Graph/Dijkstra'a%20Based%20Problems/Find%20the%20City%20With%20the%20Smallest%20Number%20of%20Neighbors%20at%20a%20Threshold%20Distance.cpp
# Using Bellman Ford - https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Graph/Bellman-Ford%20Based%20Problems/Find%20the%20City%20With%20the%20Smallest%20Number%20of%20Neighbors%20at%20a%20Threshold%20Distance.cpp


# ************************************************************ C++ ************************************************************
# Approach (Using Dijkstra's)   [note: the code below is actually Floyd-Warshall, as in the source]
# T.C : O(V^3)
# S.C : O(V^2)
class Solution:
    # #define P pair<int, int>  (unused in the source; pair -> tuple)
    def floydWarshall(self, n: int, shortestPathMatrix: List[List[int]]) -> None:

        for via in range(n):

            for i in range(n):
                for j in range(n):

                    shortestPathMatrix[i][j] = min(shortestPathMatrix[i][j],
                                                   shortestPathMatrix[i][via] + shortestPathMatrix[via][j])

    def getCityWithFewestReachable(self, n: int, shortestPathMatrix: List[List[int]], distanceThreshold: int) -> int:
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
        shortestPathMatrix = [[int(1e9 + 7)] * n for _ in range(n)]

        for i in range(n):
            shortestPathMatrix[i][i] = 0  # Distance to itself is zero

        for edge in edges:
            u = edge[0]
            v = edge[1]
            wt = edge[2]
            shortestPathMatrix[u][v] = wt
            shortestPathMatrix[v][u] = wt

        self.floydWarshall(n, shortestPathMatrix)

        return self.getCityWithFewestReachable(n, shortestPathMatrix, distanceThreshold)


Approach1 = Solution


if __name__ == "__main__":
    s = Solution()
    assert s.findTheCity(4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4) == 3
    assert s.findTheCity(5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2) == 0
    print("ok")
