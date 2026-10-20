# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=CMTlE0W01Pk
# Company Tags                : AMAZON
# Leetcode Link               : https://leetcode.com/problems/similar-string-groups/

import sys
from typing import List
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)


# Approach-1 : Using DFS
class Solution:

    def isSimilar(self, s1, s2):

        n = len(s1)
        diff = 0
        for i in range(n):
            if s1[i] != s2[i]:
                diff += 1

        return diff == 2 or diff == 0

    def DFS(self, u, adj, visited):
        visited[u] = True

        for v in adj[u]:
            if not visited[v]:
                self.DFS(v, adj, visited)

    def numSimilarGroups(self, strs: List[str]) -> int:

        n = len(strs)

        # build graph
        adj = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                if self.isSimilar(strs[i], strs[j]):
                    adj[i].append(j)
                    adj[j].append(i)

        visited = [False] * n
        count = 0

        for i in range(n):
            if not visited[i]:
                self.DFS(i, adj, visited)
                count += 1

        return count


Approach1 = Solution


# Approach-2 : Using BFS
class Solution:

    def isSimilar(self, s1, s2):

        n = len(s1)
        diff = 0
        for i in range(n):
            if s1[i] != s2[i]:
                diff += 1

        return diff == 2 or diff == 0

    def BFS(self, i, adj, visited):
        que = deque()

        que.append(i)
        visited[i] = True

        while que:

            u = que.popleft()

            for v in adj[u]:
                if not visited[v]:
                    que.append(v)
                    visited[v] = True

    def numSimilarGroups(self, strs: List[str]) -> int:

        n = len(strs)

        # build graph
        adj = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                if self.isSimilar(strs[i], strs[j]):
                    adj[i].append(j)
                    adj[j].append(i)

        visited = [False] * n
        count = 0

        for i in range(n):
            if not visited[i]:
                self.BFS(i, adj, visited)
                count += 1

        return count


Approach2 = Solution


# Approach-3 (Using DSU)
# Find this in my Disjoint Set Repo
# Link - https://github.com/MAZHARMIK/Interview_DS_Algo/tree/master/Graph/Disjoint%20Set
# (only a link in the original source, no code)


if __name__ == "__main__":
    for S in (Approach1, Approach2):
        assert S().numSimilarGroups(["tars", "rats", "arts", "star"]) == 2
        assert S().numSimilarGroups(["omv", "ovm"]) == 1
    print("ok")
