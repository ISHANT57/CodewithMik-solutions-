# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=VmUpydhNmuw
# Company Tags                : GOOGLE
# Leetcode Link               : https://leetcode.com/problems/cheapest-flights-within-k-stops/
# GfG Link                    : https://practice.geeksforgeeks.org/problems/cheapest-flights-within-k-stops/1

from typing import List
from collections import deque, defaultdict

INT_MAX = 2**31 - 1


# Approach-1 (BFS)
# T.C : O(V+E) - BFS traversal of Graph
# S.C : O(V+E)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distance = [INT_MAX] * n

        adj = defaultdict(list)  # unordered_map<int, vector<pair<int, int>>>

        for vec in flights:
            u    = vec[0]
            v    = vec[1]
            cost = vec[2]

            adj[u].append((v, cost))

        que = deque()
        que.append((src, 0))
        distance[src] = 0

        level = 0

        while que and level <= k:
            N = len(que)

            while N > 0:
                N -= 1
                u, d = que.popleft()

                for P in adj[u]:

                    v    = P[0]
                    cost = P[1]

                    if distance[v] > d + cost:
                        distance[v] = d + cost
                        que.append((v, d + cost))

            level += 1

        return -1 if distance[dst] == INT_MAX else distance[dst]


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1) == 700
    assert Solution().findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1) == 200
    assert Solution().findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0) == 500
    print("ok")
