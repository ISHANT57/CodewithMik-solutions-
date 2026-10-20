# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=74suJP4bwf0
# Company Tags                : Flipkart, Amazon, Microsoft, Samsung, MakeMyTrip, Oracle, Adobe, BankBazaar
# Gfg Link                    : https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1

from typing import List
from collections import deque


class Solution:
    # Function to detect cycle in a directed graph.
    def isCyclic(self, N: int, adj: List[List[int]]) -> bool:
        que = deque()
        indegree = [0] * N
        count = 0
        # 1
        for u in range(N):
            for v in adj[u]:
                indegree[v] += 1

        # 2. Fill que, indegree with 0
        for i in range(N):
            if indegree[i] == 0:
                que.append(i)
                count += 1

        # 3. Simple BFS
        while que:
            u = que.popleft()

            for v in adj[u]:
                indegree[v] -= 1

                if indegree[v] == 0:
                    que.append(v)
                    count += 1

        return count != N


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().isCyclic(4, [[1], [2], [3], [1]]) == True
    assert Solution().isCyclic(4, [[1], [2], [3], []]) == False
    print("ok")
