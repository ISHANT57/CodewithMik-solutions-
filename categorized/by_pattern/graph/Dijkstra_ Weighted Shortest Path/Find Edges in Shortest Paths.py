# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=O61WbSqXTgk
# Company Tags                : will update soon
# Leetcode Link               : https://leetcode.com/problems/find-edges-in-shortest-paths/

from typing import List
from collections import defaultdict
import heapq

INT_MAX = 2**31 - 1


# Using Dijkstra's
# T.C : O(n+E) , where n = number of vertices, E = number of edges
# S.C : O(n+E)
class Solution:
    # typedef long long ll; typedef pair<ll, ll> P;  (Python ints are unbounded; pairs are tuples)

    def dijkstra(self, adj, src: int, n: int) -> List[int]:
        pq = []  # min-heap of (wt, node) via heapq (greater<P>)

        dist = [INT_MAX] * n
        visited = [False] * n

        dist[src] = 0

        heapq.heappush(pq, (0, src))

        while pq:

            currWt, currNode = heapq.heappop(pq)

            if visited[currNode] == True:
                continue

            # (C++ loop variable was named "adj" shadowing the map; renamed to nbr here)
            for nbr in adj[currNode]:
                nextNode = nbr[0]
                nextWt = nbr[1]

                if dist[nextNode] > currWt + nextWt:
                    dist[nextNode] = currWt + nextWt
                    heapq.heappush(pq, (currWt + nextWt, nextNode))

            visited[currNode] = True

        return dist

    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        E = len(edges)

        adj = defaultdict(list)  # unordered_map<int, vector<P>>
        for edge in edges:
            u = edge[0]
            v = edge[1]
            w = edge[2]

            adj[u].append((v, w))
            adj[v].append((u, w))

        fromSrc  = self.dijkstra(adj, 0, n)
        fromDest = self.dijkstra(adj, n - 1, n)

        result = [False] * E

        for i in range(E):

            u = edges[i][0]
            v = edges[i][1]
            w = edges[i][2]

            distFromSrc  = fromSrc[u]   # x
            distFromDest = fromDest[v]  # y

            if distFromSrc + w + distFromDest == fromSrc[n - 1]:
                result[i] = True

            distFromSrc  = fromSrc[v]   # x
            distFromDest = fromDest[u]  # y
            if distFromSrc + w + distFromDest == fromSrc[n - 1]:
                result[i] = True

        return result


Approach1 = Solution


if __name__ == "__main__":
    edges = [[0,1,4],[0,2,1],[1,3,2],[1,4,3],[1,5,1],[2,3,1],[3,5,3],[4,5,2]]
    assert Solution().findAnswer(6, edges) == [True,True,True,False,True,True,True,False]
    edges = [[2,0,1],[0,1,1],[0,3,4],[3,2,2]]
    assert Solution().findAnswer(4, edges) == [True,False,False,True]
    print("ok")
