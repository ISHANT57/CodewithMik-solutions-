#     Scroll below to see JAVA code also (Java sections skipped in this Python port)
#
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=QyrmIu4Vo8A
#     Company Tags                : APPLE
#     Leetcode Link               : https://leetcode.com/problems/build-a-matrix-with-conditions

import sys
from collections import defaultdict, deque
from typing import List

sys.setrecursionlimit(10000)


# ************************************ C++ (ported to Python) ************************************
# Approach-1 (Topological Sorting using DFS)
# T.C : O(k*^2 + n)
# S.C : O(k*^2 + n)
class Solution:

    def topoSort(self, edges: List[List[int]], n: int) -> List[int]:
        adj = defaultdict(list)
        st = []  # list used as stack
        order = []
        # 0 : not visited;
        # 1 : visiting (currently in stack via some other DFS)
        # 2 : visited
        visited = [0] * (n + 1)
        hasCycle = [False]  # bool& in C++ -> one-element list

        for edge in edges:
            u = edge[0]
            v = edge[1]
            adj[u].append(v)

        for i in range(1, n + 1):
            if visited[i] == 0:
                self.dfs(i, adj, visited, st, hasCycle)
                if hasCycle[0]:
                    return []  # no ordering possible

        while st:
            order.append(st.pop())
        return order

    def dfs(self, node: int, adj, visited: List[int], st: List[int], hasCycle: List[bool]):

        visited[node] = 1  # Mark node as visiting
        # First, visit node's children
        for nbr in adj[node]:
            if visited[nbr] == 0:
                self.dfs(nbr, adj, visited, st, hasCycle)
            elif visited[nbr] == 1:
                # Cycle detected
                hasCycle[0] = True
                return

        visited[node] = 2  # visited
        st.append(node)  # Now node can be added

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        orderRows = self.topoSort(rowConditions, k)
        orderColumns = self.topoSort(colConditions, k)

        # We might have found cycle. That's why topo order is empty
        if not orderRows or not orderColumns:
            return []

        matrix = [[0] * k for _ in range(k)]
        for i in range(k):
            for j in range(k):
                if orderRows[i] == orderColumns[j]:
                    matrix[i][j] = orderRows[i]
        return matrix


Approach1 = Solution


# Approach-2 (Topological Sorting using BFS)
# T.C : O(k*^2 + n)
# S.C : O(k*^2 + n)
class Solution:

    def topoSort(self, edges: List[List[int]], n: int) -> List[int]:
        adj = [[] for _ in range(n + 1)]
        indegree = [0] * (n + 1)
        order = []
        for edge in edges:
            u = edge[0]
            v = edge[1]
            adj[u].append(v)
            indegree[v] += 1

        que = deque()
        count = 0
        # Push all integers with in-degree 0 in the queue.
        for i in range(1, n + 1):
            if indegree[i] == 0:
                que.append(i)
                count += 1

        while que:
            u = que.popleft()
            order.append(u)

            for v in adj[u]:
                indegree[v] -= 1

                if indegree[v] == 0:
                    que.append(v)
                    count += 1

        if count != n:
            return []  # cycle

        return order

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        orderRows = self.topoSort(rowConditions, k)
        orderColumns = self.topoSort(colConditions, k)

        # We might have found cycle. That's why topo order is empty
        if not orderRows or not orderColumns:
            return []

        matrix = [[0] * k for _ in range(k)]
        for i in range(k):
            for j in range(k):
                if orderRows[i] == orderColumns[j]:
                    matrix[i][j] = orderRows[i]
        return matrix


Approach2 = Solution

if __name__ == "__main__":
    for A in (Approach1, Approach2):
        m = A().buildMatrix(3, [[1, 2], [3, 2]], [[2, 1], [3, 2]])
        pos = {m[i][j]: (i, j) for i in range(3) for j in range(3) if m[i][j]}
        assert all(pos[a][0] < pos[b][0] for a, b in [[1, 2], [3, 2]])
        assert all(pos[a][1] < pos[b][1] for a, b in [[2, 1], [3, 2]])
        assert A().buildMatrix(3, [[1, 2], [2, 3], [3, 1], [2, 3]], [[2, 1]]) == []
    print("ok")
