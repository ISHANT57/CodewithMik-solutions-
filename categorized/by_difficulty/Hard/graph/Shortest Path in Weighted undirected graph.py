# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=icVJUN45f1E
# Company Tags                : Nil
# GfG Link                    : https://practice.geeksforgeeks.org/problems/shortest-path-in-weighted-undirected-graph/1

import heapq
from collections import defaultdict
from typing import List


class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for vec in edges:
            u = vec[0]
            v = vec[1]
            w = vec[2]

            adj[u].append((v, w))
            adj[v].append((u, w))

        # min-heap of (dist, node), same as greater<pair<int,int>>
        pq = []
        result = [2**31 - 1] * (n + 1)
        parent = [0] * (n + 1)

        for i in range(1, n + 1):
            parent[i] = i

        result[1] = 0
        heapq.heappush(pq, (0, 1))

        while pq:
            d, node = heapq.heappop(pq)

            for adjNode, dist in adj[node]:
                if d + dist < result[adjNode]:
                    result[adjNode] = d + dist
                    heapq.heappush(pq, (d + dist, adjNode))
                    parent[adjNode] = node

        path = []
        node = n

        if result[node] == 2**31 - 1:
            return [-1]

        while parent[node] != node:
            path.append(node)
            node = parent[node]
        path.append(1)
        path.reverse()
        return path


Approach1 = Solution

if __name__ == "__main__":
    # GfG example: n=5, m=6
    edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]
    res = Solution().shortestPath(5, 6, edges)
    print(res)
    assert res == [1, 4, 3, 5]
    assert Solution().shortestPath(3, 1, [[1, 2, 1]]) == [-1]
    print("ok")
