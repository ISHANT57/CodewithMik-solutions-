#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=k8LBJqGLLQE
#     Company Tags                : MICROSOFT
#     Leetcode Link               : https://leetcode.com/problems/find-eventual-safe-states/

import sys
from collections import deque
from typing import List

sys.setrecursionlimit(10000)


# ****************************************************************  C++  *****************************************************************
# Approach-1 (Using Same code of DFS Cycle Check in directed Graph)
# T.C : O(V+E)
# S.C : O(V+E)
class Solution:
    def isCycleDFS(self, adj: List[List[int]], u: int, visited: List[bool], inRecursion: List[bool]) -> bool:
        visited[u] = True
        inRecursion[u] = True

        for v in adj[u]:
            # if not visited, then we check for cycle in DFS
            if visited[v] == False and self.isCycleDFS(adj, v, visited, inRecursion):
                return True
            elif inRecursion[v] == True:
                return True

        inRecursion[u] = False
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        visited = [False] * V
        inRecursion = [False] * V

        for i in range(V):
            if not visited[i]:
                self.isCycleDFS(graph, i, visited, inRecursion)

        safeNodes = []
        for i in range(V):
            if not inRecursion[i]:
                safeNodes.append(i)

        return safeNodes


Approach1 = Solution


# Approach-2 (Using BFS) (Toplogical Sort)
# T.C : O(V+E)
# S.C : O(V+E)
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)

        adj = [[] for _ in range(V)]

        que = deque()
        indegree = [0] * V
        count = 0
        # 1
        for u in range(V):
            for v in graph[u]:
                adj[v].append(u)
                indegree[u] += 1

        # 2. Fill que, indegree with 0
        for i in range(V):
            if indegree[i] == 0:
                que.append(i)
                count += 1

        # 3. Simple BFS
        safe = [False] * V
        while que:
            u = que.popleft()
            safe[u] = True

            for v in adj[u]:
                indegree[v] -= 1

                if indegree[v] == 0:
                    que.append(v)
                    count += 1

        safeNodes = []
        for i in range(V):
            if safe[i]:
                safeNodes.append(i)
        return safeNodes


Approach2 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2):
        s = S()
        assert s.eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]) == [2, 4, 5, 6]
        assert s.eventualSafeNodes([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]) == [4]
    print("ok")
