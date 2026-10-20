# MY YOUTUBE VIDEO ON THIS Qn : DFS - https://www.youtube.com/watch?v=NeU-C1PTWB8
#                               BFS - https://www.youtube.com/watch?v=cvhXZt66VhA
#                               DSU - <soon>
# Company Tags                : Facebook, Samsung, Microsoft, Flipkart
# Leetcode Link               : https://leetcode.com/problems/is-graph-bipartite/
# GfG Link                    : https://practice.geeksforgeeks.org/problems/bipartite-graph/1

from typing import List
from collections import deque


# Approach-1 (Graph coloring : DFS)
class Solution:

    def checkBipartiteDFS(self, adj: List[List[int]], curr: int, color: List[int], currColor: int) -> bool:
        color[curr] = currColor  # color kardiya curr node ko

        # ab jaate hain adjacent nodes par
        for v in adj[curr]:

            if color[v] == color[curr]:
                return False

            if color[v] == -1:  # never colored (never visited)

                colorOfV = 1 - currColor

                if self.checkBipartiteDFS(adj, v, color, colorOfV) == False:
                    return False

        return True

    def isBipartite(self, V: int, adj: List[List[int]]) -> bool:

        color = [-1] * V  # no node colored in the start

        # red = 1
        # gree = 0

        for i in range(V):
            if color[i] == -1:
                if self.checkBipartiteDFS(adj, i, color, 1) == False:
                    return False

        return True


Approach1 = Solution


# Approach-2 (Graph coloring : BFS)
class Solution:

    def checkBipartiteBFS(self, adj: List[List[int]], curr: int, color: List[int], currColor: int) -> bool:
        color[curr] = currColor  # color kardiya curr node ko

        que = deque()
        que.append(curr)

        while que:
            u = que.popleft()

            for v in adj[u]:
                if color[v] == color[u]:
                    return False
                elif color[v] == -1:
                    color[v] = 1 - color[u]
                    que.append(v)

        return True

    def isBipartite(self, V: int, adj: List[List[int]]) -> bool:

        color = [-1] * V  # no node colored in the start

        # red = 1
        # gree = 0

        for i in range(V):
            if color[i] == -1:
                if self.checkBipartiteBFS(adj, i, color, 1) == False:
                    return False

        return True


Approach2 = Solution


# Approach-3 (Union Find)
class Solution:
    def find(self, parent: List[int], i: int) -> int:
        if parent[i] == i:
            return i

        parent[i] = self.find(parent, parent[i])
        return parent[i]

    def Union(self, parent: List[int], x: int, y: int) -> None:
        x_set = self.find(parent, x)
        y_set = self.find(parent, y)

        if x_set != y_set:
            parent[x_set] = y_set

    def isBipartite(self, graph: List[List[int]]) -> bool:
        V = len(graph)
        parent = [0] * V

        for i in range(V):
            parent[i] = i

        for i in range(V):
            # let i = 0 -> {1, 3}
            for x in graph[i]:
                u = i  # one end of edge
                v = x  # another end of edge
                # u and v should be in different sets

                x_set = self.find(parent, u)
                y_set = self.find(parent, v)

                if x_set == y_set:  # they can't be in same set
                    return False

                # {1, 3} in one set
                # Choose any one (1 or 3) as the representative of this set
                self.Union(parent, x, graph[i][0])
                # parent of every edge will be graph[i][0]

        return True


Approach3 = Solution


if __name__ == "__main__":
    g1 = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]  # not bipartite
    g2 = [[1, 3], [0, 2], [1, 3], [0, 2]]        # bipartite
    for A in (Approach1, Approach2):
        assert A().isBipartite(4, g1) == False
        assert A().isBipartite(4, g2) == True
    assert Approach3().isBipartite(g1) == False
    assert Approach3().isBipartite(g2) == True
    print("ok")
