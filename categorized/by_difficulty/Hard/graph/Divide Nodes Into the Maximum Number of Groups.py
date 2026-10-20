#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=Iku-NBN2jRE
#     Company Tags                : Will update soon
#     Leetcode Link               : https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups

import sys
from collections import deque, defaultdict
from typing import List

sys.setrecursionlimit(10000)


# ************************************************************ C++ ************************************************
# Approach - Using Bipartite, DFS and BFS
# T.C : O(V * (V+E))
# S.C : O(V+E)
class Solution:
    # 1 : Red
    # 0 : Green
    def isBipartite(self, adj, curr: int, colors: List[int], currColor: int) -> bool:
        colors[curr] = currColor

        for ngbr in adj[curr]:
            if colors[ngbr] == colors[curr]:
                return False

            if colors[ngbr] == -1:
                if self.isBipartite(adj, ngbr, colors, 1 - currColor) == False:
                    return False

        return True

    def bfs(self, adj, currNode: int, n: int) -> int:
        que = deque()
        visited = [False] * n
        que.append(currNode)
        visited[currNode] = True

        level = 1  # max groups in that components
        while que:

            size = len(que)
            while size > 0:
                size -= 1
                curr = que.popleft()

                for ngbr in adj[curr]:
                    if visited[ngbr]:
                        continue

                    que.append(ngbr)
                    visited[ngbr] = True

            level += 1  # 1 extra will be incremeented in the last loop

        return level - 1

    def getMaxFromEachComp(self, adj, curr: int, visited: List[bool], levels: List[int]) -> int:
        maxGrp = levels[curr]
        visited[curr] = True

        for ngbr in adj[curr]:
            if not visited[ngbr]:
                maxGrp = max(maxGrp, self.getMaxFromEachComp(adj, ngbr, visited, levels))

        return maxGrp

    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)  # O(V+E) space

        for edge in edges:
            u = edge[0] - 1  # converting to 0-based idnex
            v = edge[1] - 1

            adj[u].append(v)
            adj[v].append(u)

        # Bipartite check
        colors = [-1] * n  # O(V)
        # O(V*(V+E))
        for node in range(n):  # O(n)
            if colors[node] == -1:
                if self.isBipartite(adj, node, colors, 1) == False:  # O(V+E)
                    return -1

        # BFS karke max levels nikalo for each node
        levels = [0] * n
        # T.C :O(V * (V+E))
        for node in range(n):  # O(V)
            levels[node] = self.bfs(adj, node, n)  # O(V+E)

        maxGroupEachComp = 0
        visited = [False] * n
        for node in range(n):  # O(V * (V+E))
            if not visited[node]:
                maxGroupEachComp += self.getMaxFromEachComp(adj, node, visited, levels)

        return maxGroupEachComp


Approach1 = Solution


if __name__ == "__main__":
    s = Solution()
    assert s.magnificentSets(6, [[1, 2], [1, 4], [1, 5], [2, 6], [2, 3], [4, 6]]) == 4
    assert s.magnificentSets(3, [[1, 2], [2, 3], [3, 1]]) == -1
    print("ok")
