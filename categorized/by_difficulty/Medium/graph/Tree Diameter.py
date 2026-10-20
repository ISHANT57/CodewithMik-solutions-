# MY YOUTUBE VIDEO ON THIS Qn  : https://www.youtube.com/watch?v=na3LE8CBYLo
# Company Tags                 : GOOGLE, META
# Leetcode Link                : https://leetcode.com/problems/tree-diameter/description/
# Hard Version of This Problem : https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees
#
# Leetcode-1245 : Tree Diameter
# Given an undirected tree, return its diameter: the number of edges in a longest path in that tree.
# The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge between nodes u and v.
# Each node has labels in the set {0, 1, ..., edges.length}.
# (Java duplicate section of the original file is skipped)

from typing import List
from collections import defaultdict, deque


# ***************************************************** C++ (Python port) *****************************************************
# Approach (Using BFS)
# T.C : O(V+E)
# S.C : O(V+E)
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        # Number of nodes in the tree
        n = len(edges) + 1

        # Build adjacency list
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        # Find the diameter of the tree
        return self.findDiameter(n, adj)

    # Function to find the diameter of a tree using two BFS calls
    def findDiameter(self, n, adj):
        # First BFS to find the farthest node from any arbitrary node (e.g., 0)
        farthestNode, _ = self.findFarthestNode(n, adj, 0)

        # Second BFS from the farthest node to determine the diameter
        _, diameter = self.findFarthestNode(n, adj, farthestNode)
        return diameter

    # BFS helper function to find the farthest node and its distance from the source
    def findFarthestNode(self, n, adj, sourceNode):
        que = deque()
        visited = [False] * n

        # Push source node into the queue
        que.append(sourceNode)
        visited[sourceNode] = True

        maximumDistance = 0
        farthestNode = sourceNode

        # Explore neighbors
        while que:
            size = len(que)
            for i in range(size):
                currentNode = que.popleft()
                # Update farthest node
                farthestNode = currentNode

                for neighbor in adj[currentNode]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        que.append(neighbor)
            if que:
                maximumDistance += 1
        return (farthestNode, maximumDistance)


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().treeDiameter([[0, 1], [0, 2]]) == 2
    assert Solution().treeDiameter([[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]) == 4
    print("ok")
