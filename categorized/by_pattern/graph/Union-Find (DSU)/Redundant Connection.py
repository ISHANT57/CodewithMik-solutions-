# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=EawxDEOxeIk
# Company Tags                : Google
# Leetcode Link               : https://leetcode.com/problems/redundant-connection

from typing import List
from collections import defaultdict, deque


# Approach-1 - Using DFS
# T.C : O(n^2)
# S.C : O(n)
class Solution:
    def dfs(self, adj, u: int, v: int, visited: List[bool]) -> bool:
        visited[u] = True

        if u == v:
            return True

        for ngbr in adj[u]:
            if visited[ngbr]:
                continue

            if self.dfs(adj, ngbr, v, visited):
                return True

        return False

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        # number of nodes = n
        # number of edges = n

        adj = defaultdict(list)

        for i in range(n):
            u = edges[i][0]
            v = edges[i][1]

            # size n+1 (labels are 1..n); C++ used n which would be out of bounds for node n
            visited = [False] * (n + 1)
            if u in adj and v in adj and self.dfs(adj, u, v, visited):
                return edges[i]

            adj[u].append(v)
            adj[v].append(u)

        return []


Approach1 = Solution


# Approach-2 - Using BFS
# T.C : O(n^2)
# S.C : O(n)
class Solution:
    def bfs(self, mp, start: int, end: int) -> bool:
        visited = [False] * (self.n + 1)
        que = deque()
        que.append(start)

        while que:
            curr = que.popleft()
            visited[curr] = True
            if curr == end:
                return True

            for x in mp[curr]:
                if not visited[x]:
                    que.append(x)
        return False

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        mp = defaultdict(list)  # map<int, vector<int>> (ordered map not needed for logic)
        self.n = len(edges)
        n = self.n

        for i in range(n):
            u = edges[i][0]
            v = edges[i][1]

            # if u and v are already in graph, then we check
            # if this current edge connects them again ?
            # If yes, this edge is unwanted (redundant)
            if u in mp and v in mp and self.bfs(mp, u, v):
                return edges[i]

            # Else add them to graph
            mp[u].append(v)
            mp[v].append(u)

        return []


Approach2 = Solution


# Approach-3 (DSU - Union Find with Path compression)
# T.C : O(n * alpha(n))
# S.C : O(n)
class DSU:
    def __init__(self, n: int):
        self.parent = [0] * (n + 1)  # 1, 2, 3, 4, 5.., n
        self.rank = [0] * (n + 1)
        for i in range(1, n + 1):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, x: int) -> int:
        if x == self.parent[x]:
            return x

        self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def Union(self, x: int, y: int) -> None:
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent == y_parent:
            return

        if self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
        elif self.rank[y_parent] > self.rank[x_parent]:
            self.parent[x_parent] = y_parent
        else:
            self.parent[y_parent] = x_parent  # we made x as the parent
            self.rank[x_parent] += 1


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        dsu = DSU(n)
        # T.C : DSU = alpha(n)

        # T.C : O(n * alpha(n))
        for edge in edges:  # O(n)
            u = edge[0]
            v = edge[1]

            if dsu.find(u) == dsu.find(v):
                return edge

            dsu.Union(u, v)

        return []


Approach3 = Solution

# (Java section of the original file skipped: duplicates of the C++ approaches)

if __name__ == "__main__":
    for S in (Approach1, Approach2, Approach3):
        assert S().findRedundantConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
        assert S().findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]
    print("ok")
