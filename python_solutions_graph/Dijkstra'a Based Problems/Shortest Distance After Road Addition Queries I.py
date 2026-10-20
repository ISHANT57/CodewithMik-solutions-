# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=INUZt6li__c
# Company Tags                : Will update soon
# Leetcode Link               : https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i

from typing import List
import heapq
from collections import defaultdict, deque

INT_MAX = 2**31 - 1


# Approach-1 (Using Dijkstra's Algorothm - Assuming each edge weight is 1)
# T.C : O(q * (V+E)) , V = number of vertices and E = number of edges
# S.C : O(V+E)
class Solution:
    def __init__(self):
        self.adj = defaultdict(list)

    def dijkstra(self, n: int) -> int:
        result = [INT_MAX] * n
        result[0] = 0
        pq = []  # min heap of (distance, node)
        heapq.heappush(pq, (0, 0))

        while pq:
            d, node = heapq.heappop(pq)  # d = distance of current node, node = current node

            if node == n - 1:
                return result[n - 1]

            if d > result[node]:
                continue

            for p in self.adj[node]:
                adjNode = p[0]
                dist = p[1]
                if d + dist < result[adjNode]:
                    result[adjNode] = d + dist
                    heapq.heappush(pq, (d + dist, adjNode))
        return result[n - 1]

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        result = []

        for i in range(n - 1):
            self.adj[i].append((i + 1, 1))

        for query in queries:
            u = query[0]
            v = query[1]
            self.adj[u].append((v, 1))
            d = self.dijkstra(n)
            result.append(d)

        return result


Approach1 = Solution


# Approach-2 (Using BFS (edges are unweighted)
# T.C : O(q * (E log(V)) , V = number of vertices and E = number of edges
# S.C : O(V+E)
class Solution:
    def __init__(self):
        self.adj = defaultdict(list)

    def bfs(self, n: int) -> int:
        que = deque()
        que.append(0)
        visited = [False] * n
        visited[0] = True

        level = 0
        while que:
            size = len(que)
            while size > 0:
                size -= 1
                node = que.popleft()

                if node == n - 1:
                    return level  # Found the destination node

                for neighbor in self.adj[node]:
                    if not visited[neighbor]:
                        que.append(neighbor)
                        visited[neighbor] = True
            level += 1
        return -1  # If destination node is unreachable

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        self.adj.clear()

        for i in range(n - 1):
            self.adj[i].append(i + 1)

        k = len(queries)
        res = [0] * k
        for i in range(k):
            self.adj[queries[i][0]].append(queries[i][1])
            res[i] = self.bfs(n)
        return res


Approach2 = Solution


if __name__ == "__main__":
    for sol in (Approach1, Approach2):
        assert sol().shortestDistanceAfterQueries(5, [[2, 4], [0, 2], [0, 4]]) == [3, 2, 1]
        assert sol().shortestDistanceAfterQueries(4, [[0, 3], [0, 2]]) == [1, 1]
    print("ok")
