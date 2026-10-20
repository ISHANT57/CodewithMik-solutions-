#     Scroll below to see JAVA code also
#
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=F6sRIQKslwA
#     Company Tags                : will update soon
#     Leetcode Link               : https://leetcode.com/problems/modify-graph-edge-weights

from typing import List
from collections import defaultdict
import heapq

INT_MAX = 2**31 - 1

# Using Dijkstra for Shortest Path
# T.C : O(E * E * Log(V)) //E = number of edges, V = number of vertices/nodes
# S.C : O(V+E)
class Solution:
    LARGE_VALUE = int(2e9)

    def DijkstraAlgo(self, edges: List[List[int]], n: int, src: int, dest: int) -> int:
        # make the graph excluing -1 et edges
        adj = defaultdict(list)  # u -> (v, wt)

        for edge in edges:
            if edge[2] != -1:
                u  = edge[0]
                v  = edge[1]
                wt = edge[2]

                adj[u].append((v, wt))
                adj[v].append((u, wt))

        pq = []  # min-heap of (dist, node)
        result = [INT_MAX] * n  # result[i] = shortest path distance of src to ith node
        # vector<bool> visited(n, false); //YOU DON"T NEED VISITED ARRAY BECAUSE ANYWAYS YOU WILL NOT VISIT SAME NODE AS IT's DISTANCE WILL BE INCREASED NEXT TIME DIJKSTRA YOU WILL SKIP IT

        result[src] = 0  # src to src distance is 0
        heapq.heappush(pq, (0, src))

        while pq:
            currDist, currNode = heapq.heappop(pq)

            # We don't need visited vector in Dijkstra
            # if(visited[currNode] == true) {
            #     continue;
            # }
            # visited[currNode] = true;

            for nbr, wt in adj[currNode]:
                if result[nbr] > currDist + wt:
                    result[nbr] = currDist + wt
                    heapq.heappush(pq, (result[nbr], nbr))

        return result[dest]

    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        currShortestDist = self.DijkstraAlgo(edges, n, source, destination)

        if currShortestDist < target:
            return []

        matchedTarget = (currShortestDist == target)

        for edge in edges:
            if edge[2] == -1:

                edge[2] = self.LARGE_VALUE if matchedTarget == True else 1  # assign lowest number i.e. 1

                if matchedTarget != True:
                    newShortestDist = self.DijkstraAlgo(edges, n, source, destination)

                    if newShortestDist <= target:
                        matchedTarget = True
                        edge[2] += (target - newShortestDist)

        if matchedTarget == False:
            return []
        return edges

Approach1 = Solution


if __name__ == "__main__":
    s = Solution()
    edges = [[4, 1, -1], [2, 0, -1], [0, 3, -1], [4, 3, -1]]
    res = s.modifiedGraphEdges(5, edges, 0, 1, 5)
    assert res and s.DijkstraAlgo(res, 5, 0, 1) == 5 and all(e[2] > 0 for e in res)
    assert Solution().modifiedGraphEdges(3, [[0, 1, -1], [0, 2, 5]], 0, 2, 6) == []
    e2 = [[1, 0, 4], [1, 2, 3], [2, 3, 5], [0, 3, -1]]
    r2 = Solution().modifiedGraphEdges(4, e2, 0, 2, 6)
    assert r2 and Solution().DijkstraAlgo(r2, 4, 0, 2) == 6
    print("ok")
