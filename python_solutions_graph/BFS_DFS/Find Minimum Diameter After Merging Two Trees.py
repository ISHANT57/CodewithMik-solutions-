#                        Scroll down to see JAVA code also (Java section skipped in this Python port)
#
#     MY YOUTUBE VIDEO ON THIS Qn  : https://www.youtube.com/watch?v=uz_WISpySFs
#     Company Tags                 : will update
#     Leetcode Link                : https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees
#
#     Similar Medium Problem : Leetcode-1245 : Tree Diameter
#     Video Link - https://www.youtube.com/watch?v=na3LE8CBYLo

from typing import List, Tuple
from collections import defaultdict, deque


# ********************************************************************** C++ (ported to Python) **********************************************************************
# Approach (Using BFS)
# T.C : O(V+E)
# S.C : O(V+E)
class Solution:
    def __init__(self):
        self.n = 0

    def BFS(self, adj, source: int) -> Tuple[int, int]:
        que = deque()
        que.append(source)

        visited = defaultdict(bool)  # unordered_map<int, bool>
        visited[source] = True

        distance = 0
        farthestNode = source

        while que:
            size = len(que)  # current level me itne nodes hain

            for _ in range(size):
                curr = que.popleft()

                farthestNode = curr

                for nbr in adj[curr]:
                    if visited[nbr] == False:
                        visited[nbr] = True
                        que.append(nbr)

            if que:
                distance += 1

        return (farthestNode, distance)

    def findDiameter(self, adj) -> int:
        # step-1 find the farthest node from a random node - 0
        farthestNode, dist = self.BFS(adj, 0)

        # step-2 : the farthestNode we got above is nothing but one end of the diameter of adj

        # step-3 : Find the farthestnode from the node we got above , that will be the other end of diameter - diameter
        otherEndNode, diameter = self.BFS(adj, farthestNode)

        return diameter

    def buildAdj(self, edges: List[List[int]]):
        adj = defaultdict(list)

        for edge in edges:
            u = edge[0]
            v = edge[1]
            adj[u].append(v)
            adj[v].append(u)
        return adj

    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        adj1 = self.buildAdj(edges1)
        adj2 = self.buildAdj(edges2)

        d1 = self.findDiameter(adj1)
        d2 = self.findDiameter(adj2)

        combined = (d1 + 1) // 2 + (d2 + 1) // 2 + 1

        return max(d1, d2, combined)


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().minimumDiameterAfterMerge([[0, 1], [0, 2], [0, 3]], [[0, 1]]) == 3
    e = [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]]
    assert Solution().minimumDiameterAfterMerge(e, e) == 5
    print("ok")
