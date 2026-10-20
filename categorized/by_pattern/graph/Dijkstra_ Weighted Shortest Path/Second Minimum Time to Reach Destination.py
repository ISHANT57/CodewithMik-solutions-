# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=_rnQKrA9xzA
# Company Tags                : will update soon
# Leetcode Link               : https://leetcode.com/problems/second-minimum-time-to-reach-destination/description/

from typing import List
import heapq
from collections import defaultdict, deque

INT_MAX = 2**31 - 1


# Approach-1 (Using modified Dijkstra's)
# T.C : O(E logV) - where E = number of edges and V = number of vertices
# S.C : O(V+E)
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = defaultdict(list)
        for edge in edges:
            u = edge[0]
            v = edge[1]
            adj[u].append(v)
            adj[v].append(u)

        d1 = [INT_MAX] * (n + 1)
        d2 = [INT_MAX] * (n + 1)
        pq = []  # min heap of (time, node)
        heapq.heappush(pq, (0, 1))
        d1[1] = 0

        while pq:
            timePassed, node = heapq.heappop(pq)

            if d2[n] != INT_MAX and node == n:  # We reached n 2nd time means it's the second minimum
                return d2[n]

            mult = timePassed // change
            if mult % 2 == 1:  # Red
                timePassed = change * (mult + 1)  # to set green

            for nbr in adj[node]:
                if d1[nbr] > timePassed + time:  # +time for this edge to reach nbr
                    d2[nbr] = d1[nbr]
                    d1[nbr] = timePassed + time
                    heapq.heappush(pq, (timePassed + time, nbr))
                elif d2[nbr] > timePassed + time and d1[nbr] != timePassed + time:
                    d2[nbr] = timePassed + time
                    heapq.heappush(pq, (timePassed + time, nbr))
        return -1


Approach1 = Solution


# Approach-2 (Using BFS)
# T.C : O(V + E) - where E = number of edges and V = number of vertices
# S.C : O(V+E)
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = [[] for _ in range(n + 1)]
        for edge in edges:
            u = edge[0]
            v = edge[1]
            adj[u].append(v)
            adj[v].append(u)

        d1 = [INT_MAX] * (n + 1)
        d2 = [INT_MAX] * (n + 1)
        que = deque()
        que.append((1, 1))  # Visited node 1 once
        d1[1] = 0

        while que:
            node, freq = que.popleft()

            timePassed = d1[node] if freq == 1 else d2[node]
            if d2[n] != INT_MAX and node == n:  # We reached n 2nd time means it's the second minimum
                return d2[n]

            mult = timePassed // change
            if mult % 2 == 1:  # Red
                timePassed = change * (mult + 1)  # to set green

            for nbr in adj[node]:
                if d1[nbr] == INT_MAX:
                    d1[nbr] = timePassed + time
                    que.append((nbr, 1))
                elif d2[nbr] == INT_MAX and d1[nbr] != timePassed + time:
                    d2[nbr] = timePassed + time
                    que.append((nbr, 2))
        return -1


Approach2 = Solution


if __name__ == "__main__":
    for sol in (Approach1, Approach2):
        s = sol()
        assert s.secondMinimum(5, [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], 3, 5) == 13
        assert s.secondMinimum(2, [[1, 2]], 3, 2) == 11
    print("ok")
