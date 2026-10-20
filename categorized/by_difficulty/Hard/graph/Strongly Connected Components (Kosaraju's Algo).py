# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=E6DeC0Zpdns
# Company Tags                : Amazon, Visa
# Question Link               : https://practice.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1

import sys
from typing import List

sys.setrecursionlimit(10000)


# Kosaraju's Algorithm :     Time  : O(V+E), V = # vertices, E = # edges , Space : O(V)
class Solution:

    def dfsFill(self, u: int, adj: List[List[int]], visited: List[bool], st: List[int]):
        visited[u] = True

        for v in adj[u]:

            if not visited[v]:
                self.dfsFill(v, adj, visited, st)

        st.append(u)  # list used as stack

    def dfsTraverse(self, u: int, adjReversed: List[List[int]], visited: List[bool]):
        visited[u] = True

        for v in adjReversed[u]:

            if not visited[v]:
                self.dfsTraverse(v, adjReversed, visited)

    # Function to find number of strongly connected components in the graph.
    def kosaraju(self, V: int, adj: List[List[int]]) -> int:
        st = []
        visited = [False] * V

        for i in range(V):
            if not visited[i]:
                self.dfsFill(i, adj, visited, st)

        adjReversed = [[] for _ in range(V)]
        for u in range(V):
            for v in adj[u]:
                # u->v
                # v->u
                adjReversed[v].append(u)

        count = 0

        visited = [False] * V
        while st:
            node = st.pop()
            if not visited[node]:
                self.dfsTraverse(node, adjReversed, visited)
                count += 1

        return count


Approach1 = Solution

if __name__ == "__main__":
    adj = [[1], [2], [0, 3], [4], [5, 7], [6], [4, 7], []]
    res = Solution().kosaraju(8, adj)
    print(res)
    assert res == 4
    print("ok")
