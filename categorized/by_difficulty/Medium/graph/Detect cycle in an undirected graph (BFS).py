# Company Tags  : Flipkart, Amazon, Samsung, MakeMyTrip, Oracle, Adobe
# Question Link : https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

from typing import List
from collections import deque


# Using Queue of Pair {node, parent_of_node}
class Solution:
    def isCycleBFS(self, g: List[List[int]], V: int, start: int, visited: List[bool]) -> bool:
        que = deque()
        que.append((start, -1))
        visited[start] = True
        while que:
            curr, parent = que.popleft()

            for x in g[curr]:
                if visited[x] == False:
                    que.append((x, curr))
                    visited[x] = True
                elif x != parent:
                    return True

        return False

    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:

        visited = [False] * V

        for i in range(V):
            if not visited[i] and self.isCycleBFS(adj, V, i, visited):
                return True

        return False


Approach1 = Solution


# Using Parent vector
def isCyclicUtil(g: List[List[int]], V: int, start: int, visited: List[bool]) -> bool:
    parent = [-1] * V
    que = deque()
    que.append(start)
    visited[start] = True
    while que:
        curr = que.popleft()

        for x in g[curr]:
            if visited[x] == False:
                que.append(x)
                visited[x] = True
                parent[x] = curr
            elif parent[curr] != x:
                return True

    return False


def isCyclic(g: List[List[int]], V: int) -> bool:
    visited = [False] * V

    for i in range(V):
        if visited[i] == False and isCyclicUtil(g, V, i, visited):
            return True
    return False


Approach2 = isCyclic


if __name__ == "__main__":
    cyc = [[1, 2], [0, 2], [0, 1]]
    acyc = [[1], [0, 2], [1]]
    assert Solution().isCycle(3, cyc) == True
    assert Solution().isCycle(3, acyc) == False
    assert isCyclic(cyc, 3) == True
    assert isCyclic(acyc, 3) == False
    print("ok")
