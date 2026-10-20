#         Scroll below to see JAVA code as well (Java sections skipped in this Python port)
#
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=Vn-voe1XNtQ
#     Company Tags                : <soon>
#     Leetcode Link               : https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

from typing import List
from collections import deque

INT_MAX = 2**31 - 1


# ****************************************************************** C++ (ported to Python) ******************************************************************
# Approach-1 (BFS)
# T.C : O(V+E), V = number of vertices and E = number of edges
# S.C : O(n)
class Solution:
    def __init__(self):
        self.n = 0

    def bfs(self, edges: List[int], startNode: int, dist_node: List[int]) -> None:
        que = deque()
        que.append(startNode)
        dist_node[startNode] = 0
        visited = [False] * self.n
        visited[startNode] = True

        while que:
            u = que.popleft()

            v = edges[u]

            if v != -1 and not visited[v]:
                visited[v] = True
                dist_node[v] = 1 + dist_node[u]
                que.append(v)

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        self.n = len(edges)
        n = self.n

        dist1 = [INT_MAX] * n
        dist2 = [INT_MAX] * n

        self.bfs(edges, node1, dist1)
        self.bfs(edges, node2, dist2)

        minDistNode = -1
        minDistTillNow = INT_MAX
        for i in range(n):

            maxD = max(dist1[i], dist2[i])

            if minDistTillNow > maxD:
                minDistNode = i
                minDistTillNow = maxD

        return minDistNode


Approach1 = Solution


# Approach-2 (DFS)
# T.C : O(V+E), V = number of vertices and E = number of edges
# S.C : O(n)
class Solution:
    def __init__(self):
        self.n = 0

    def dfs(self, edges: List[int], startNode: int, dist_node: List[int], visited: List[bool]) -> None:
        visited[startNode] = True

        v = edges[startNode]

        if v != -1 and not visited[v]:
            visited[v] = True
            dist_node[v] = 1 + dist_node[startNode]
            self.dfs(edges, v, dist_node, visited)

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        self.n = len(edges)
        n = self.n

        dist1 = [INT_MAX] * n
        dist2 = [INT_MAX] * n
        visited1 = [False] * n
        visited2 = [False] * n
        dist1[node1] = 0
        dist2[node2] = 0

        self.dfs(edges, node1, dist1, visited1)
        self.dfs(edges, node2, dist2, visited2)

        minDistNode = -1
        minDistTillNow = INT_MAX
        for i in range(n):

            maxD = max(dist1[i], dist2[i])

            if minDistTillNow > maxD:
                minDistNode = i
                minDistTillNow = maxD

        return minDistNode


Approach2 = Solution


if __name__ == "__main__":
    for cls in (Approach1, Approach2):
        assert cls().closestMeetingNode([2, 2, 3, -1], 0, 1) == 2
        assert cls().closestMeetingNode([1, 2, -1], 0, 2) == 2
    print("ok")
