# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=7b7GbuFMWRw
# Company Tags                : AMAZON
# Leetcode Link               : https://leetcode.com/problems/count-the-number-of-complete-components

from typing import List
from collections import defaultdict, deque


# Approach-1 (Using DFS)
# T.C : O(V+E)
# S.C : O(V+E)
class Solution:
    # v and e are C++ int& references; here they are one-element lists
    def dfs(self, i: int, adj, visited: List[bool], v: List[int], e: List[int]) -> None:
        visited[i] = True
        v[0] += 1
        e[0] += len(adj[i])

        for ngbr in adj[i]:
            if not visited[ngbr]:
                self.dfs(ngbr, adj, visited, v, e)

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        result = 0

        # Build the graph
        for edge in edges:
            u = edge[0]
            v = edge[1]

            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        for i in range(n):
            if visited[i] == True:
                continue
            v = [0]
            e = [0]
            self.dfs(i, adj, visited, v, e)

            if (v[0] * (v[0] - 1)) == e[0]:
                result += 1

        return result


Approach1 = Solution


# Approach-2 (Using BFS)
# T.C : O(V+E)
# S.C : O(V+E)
class Solution:
    # v and e are C++ int& references; here they are one-element lists
    def bfs(self, i: int, adj, visited: List[bool], v: List[int], e: List[int]) -> None:
        que = deque()
        que.append(i)
        visited[i] = True

        while que:
            curr = que.popleft()
            v[0] += 1
            e[0] += len(adj[curr])

            for ngbr in adj[curr]:
                if not visited[ngbr]:
                    visited[ngbr] = True
                    que.append(ngbr)

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        result = 0

        # Build the graph
        for edge in edges:
            u = edge[0]
            v = edge[1]

            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        for i in range(n):
            if visited[i] == True:
                continue
            v = [0]
            e = [0]
            self.bfs(i, adj, visited, v, e)

            if (v[0] * (v[0] - 1)) == e[0]:
                result += 1

        return result


Approach2 = Solution


# Approach-3 (Using DSU)
# T.C : O(E * alpha(V))
# S.C : O(V)
class Solution:
    class DSU:
        def __init__(self, n: int):
            self.parent = [0] * n
            self.size = [0] * n
            for i in range(n):
                self.parent[i] = i
                self.size[i] = 1

        def find(self, x: int) -> int:
            if self.parent[x] == x:
                return x

            self.parent[x] = self.find(self.parent[x])  # path compression
            return self.parent[x]

        def Union(self, x: int, y: int) -> None:
            x_par = self.find(x)
            y_par = self.find(y)

            if x_par == y_par:
                return

            if self.size[x_par] > self.size[y_par]:
                self.parent[y_par] = x_par
                self.size[x_par] += self.size[y_par]
            elif self.size[x_par] < self.size[y_par]:
                self.parent[x_par] = y_par
                self.size[y_par] += self.size[x_par]
            else:
                self.parent[x_par] = y_par
                self.size[y_par] += self.size[x_par]

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = Solution.DSU(n)
        mp = defaultdict(int)  # root -> edges

        for edge in edges:
            u = edge[0]
            v = edge[1]
            dsu.Union(u, v)

        # Count the edges for each root
        for edge in edges:
            u = edge[0]
            v = edge[1]
            root = dsu.find(u)
            mp[root] += 1  # incrementing for edge count

        result = 0
        for i in range(n):
            if dsu.find(i) == i:  # ye papa ji hain (root hai)
                v = dsu.size[i]
                e = mp[i]

                if (v * (v - 1)) // 2 == e:
                    result += 1

        return result


Approach3 = Solution


if __name__ == "__main__":
    for sol in (Approach1, Approach2, Approach3):
        assert sol().countCompleteComponents(6, [[0, 1], [0, 2], [1, 2], [3, 4]]) == 3
        assert sol().countCompleteComponents(6, [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]) == 1
    print("ok")
