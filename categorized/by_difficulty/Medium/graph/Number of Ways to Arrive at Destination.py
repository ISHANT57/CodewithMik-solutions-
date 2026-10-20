#     Scroll below to see JAVA code also
#
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=F_jnqx14idY
#     Company Tags                : Will update soon
#     Leetcode Link               : https://leetcode.com/problems/number-of-ways-to-arrive-at-destination

from typing import List
from collections import defaultdict
import heapq

LLONG_MAX = 2**63 - 1

# Approach (Using Dijkstra's Algorithm)
# T.C : O(((V+E)*log(V))
# S.C : O(V+E)
class Solution:
    M = 10**9 + 7

    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        adj = defaultdict(list)
        for road in roads:
            u    = road[0]
            v    = road[1]
            time = road[2]
            adj[u].append((v, time))
            adj[v].append((u, time))

        pq = []  # min-heap of (time, node)
        result = [LLONG_MAX] * n
        pathCount = [0] * n

        result[0] = 0
        pathCount[0] = 1
        heapq.heappush(pq, (0, 0))

        while pq:
            currTime, currNode = heapq.heappop(pq)

            # if (currTime > result[currNode]) continue;

            for adjNode, roadTime in adj[currNode]:

                if currTime + roadTime < result[adjNode]:
                    result[adjNode] = currTime + roadTime
                    pathCount[adjNode] = pathCount[currNode]
                    heapq.heappush(pq, (result[adjNode], adjNode))
                elif currTime + roadTime == result[adjNode]:
                    pathCount[adjNode] = (pathCount[adjNode] + pathCount[currNode]) % self.M

        return pathCount[n - 1]

Approach1 = Solution


if __name__ == "__main__":
    s = Solution()
    roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]
    assert s.countPaths(7, roads) == 4
    assert s.countPaths(2, [[1, 0, 10]]) == 1
    print("ok")
