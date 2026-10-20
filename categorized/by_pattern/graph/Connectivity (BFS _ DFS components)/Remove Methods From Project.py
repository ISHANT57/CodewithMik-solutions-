# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=2D13j9J62g4
# Company Tags                : will update later
# Leetcode Link               : https://leetcode.com/problems/remove-methods-from-project/description/
# (Java duplicate sections of the original file are skipped)

import sys
from typing import List
from collections import deque

sys.setrecursionlimit(10 ** 6)


# ***************************************************** C++ (Python port) *****************************************************
# Approach-1 - Using BFS
# T.C : O(V+E) , V = number of nodes(methods), E = number of edges
# S.C : O(V+E), V = number of nodes(methods), E = number of edges
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # O(V+E), V = nodes , E = edges
        # graph - adjacency list
        adj = [[] for _ in range(n)]  # u -> {ngbr1, ngbr2} #O(V+E)
        inDegree = [0] * n  # O(V)
        suspicious = [False] * n  # O(V)

        for edge in invocations:
            u = edge[0]
            v = edge[1]
            adj[u].append(v)
            inDegree[v] += 1

        # BFS
        que = deque()
        que.append(k)
        suspicious[k] = True

        while que:
            curr = que.popleft()

            for ngbr in adj[curr]:
                inDegree[ngbr] -= 1
                if not suspicious[ngbr]:
                    que.append(ngbr)
                    suspicious[ngbr] = True

        result = []
        cannotRemove = False

        for i in range(n):
            if suspicious[i] and inDegree[i] > 0:
                cannotRemove = True
                break

            if not suspicious[i]:
                result.append(i)

        if cannotRemove:
            vec = [0] * n  # 0, 1, 2,... n-1
            for i in range(n):
                vec[i] = i
            return vec

        return result


Approach1 = Solution


# Approach-2 - Using DFS
# T.C : O(V+E) , V = number of nodes(methods), E = number of edges
# S.C : O(V+E), V = number of nodes(methods), E = number of edges
class Solution:
    def dfs(self, curr, adj, inDegree, suspicious):
        suspicious[curr] = True
        for ngbr in adj[curr]:
            inDegree[ngbr] -= 1
            if not suspicious[ngbr]:
                self.dfs(ngbr, adj, inDegree, suspicious)

    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # O(V+E), V = nodes , E = edges
        # graph - adjacency list
        adj = [[] for _ in range(n)]  # u -> {ngbr1, ngbr2} #O(V+E)
        inDegree = [0] * n  # O(V)
        suspicious = [False] * n  # O(V)
        for edge in invocations:
            u = edge[0]
            v = edge[1]
            adj[u].append(v)
            inDegree[v] += 1
        # DFS
        self.dfs(k, adj, inDegree, suspicious)

        result = []
        cannotRemove = False

        for i in range(n):
            if suspicious[i] and inDegree[i] > 0:
                cannotRemove = True
                break
            if not suspicious[i]:
                result.append(i)
        if cannotRemove:
            vec = [0] * n  # 0, 1, 2,... n-1
            for i in range(n):
                vec[i] = i
            return vec

        return result


Approach2 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2):
        assert S().remainingMethods(4, 1, [[1, 2], [0, 1], [3, 2]]) == [0, 1, 2, 3]
        assert S().remainingMethods(5, 0, [[1, 2], [0, 2], [0, 1], [3, 4]]) == [3, 4]
        assert S().remainingMethods(3, 2, [[1, 2], [0, 1], [2, 0]]) == []
    print("ok")
