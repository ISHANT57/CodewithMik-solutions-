#     Scroll below to see JAVA code also (Java sections skipped in this Python port)
#
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=zdGouql8XKs
#     Company Tags                : GOOGLE, ORACLE, PALANTIR TECHNOLOGIES (Thank you Thank you Himanshu for this list)
#     Leetcode Link               : https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/description/

from typing import List
from collections import defaultdict, deque


# ************************************************ C++ (ported to Python) ************************************************
# Approach-1 (Using DFS)
# T.C : O(n * (n+m)) , n = number of vertices and m = number of edges
# S.C : O(n+m)
class Solution:

    def DFS(self, ancestor: int, adj, currNode: int, result: List[List[int]]) -> None:

        for ngbr in adj[currNode]:
            if not result[ngbr] or result[ngbr][-1] != ancestor:  # to avoid duplicate entry
                result[ngbr].append(ancestor)
                self.DFS(ancestor, adj, ngbr, result)

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        result = [[] for _ in range(n)]
        adj = defaultdict(list)  # unordered_map<int, vector<int>>

        for vec in edges:
            u = vec[0]
            v = vec[1]

            adj[u].append(v)  # u --> v

        for i in range(n):
            ancestor = i
            self.DFS(ancestor, adj, i, result)

        return result


Approach1 = Solution


# Approach-2 (Reversing the graph + Using DFS)
# T.C : O(n * (n+m)) , n = number of vertices and m = number of edges
# S.C : O(n+m)
class Solution:

    def DFS(self, u: int, adj, visited: List[bool]) -> None:
        visited[u] = True

        for v in adj[u]:
            if visited[v] != True:
                self.DFS(v, adj, visited)

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        result = []
        adj = defaultdict(list)  # unordered_map<int, vector<int>>

        for vec in edges:  # O(E)
            u = vec[0]
            v = vec[1]

            adj[v].append(u)  # v --> u

        for u in range(n):
            ancestors = []
            visited = [False] * n
            self.DFS(u, adj, visited)

            for i in range(n):
                if i == u:
                    continue

                if visited[i] == True:
                    ancestors.append(i)

            result.append(ancestors)

        return result


Approach2 = Solution


# Approach-3 (Using Topological Sorting)
# T.C : O(n + m + n^2 + nlogn) -> O(n+m) for building the graph and performing the topological sort,
#                      -> O(n^2) for processing each node and merging ancestor lists.
#                      -> O(nlogn) for sorting the ancestor lists for each node.
# S.C : O(n^2+m)
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        result = [[] for _ in range(n)]
        adj = defaultdict(list)  # S.C : O(V+E)

        indegree = [0] * n

        for vec in edges:  # O(E)
            u = vec[0]
            v = vec[1]

            adj[u].append(v)  # u --> v
            indegree[v] += 1

        # TOPOLOGICAL SORTING
        que = deque()
        for i in range(n):
            if indegree[i] == 0:
                que.append(i)

        topoOrder = []
        while que:
            curr = que.popleft()
            topoOrder.append(curr)

            for v in adj[curr]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    que.append(v)

        vec = [set() for _ in range(n)]

        for node in topoOrder:
            for v in adj[node]:
                vec[v].add(node)  # adding node ancestor
                vec[v].update(vec[node])  # adding ancestors of node

        for i in range(n):
            result[i] = list(vec[i])

            result[i].sort()

        return result


Approach3 = Solution


if __name__ == "__main__":
    n = 8
    edges = [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]
    expected = [[], [], [], [0, 1], [0, 2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3]]
    for cls in (Approach1, Approach2, Approach3):
        res = cls().getAncestors(n, edges)
        res = [sorted(r) for r in res]
        assert res == expected, (cls, res)
    print("ok")
