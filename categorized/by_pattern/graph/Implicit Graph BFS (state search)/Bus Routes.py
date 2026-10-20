# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=uDbr-6svYKw
# Company Tags                : Uber
# Leetcode Link               : https://leetcode.com/problems/bus-routes/

from typing import List
from collections import deque, defaultdict


# Approach- (Using BFS)
# T.C : O(m^2 * k) - m is the size of routes, and k is the maximum size of routes[i].
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        adj = defaultdict(list)  # unordered_map<int, vector<int>>

        for route in range(len(routes)):
            for stop in routes[route]:
                adj[stop].append(route)

        que = deque()
        visited = [False] * 501

        for route in adj[source]:
            que.append(route)
            visited[route] = True

        busCount = 1
        while que:
            size = len(que)

            while size > 0:
                size -= 1
                route = que.popleft()

                for stop in routes[route]:

                    if stop == target:
                        return busCount

                    for nextRoute in adj[stop]:
                        if not visited[nextRoute]:
                            visited[nextRoute] = True
                            que.append(nextRoute)

            busCount += 1
        return -1


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6) == 2
    assert Solution().numBusesToDestination([[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12) == -1
    print("ok")
