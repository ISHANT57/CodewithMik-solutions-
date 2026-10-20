# MY YOUTUBE VIDEOS ON THIS Qn : DFS - https://www.youtube.com/watch?v=70LNE8RMPNc
#                                BFS - https://www.youtube.com/watch?v=YDMkSvNdB20
# Company Tags                 : Google, Microsoft, Amazon
# Leetcode Link                : https://leetcode.com/problems/number-of-provinces/
# GfG Link                     : https://practice.geeksforgeeks.org/problems/number-of-provinces/1

from typing import List
from collections import defaultdict, deque


# Approach-1 : [ Using DFS - Creating our own Map as graph ]
class Solution:
    def dfs(self, adj, u, visited):
        visited[u] = True

        # Visit neighbours
        for v in adj[u]:
            if not visited[v]:
                self.dfs(adj, v, visited)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        adj = defaultdict(list)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    adj[i].append(j)
                    adj[j].append(i)

        visited = [False] * n
        count = 0

        for i in range(n):
            if not visited[i]:
                count += 1
                self.dfs(adj, i, visited)

        return count


Approach1 = Solution


# Approach-2 : [ Using DFS - Using given input graph]
class Solution:
    def dfs(self, adj, u, visited):
        visited[u] = True

        # Visit neighbours
        for v in range(self.n):
            if adj[u][v] == 1 and not visited[v]:
                self.dfs(adj, v, visited)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.n = len(isConnected)

        visited = [False] * self.n
        count = 0

        for i in range(self.n):
            if not visited[i]:
                count += 1
                self.dfs(isConnected, i, visited)

        return count


Approach2 = Solution


# Approach-3 : [ Using BFS : Creating our own Map as graph ]
class Solution:
    def bfs(self, adj, u, visited):
        que = deque()
        que.append(u)
        visited[u] = True

        while que:
            u = que.popleft()

            # Visit neighbours
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    que.append(v)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        adj = defaultdict(list)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    adj[i].append(j)
                    adj[j].append(i)

        visited = [False] * n
        count = 0

        for i in range(n):
            if not visited[i]:
                self.bfs(adj, i, visited)
                count += 1

        return count


Approach3 = Solution


# Approach-4 : [ Using BFS - Using given input graph]
class Solution:
    def bfs(self, adj, u, visited):
        que = deque()
        que.append(u)
        visited[u] = True

        while que:
            u = que.popleft()

            # Visit neighbours
            for v in range(self.n):
                if adj[u][v] == 1 and not visited[v]:
                    visited[v] = True
                    que.append(v)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.n = len(isConnected)

        visited = [False] * self.n
        count = 0

        for i in range(self.n):
            if not visited[i]:
                self.bfs(isConnected, i, visited)
                count += 1

        return count


Approach4 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2, Approach3, Approach4):
        assert S().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
        assert S().findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3
    print("ok")
