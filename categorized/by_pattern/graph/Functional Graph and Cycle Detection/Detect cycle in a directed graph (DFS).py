# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=K_LamGUvwUc
# Company Tags                : Flipkart, Amazon, Microsoft, Samsung, MakeMyTrip, Oracle, Adobe, BankBazaar
# Gfg Link                    : https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1

from typing import List


class Solution:

    def isCycleDFS(self, adj: List[List[int]], u: int, visited: List[bool], inRecursion: List[bool]) -> bool:
        visited[u] = True
        inRecursion[u] = True

        for v in adj[u]:
            # if not visited, then we check for cycle in DFS
            if visited[v] == False and self.isCycleDFS(adj, v, visited, inRecursion):
                return True
            elif inRecursion[v] == True:
                return True

        inRecursion[u] = False
        return False

    # Function to detect cycle in a directed graph.
    def isCyclic(self, V: int, adj: List[List[int]]) -> bool:
        visited = [False] * V
        inRecursion = [False] * V

        for i in range(V):
            if not visited[i] and self.isCycleDFS(adj, i, visited, inRecursion):
                return True

        return False


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().isCyclic(4, [[1], [2], [3], [1]]) == True
    assert Solution().isCyclic(4, [[1], [2], [3], []]) == False
    print("ok")
