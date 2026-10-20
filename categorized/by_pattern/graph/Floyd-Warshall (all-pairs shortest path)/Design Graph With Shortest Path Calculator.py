#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=EPvZsimuqwM
#     Company Tags                : will update soon
#     Leetcode Link               : https://leetcode.com/problems/design-graph-with-shortest-path-calculator

from typing import List


# ******************************************************** C++ ********************************************************
# Approach-1 (Using Floyd Warshal Algorithm)
# T.C : O(N^3) - Making adj Matrix
class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.N = n
        self.adj = [[10**9] * n for _ in range(n)]

        for vec in edges:
            u = vec[0]
            v = vec[1]
            cost = vec[2]

            self.adj[u][v] = cost

        for i in range(n):
            self.adj[i][i] = 0

        # Floyd Warshal
        for k in range(n):

            for i in range(self.N):
                for j in range(self.N):

                    self.adj[i][j] = min(self.adj[i][j], self.adj[i][k] + self.adj[k][j])

    def addEdge(self, edge: List[int]) -> None:
        u = edge[0]
        v = edge[1]
        cost = edge[2]
        # check with 2 new vertices - u and v

        for i in range(self.N):
            for j in range(self.N):

                self.adj[i][j] = min(self.adj[i][j], self.adj[i][u] + cost + self.adj[v][j])

    def shortestPath(self, node1: int, node2: int) -> int:
        return -1 if self.adj[node1][node2] == 10**9 else self.adj[node1][node2]


Approach1 = Graph


# Approach-2 (Using Dijkstra's Algorithm)
# Code - https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Graph/Dijkstra'a%20Based%20Problems/Design%20Graph%20With%20Shortest%20Path%20Calculator.cpp
# (Not included in the source file; only a link was given.)


if __name__ == "__main__":
    g = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
    assert g.shortestPath(3, 2) == 6
    assert g.shortestPath(0, 3) == -1
    g.addEdge([1, 3, 4])
    assert g.shortestPath(0, 3) == 6
    print("ok")
