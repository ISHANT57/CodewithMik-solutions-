#       MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=hptQEIpvaxM
#       Company Tags                : GOOGLE, Akuna Capital
#       Leetcode Link               : https://leetcode.com/problems/network-delay-time/

from typing import List
from collections import defaultdict
import heapq

INT_MAX = 2**31 - 1
INT_MIN = -2**31

# Just copy paste the Dijkstra'a Code and Find the maximum amongst the minimums in result vector
# But, Why maximum ?
# Because, we have to return the minimum time it takes for all the n nodes to receive the signal
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = defaultdict(list)
        for vec in times:

            u = vec[0]
            v = vec[1]
            w = vec[2]

            adj[u].append((v, w))

        pq = []  # min-heap of (dist, node)

        result = [INT_MAX] * (n+1)

        result[k] = 0
        heapq.heappush(pq, (0, k))

        while pq:

            d, node = heapq.heappop(pq)

            for adjNode, dist in adj[node]:

                if d + dist < result[adjNode]:

                    result[adjNode] = d + dist
                    heapq.heappush(pq, (d+dist, adjNode))

        ans = INT_MIN

        for i in range(1, n+1):
            ans = max(ans, result[i])

        return -1 if ans == INT_MAX else ans

Approach1 = Solution


if __name__ == "__main__":
    s = Solution()
    assert s.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2
    assert s.networkDelayTime([[1, 2, 1]], 2, 1) == 1
    assert s.networkDelayTime([[1, 2, 1]], 2, 2) == -1
    print("ok")
