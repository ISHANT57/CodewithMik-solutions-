# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=W1xTqEcoSkI
# Company Tags                : will update later
# Leetcode Link               : https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii

import sys
from collections import defaultdict
from typing import List

sys.setrecursionlimit(10**6)

# ****************************************************************** C++ ******************************************************************
# Approach (Using DFS and Marking Nodes)
# T.C : O(V+E)
# S.C : O(V+E)
class Solution:
    def getAdj(self, edges: List[List[int]]):
        adj = defaultdict(list)  # unordered_map<int, vector<int>>
        for edge in edges:
            u = edge[0]
            v = edge[1]

            adj[u].append(v)
            adj[v].append(u)

        return adj

    # O(V+E)
    # counts = [zeroMarkedCount, oneMarkedCount] (C++ passed these by reference)
    def dfs(self, curr: int, adj, parent: int, mark: List[int], counts: List[int]) -> None:

        if mark[curr] == 0:
            counts[0] += 1
        else:
            counts[1] += 1

        for ngbr in adj[curr]:
            if ngbr != parent:
                mark[ngbr] = 1 if mark[curr] == 0 else 0  # alternate marking
                self.dfs(ngbr, adj, curr, mark, counts)

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        N = len(edges1) + 1  # Tree A
        M = len(edges2) + 1  # Tree B

        adjA = self.getAdj(edges1)  # O(V1+E1)
        adjB = self.getAdj(edges2)  # O(V2+E2)

        markA = [-1] * N
        markA[0] = 0  # mark 0th node as 0
        countsA = [0, 0]  # zeroMarkedCountA, oneMarkedCountA
        self.dfs(0, adjA, -1, markA, countsA)  # O(V+E)
        zeroMarkedCountA, oneMarkedCountA = countsA

        markB = [-1] * M
        markB[0] = 0  # mark 0th node as 0
        countsB = [0, 0]  # zeroMarkedCountB, oneMarkedCountB
        self.dfs(0, adjB, -1, markB, countsB)  # O(V+E)
        zeroMarkedCountB, oneMarkedCountB = countsB

        maxFromTree2 = max(zeroMarkedCountB, oneMarkedCountB)

        result = [0] * N
        for i in range(N):  # O(V)
            result[i] = (zeroMarkedCountA if markA[i] == 0 else oneMarkedCountA) + maxFromTree2

        return result

Approach1 = Solution


if __name__ == "__main__":
    assert Solution().maxTargetNodes([[0,1],[0,2],[2,3],[2,4]], [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]) == [8,7,7,8,8]
    assert Solution().maxTargetNodes([[0,1],[0,2],[0,3],[0,4]], [[0,1],[1,2],[2,3]]) == [3,6,6,6,6]
    print("ok")
