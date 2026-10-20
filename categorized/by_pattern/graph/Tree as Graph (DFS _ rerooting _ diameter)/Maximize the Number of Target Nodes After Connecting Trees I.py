# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=tGtXUkUbYfo
# Company Tags                : will update later
# Leetcode Link               : https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i

from typing import List
from collections import deque, defaultdict


# ****************************************************************** C++ ******************************************************************
# Approach-1 (Using BFS)
# T.C : O(V*(V+E))
# S.C : O(V+E)
class Solution:

    def bfs(self, curr: int, adj, d: int, N: int) -> int:

        que = deque()
        que.append((curr, 0))
        visited = [False] * N
        visited[curr] = True

        count = 0  # count the target nodes
        while que:
            currNode, dist = que.popleft()

            if dist > d:
                continue

            count += 1  # include current node in targetNodes count
            # visit neighbors of currNode
            for ngbr in adj[currNode]:
                if not visited[ngbr]:
                    visited[ngbr] = True
                    que.append((ngbr, dist + 1))

        return count

    def findCount(self, edges: List[List[int]], d: int) -> List[int]:
        N = len(edges) + 1

        # adjacency list
        adj = defaultdict(list)
        for edge in edges:
            u = edge[0]
            v = edge[1]
            adj[u].append(v)
            adj[v].append(u)

        result = [0] * N
        for i in range(N):
            result[i] = self.bfs(i, adj, d, N)

        return result

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        # Tree 1 me kitne nodes hain
        N = len(edges1) + 1

        result1 = self.findCount(edges1, k)  # stores targetnodes count from each node within tree1 within k distance
        result2 = self.findCount(edges2, k - 1)  # stores targetnodes count from each node within tree2 within k-1 distance

        maxTargetNodesCount = max(result2)

        for i in range(len(result1)):
            result1[i] += maxTargetNodesCount

        return result1


Approach1 = Solution


# Approach-2 (Using DFS)
# T.C : O(V*(V+E))
# S.C : O(V+E)
class Solution:

    def dfs(self, curr: int, adj, d: int, currNodeKaParent: int) -> int:
        if d < 0:
            return 0

        count = 1  # counting current node as 1

        for ngbr in adj[curr]:
            if ngbr != currNodeKaParent:
                count += self.dfs(ngbr, adj, d - 1, curr)

        return count

    def findCount(self, edges: List[List[int]], d: int) -> List[int]:
        N = len(edges) + 1

        # adjacency list
        adj = defaultdict(list)
        for edge in edges:
            u = edge[0]
            v = edge[1]
            adj[u].append(v)
            adj[v].append(u)

        result = [0] * N
        for i in range(N):
            result[i] = self.dfs(i, adj, d, -1)

        return result

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        # Tree 1 me kitne nodes hain
        N = len(edges1) + 1

        result1 = self.findCount(edges1, k)  # stores targetnodes count from each node within tree1 within k distance
        result2 = self.findCount(edges2, k - 1)  # stores targetnodes count from each node within tree2 within k-1 distance

        maxTargetNodesCount = max(result2)

        for i in range(len(result1)):
            result1[i] += maxTargetNodesCount

        return result1


Approach2 = Solution

# (The Java section of the original file duplicates the above and is skipped.)


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10**6)
    e1 = [[0,1],[0,2],[2,3],[2,4]]
    e2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
    assert Approach1().maxTargetNodes(e1, e2, 2) == [9, 7, 9, 8, 8]
    assert Approach2().maxTargetNodes(e1, e2, 2) == [9, 7, 9, 8, 8]
    print("ok")
