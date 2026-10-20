# MY YOUTUBE VIDEO ON THIS Qn : Using Prim's     - https://www.youtube.com/watch?v=hsr7KolYDH0
#                               Using Kruskal's  - https://www.youtube.com/watch?v=O6wQQtv71S0
# Company Tags                : META
# Leetcode Link               : https://leetcode.com/problems/min-cost-to-connect-all-points/

import heapq
from typing import List

# Approach-1 (Using Priority_queue and Adjacency list representation of graph) - Prim's Algorithm
# typedef pair<int, int> P  -> tuple (int, int)
class Solution:
    def minMST(self, adj, V: int) -> int:
        pq = []  # minheap (heapq is a min-heap, same as greater<P>)
        heapq.heappush(pq, (0, 0))  # {weight, vertex}

        inMST = [False] * V
        sum_ = 0

        while pq:

            p = heapq.heappop(pq)

            wt = p[0]
            node = p[1]

            if inMST[node] == True:
                continue

            inMST[node] = True  # added to mst
            sum_ += wt

            for tmp in adj[node]:

                neighbor = tmp[0]
                neighbor_wt = tmp[1]

                if inMST[neighbor] == False:
                    heapq.heappush(pq, (neighbor_wt, neighbor))

        return sum_

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        V = len(points)

        adj = [[] for _ in range(V)]

        for i in range(V):
            for j in range(i+1, V):
                x1 = points[i][0]
                y1 = points[i][1]

                x2 = points[j][0]
                y2 = points[j][1]

                d = abs(x1-x2) + abs(y1-y2)

                adj[i].append((j, d))
                adj[j].append((i, d))

        return self.minMST(adj, V)

Approach1 = Solution


# Approach-2 (Using 2-D matrix graph) - Prim's Algorithm
class Solution:
    def minKey(self, inMST: List[bool], key: List[int]) -> int:
        minIndex = 0
        minVal = 2**31 - 1  # INT_MAX
        for i in range(len(key)):
            if not inMST[i] and key[i] < minVal:
                minIndex = i
                minVal = key[i]
        return minIndex

    def MST(self, graph: List[List[int]], V: int) -> int:
        key = [2**31 - 1] * V  # INT_MAX
        inMST = [False] * V
        key[0] = 0

        for count in range(1, V):
            u = self.minKey(inMST, key)
            inMST[u] = True

            for v in range(V):
                if graph[u][v] and not inMST[v] and graph[u][v] < key[v]:
                    key[v] = graph[u][v]

        cost = 0
        for i in key:
            cost += i
        return cost

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = [[0] * n for _ in range(n)]

        for i in range(n-1):
            for j in range(i+1, n):
                p1 = points[i]
                p2 = points[j]
                md = abs(p1[0]-p2[0]) + abs(p1[1] - p2[1])
                graph[i][j] = md
                graph[j][i] = md

        return self.MST(graph, n)

Approach2 = Solution


# Approach-3 (Using Kruskal's Algorithm)
class Solution:

    def find(self, x: int) -> int:
        if x == self.parent[x]:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def Union(self, x: int, y: int) -> None:
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent == y_parent:
            return

        if self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
        elif self.rank[x_parent] < self.rank[y_parent]:
            self.parent[x_parent] = y_parent
        else:
            self.parent[x_parent] = y_parent
            self.rank[y_parent] += 1

    def Kruskal(self, vec: List[List[int]]) -> int:

        sum_ = 0
        for temp in vec:

            u = temp[0]
            v = temp[1]
            wt = temp[2]

            parent_u = self.find(u)
            parent_v = self.find(v)

            if parent_u != parent_v:
                self.Union(u, v)
                sum_ += wt

        return sum_

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        V = len(points)
        self.parent = [0] * V
        self.rank = [0] * V

        for i in range(V):
            self.parent[i] = i

        vec = []

        for i in range(V):

            for j in range(i+1, V):

                x1 = points[i][0]
                y1 = points[i][1]

                x2 = points[j][0]
                y2 = points[j][1]

                d = abs(x1-x2) + abs(y1-y2)

                vec.append([i, j, d])

        lambda_ = lambda v1: v1[2]  # comparator v1[2] < v2[2] -> sort key

        vec.sort(key=lambda_)

        return self.Kruskal(vec)

Approach3 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2, Approach3):
        assert S().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]) == 20
        assert S().minCostConnectPoints([[3,12],[-2,5],[-4,1]]) == 18
        assert S().minCostConnectPoints([[0,0]]) == 0
    print("ok")
