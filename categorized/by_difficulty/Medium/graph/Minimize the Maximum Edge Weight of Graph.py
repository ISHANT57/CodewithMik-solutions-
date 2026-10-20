# MY YOUTUBE VIDEO ON THIS Qn  : https://www.youtube.com/watch?v=B5aIqLq50_8
# Company Tags                 : will update
# Leetcode Link                : https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/

from typing import List
from collections import deque, defaultdict


# ********************************************************************** C++ **********************************************************************
# Approach-1 (Using BFS)
# T.C : O(log(maxWt) * (V+E))
# S.C : O(V+E)
class Solution:
    # typedef pair<int, int> P  -> tuple (node, weight)

    def canAllReachZero(self, n: int, adj, mid: int) -> bool:
        # BFS
        que = deque()
        visited = [False] * n

        que.append(0)
        visited[0] = True

        while que:
            u = que.popleft()

            for p in adj[u]:
                v = p[0]  # ngbr node
                w = p[1]  # edge weight

                if w <= mid and not visited[v]:
                    visited[v] = True
                    que.append(v)

        for i in range(n):
            if visited[i] == False:  # this ith node was not visited
                return False  # we could not visit all the nodes

        return True

    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        adj = defaultdict(list)
        # u -> {(v1, w1), (v2,w2),... }

        maxWt = 0
        # Form the adj with reversed edge
        for edge in edges:
            u = edge[0]
            v = edge[1]
            w = edge[2]

            adj[v].append((u, w))  # with reversed edge
            maxWt = max(maxWt, w)

        # apply binary search on answer (weight)
        result = 2**31 - 1  # INT_MAX  invalid answer

        l = 0
        r = maxWt

        while l <= r:
            mid = l + (r - l) // 2

            if self.canAllReachZero(n, adj, mid) == True:
                result = mid
                r = mid - 1
            else:
                l = mid + 1

        return -1 if result == 2**31 - 1 else result


Approach1 = Solution


# Approach-2 (Using DFS)
# T.C : O(log(maxWt) * (V+E))
# S.C : O(V+E)
class Solution:

    # typedef pair<int, int> P  -> tuple (node, weight)

    def dfs(self, u: int, adj, mid: int, visited: List[bool]) -> None:
        visited[u] = True

        # visit all ngbrs of u if possible
        for p in adj[u]:
            v = p[0]
            w = p[1]

            if w <= mid and not visited[v]:
                visited[v] = True
                self.dfs(v, adj, mid, visited)

    def canAllReachZero(self, n: int, adj, mid: int) -> bool:
        # DFS
        visited = [False] * n
        self.dfs(0, adj, mid, visited)

        for i in range(n):
            if visited[i] == False:
                return False

        return True

    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        adj = defaultdict(list)
        # u -> {(v1, w1), (v2,w2),... }

        maxWt = 0
        # Form the adj with reversed edge
        for edge in edges:
            u = edge[0]
            v = edge[1]
            w = edge[2]

            adj[v].append((u, w))  # with reversed edge
            maxWt = max(maxWt, w)

        # apply binary search on answer (weight)
        result = 2**31 - 1  # INT_MAX  invalid answer

        l = 0
        r = maxWt

        # T.C : O(log(maxWt) * (V+E))
        # S.C : O(V+E)
        while l <= r:
            mid = l + (r - l) // 2

            if self.canAllReachZero(n, adj, mid) == True:  # O(V+E) due to BFS or DFS
                result = mid
                r = mid - 1
            else:
                l = mid + 1

        return -1 if result == 2**31 - 1 else result


Approach2 = Solution

# (The Java section of the original file duplicates the above and is skipped.)


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10**6)
    e = [[1,0,1],[2,0,2],[3,0,1],[4,3,1],[2,1,1]]
    assert Approach1().minMaxWeight(5, e, 2) == 1
    assert Approach2().minMaxWeight(5, e, 2) == 1
    assert Approach1().minMaxWeight(5, [[0,1,1],[0,2,2],[0,3,1],[0,4,1],[1,2,1]], 1) == -1
    print("ok")
