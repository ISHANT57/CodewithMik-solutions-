# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=yYBKsu27f2s
# Company Tags                : Microsoft, Flipkart, Samsung,
# Leetcode Link               : https://leetcode.com/problems/possible-bipartition/

from typing import List
from collections import defaultdict, deque


# Using BFS - O(V+E)
class Solution:
    def isBipartite(self, adj, node: int, color: List[int]) -> bool:
        que = deque()

        que.append(node)
        color[node] = 1

        while que:
            u = que.popleft()

            for v in adj[u]:
                if color[v] == color[u]:
                    return False

                if color[v] == -1:
                    color[v] = 1 - color[u]
                    que.append(v)
        return True

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for vec in dislikes:
            u = vec[0]
            v = vec[1]

            adj[u].append(v)
            adj[v].append(u)

        color = [-1] * (n + 1)

        for i in range(1, n + 1):
            if color[i] == -1:
                if not self.isBipartite(adj, i, color):
                    return False

        return True


Approach1 = Solution


# Using DFS - O(V+E):(SOON)
# (not written in the original file)

if __name__ == "__main__":
    assert Solution().possibleBipartition(4, [[1, 2], [1, 3], [2, 4]]) == True
    assert Solution().possibleBipartition(3, [[1, 2], [1, 3], [2, 3]]) == False
    assert Solution().possibleBipartition(5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]) == False
    print("ok")
