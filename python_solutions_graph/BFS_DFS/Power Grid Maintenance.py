# MY YOUTUBE VIDEO ON THIS Qn : DFS - https://www.youtube.com/watch?v=ylJ2lDHUBZA
#                               DSU - https://www.youtube.com/watch?v=R85fl-ku9WQ
# Company Tags                : will update later
# Leetcode Link               : https://leetcode.com/problems/power-grid-maintenance
# (Java duplicate sections of the original file are skipped)
#
# NOTE: C++ std::set<int> is replaced by a sorted Python list kept ordered with bisect
#       (insort for insert, bisect_left + pop for erase, list[0] for *begin()).

import sys
from bisect import bisect_left, insort
from collections import defaultdict, deque
from typing import List

sys.setrecursionlimit(10 ** 6)


# ***************************************************** C++ (Python port) *****************************************************
# Approach-1 (Using DFS)
# T.C : O((c + n) + q log c)
# S.C : O(c + n)
class Solution:
    # O(c + n)
    def dfs(self, node, adj, id, nodeId, mp, visited):
        visited[node] = True
        insort(mp[id], node)  # set insert (sorted list)
        nodeId[node] = id

        for ngbr in adj[node]:
            if not visited[ngbr]:
                self.dfs(ngbr, adj, id, nodeId, mp, visited)

    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for edge in connections:
            u = edge[0]
            v = edge[1]

            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * (c + 1)
        nodeId = [0] * (c + 1)
        # id -> {}  (sorted list standing in for std::set)
        mp = defaultdict(list)

        # O(c+n)
        for node in range(1, c + 1):
            if not visited[node]:
                id = node
                self.dfs(node, adj, id, nodeId, mp, visited)

        result = []
        # O(q * log(c))
        for query in queries:
            type = query[0]  # 1, 2
            node = query[1]  # station/node

            if type == 1:
                id = nodeId[node]
                i = bisect_left(mp[id], node)
                if i < len(mp[id]) and mp[id][i] == node:
                    result.append(node)
                elif mp[id]:
                    result.append(mp[id][0])
                else:
                    result.append(-1)
            else:
                id = nodeId[node]
                i = bisect_left(mp[id], node)
                if i < len(mp[id]) and mp[id][i] == node:
                    mp[id].pop(i)  # erase
        return result


Approach1 = Solution


# Approach-2 (Using BFS)
# T.C : O((c + n) + q log c)
# S.C : O(c + n)
class Solution:
    # O(c + n)
    def bfs(self, start, adj, id, nodeId, mp, visited):
        q = deque()
        q.append(start)
        visited[start] = True
        nodeId[start] = id
        insort(mp[id], start)

        while q:
            node = q.popleft()

            for ngbr in adj[node]:
                if not visited[ngbr]:
                    visited[ngbr] = True
                    nodeId[ngbr] = id
                    insort(mp[id], ngbr)
                    q.append(ngbr)

    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for edge in connections:
            u = edge[0]
            v = edge[1]
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * (c + 1)
        nodeId = [0] * (c + 1)
        mp = defaultdict(list)  # sorted list standing in for std::set

        # O(c + n)
        for node in range(1, c + 1):
            if not visited[node]:
                id = node
                self.bfs(node, adj, id, nodeId, mp, visited)

        result = []
        # O(q * log(c))
        for query in queries:
            type = query[0]  # 1 or 2
            node = query[1]  # station/node

            if type == 1:
                id = nodeId[node]
                i = bisect_left(mp[id], node)
                if i < len(mp[id]) and mp[id][i] == node:
                    result.append(node)
                elif mp[id]:
                    result.append(mp[id][0])
                else:
                    result.append(-1)
            else:
                id = nodeId[node]
                i = bisect_left(mp[id], node)
                if i < len(mp[id]) and mp[id][i] == node:
                    mp[id].pop(i)  # erase

        return result


Approach2 = Solution


# Approach-3 (Using DSU)
# T.C : O((n+c+q)*alpha(c)), n = connections.size(), c = number of nodes, q = number of queries
# S.C : O(n + c + q)
class Solution:
    def Find(self, x):
        if x == self.parent[x]:
            return x

        self.parent[x] = self.Find(self.parent[x])
        return self.parent[x]

    def Union(self, x, y):
        x_par = self.Find(x)
        y_par = self.Find(y)

        if x_par == y_par:
            return

        if self.rank[x_par] > self.rank[y_par]:
            self.parent[y_par] = x_par
            self.rank[x_par] += 1
        elif self.rank[x_par] < self.rank[y_par]:
            self.parent[x_par] = y_par
            self.rank[y_par] += 1
        else:
            self.parent[y_par] = x_par
            self.rank[x_par] += 1

    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = []
        n = len(connections)

        self.rank = [0] * (c + 1)
        self.parent = [0] * (c + 1)
        for i in range(1, c + 1):
            self.parent[i] = i

        for edge in connections:
            u = edge[0]
            v = edge[1]
            self.Union(u, v)

        mp = defaultdict(list)  # id -> {ordered set of nodes} (sorted list)
        nodeId = [0] * (c + 1)

        for i in range(1, c + 1):
            par = self.Find(i)
            insort(mp[par], i)
            nodeId[i] = par

        for query in queries:
            type = query[0]  # 1, 2
            node = query[1]  # station/node
            id = nodeId[node]

            i = bisect_left(mp[id], node)
            present = i < len(mp[id]) and mp[id][i] == node
            if type == 1:
                if present:
                    result.append(node)
                elif mp[id]:
                    result.append(mp[id][0])
                else:
                    result.append(-1)
            else:
                if present:
                    mp[id].pop(i)

        return result


Approach3 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2, Approach3):
        r = S().processQueries(5, [[1, 2], [2, 3], [3, 4], [4, 5]], [[1, 3], [2, 1], [1, 1], [2, 2], [1, 2]])
        assert r == [3, 2, 3], r
        r = S().processQueries(3, [], [[1, 1], [2, 1], [1, 1]])
        assert r == [1, -1], r
    print("ok")
