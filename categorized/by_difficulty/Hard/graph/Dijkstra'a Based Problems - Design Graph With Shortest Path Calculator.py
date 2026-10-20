# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=EPvZsimuqwM
# Company Tags                : will update soon.
# Leetcode Link               : https://leetcode.com/problems/design-graph-with-shortest-path-calculator

from typing import List
from collections import defaultdict
import heapq

INT_MAX = 2**31 - 1


# Approach-1 (Using Dijkstra's Algorithm)
# T.C : Dijkatra's called M times - O(M * ElogV)
class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.adj = defaultdict(list)  # unordered_map<int, vector<pair<int, int>>>
        self.N = n
        self.result = []
        self.pq = []  # min-heap of (dist, node) via heapq (greater<pair<int,int>>)

        for vec in edges:
            u    = vec[0]
            v    = vec[1]
            cost = vec[2]

            self.adj[u].append((v, cost))

    def addEdge(self, edge: List[int]) -> None:
        u    = edge[0]
        v    = edge[1]
        cost = edge[2]

        self.adj[u].append((v, cost))

    def shortestPath(self, node1: int, node2: int) -> int:

        result = [INT_MAX] * self.N

        result[node1] = 0
        heapq.heappush(self.pq, (0, node1))

        while self.pq:

            d, node = heapq.heappop(self.pq)

            for vec in self.adj[node]:

                adjNode = vec[0]
                dist    = vec[1]

                if d + dist < result[adjNode]:

                    result[adjNode] = d + dist
                    heapq.heappush(self.pq, (d + dist, adjNode))

        return -1 if result[node2] == INT_MAX else result[node2]


Approach1 = Graph

# Approach-2 (Using Floyd Warshal Algorithm because it helps to find multi Source Shortest Path)
# Code - https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Graph/Floyd%20Warshall/Design%20Graph%20With%20Shortest%20Path%20Calculator.cpp
# (Approach-2 was only a link in the source, no code, so none is provided here.)


if __name__ == "__main__":
    g = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
    assert g.shortestPath(3, 2) == 6
    assert g.shortestPath(0, 3) == -1
    g.addEdge([1, 3, 4])
    assert g.shortestPath(0, 3) == 6
    print("ok")
