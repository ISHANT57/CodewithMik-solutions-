#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=ElXqjhZoUC0
#     Company Tags                : Will update soon
#     Leetcode Link               : https://leetcode.com/problems/valid-arrangement-of-pairs

import sys
from collections import defaultdict
from typing import List

sys.setrecursionlimit(1000000)


# ************************************************************ C++ ************************************************
# Approach-1 (DFS Using Stack) - Hierholzer's Algorithm to find Euler Path
# T.C : O(V+E) for normal DFS
# S.C : O(V+E)
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # Step-1 Build adjacency list - Graph
        adj = defaultdict(list)

        # build  indegree and outdegree
        indegree = defaultdict(int)
        outdegree = defaultdict(int)
        # key - node
        # value - indegree/outdegree

        for edge in pairs:
            u = edge[0]
            v = edge[1]

            adj[u].append(v)  # u --> v
            outdegree[u] += 1
            indegree[v] += 1

        # Find the startNode of the Euler Path
        startNode = pairs[0][0]
        for node in list(adj.keys()):
            if outdegree[node] - indegree[node] == 1:
                startNode = node
                break

        # Simply do the Khandani DFS
        EulerPath = []  # to store my eulerpath
        st = []  # to perform dfs
        st.append(startNode)

        while st:
            curr = st[-1]
            if adj[curr]:
                ngbr = adj[curr].pop()
                st.append(ngbr)
            else:
                EulerPath.append(curr)
                st.pop()

        # Build your result
        EulerPath.reverse()
        result = []
        for i in range(len(EulerPath) - 1):
            result.append([EulerPath[i], EulerPath[i + 1]])

        return result


Approach1 = Solution


# Approach-2 (DFS Using Recursion) - Hierholzer's Algorithm to find Euler Path
# T.C : O(V+E) for normal DFS
# S.C : O(V+E)
class Solution:
    def __init__(self):
        # Adjacency list
        self.adj = defaultdict(list)

        # Vector to store the Eulerian path
        self.eulerPath = []

    # Recursive DFS function to find the Eulerian path
    def dfs(self, node: int) -> None:
        while self.adj[node]:
            nextNode = self.adj[node].pop()  # Remove the edge after visiting
            self.dfs(nextNode)               # Recursive DFS call
        self.eulerPath.append(node)  # Add node to Euler path after all edges are visited

    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # Step-1: Build adjacency list and calculate in-degree & out-degree
        indegree = defaultdict(int)
        outdegree = defaultdict(int)

        for edge in pairs:
            u = edge[0]
            v = edge[1]
            self.adj[u].append(v)  # u --> v
            outdegree[u] += 1
            indegree[v] += 1

        # Step-2: Find the start node of the Eulerian path
        startNode = pairs[0][0]  # default start node
        for node in list(self.adj.keys()):
            if outdegree[node] - indegree[node] == 1:
                startNode = node  # Node with outdegree > indegree by 1
                break

        # Step-3: Perform DFS from the start node to find the Eulerian path
        self.dfs(startNode)

        # Step-4: Build the result from the Eulerian path
        self.eulerPath.reverse()
        result = []
        for i in range(len(self.eulerPath) - 1):
            result.append([self.eulerPath[i], self.eulerPath[i + 1]])

        return result


Approach2 = Solution


if __name__ == "__main__":
    def valid(pairs, res):
        if sorted(map(tuple, pairs)) != sorted(map(tuple, res)):
            return False
        return all(res[i][1] == res[i + 1][0] for i in range(len(res) - 1))

    for S in (Approach1, Approach2):
        for pairs in ([[5, 1], [4, 5], [11, 9], [9, 4]], [[1, 3], [3, 2], [2, 1]], [[1, 2], [1, 3], [2, 1]]):
            assert valid(pairs, S().validArrangement([p[:] for p in pairs]))
    print("ok")
