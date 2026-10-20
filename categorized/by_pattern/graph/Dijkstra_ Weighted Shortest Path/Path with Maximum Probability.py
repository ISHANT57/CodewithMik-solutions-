# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=zTM9k6jqpXI
# Company Tags                : GOOGLE
# Leetcode Link               : https://leetcode.com/problems/path-with-maximum-probability/

from typing import List
import heapq
from collections import defaultdict


# Using Dijkstra's Algorithm
# T.C : O(E*log(V))
# S.C : O(V + E)
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = defaultdict(list)
        result = [0.0] * n

        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]
            prob = succProb[i]
            adj[u].append((v, prob))
            adj[v].append((u, prob))

        pq = []  # max heap because we need maximum probability (heapq is min-heap, so probability is negated)

        result[start] = 1
        heapq.heappush(pq, (-1.0, start))

        while pq:
            curProb, curnode = heapq.heappop(pq)
            curProb = -curProb

            for child in adj[curnode]:
                if result[child[0]] < curProb * child[1]:  # we want maximum this time
                    result[child[0]] = curProb * child[1]
                    heapq.heappush(pq, (-result[child[0]], child[0]))

        return result[end]


Approach1 = Solution


if __name__ == "__main__":
    s = Solution()
    assert abs(s.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2) - 0.25) < 1e-5
    assert s.maxProbability(3, [[0, 1]], [0.5], 0, 2) == 0
    print("ok")
