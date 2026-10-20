#       MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=i8h_O6u3DSc
#       Company Tags                : Google (Variation)
#       Leetcode/GfG Link           : https://practice.geeksforgeeks.org/problems/euler-circuit-and-path/1

import sys
from typing import List

sys.setrecursionlimit(10000)


# ************************************************ C++ ************************************************************
class Solution:

    def DFS(self, adj: List[List[int]], u: int, visited: List[bool]) -> None:
        visited[u] = True

        for it in adj[u]:
            if visited[it] == False:
                self.DFS(adj, it, visited)

    def isConnected(self, V: int, adj: List[List[int]]) -> bool:
        visited = [False] * V

        # Find a vertex with non-zero degree
        nonZeroDegreeVertex = -1
        for i in range(V):
            if len(adj[i]) != 0:
                nonZeroDegreeVertex = i
                break

        # Start DFS traversal from a vertex with non-zero degree
        self.DFS(adj, nonZeroDegreeVertex, visited)

        # Check if all non-zero degree vertices are visited
        for i in range(V):
            if visited[i] == False and len(adj[i]) > 0:
                return False
        return True

    def isEularCircuit(self, V: int, adj: List[List[int]]) -> int:

        # Check if all non-zero degree vertices are connected
        if self.isConnected(V, adj) == False:
            return 0  # Non-Eulerian

        # Count vertices with odd degree
        oddCount = 0
        for i in range(V):
            if len(adj[i]) % 2 != 0:
                oddCount += 1

        # If count is more than 2, then graph is not Eulerian
        if oddCount > 2:
            return 0  # Non-Eulerian

        if oddCount == 2:
            return 1  # Semi-Eulerian (It has only Euler Path)

        return 2  # (Euler Circuit)


Approach1 = Solution


if __name__ == "__main__":
    s = Solution()
    assert s.isEularCircuit(3, [[1, 2], [0, 2], [0, 1]]) == 2  # triangle
    assert s.isEularCircuit(3, [[1], [0, 2], [1]]) == 1        # path
    assert s.isEularCircuit(4, [[1, 2, 3], [0], [0], [0]]) == 0  # star: 4 odd vertices
    print("ok")
