#       MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=kOt2VNsU0FE
#       Company Tags                : MICROSOFT
#       Leetcode Link               : https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

from typing import List
from collections import defaultdict, deque


# Approach-1 : Using DFS - (Remaining Nodes concept)
class Solution:

    def dfs(self, u: int, adj, visited: List[bool], sizeOfComponent: List[int]) -> None:
        # sizeOfComponent is a 1-element list standing in for C++ `long long &`
        visited[u] = True
        sizeOfComponent[0] += 1

        for v in adj[u]:

            if not visited[v]:
                self.dfs(v, adj, visited, sizeOfComponent)

    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for vec in edges:

            u = vec[0]
            v = vec[1]

            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        remainingNodes = n

        result = 0

        for i in range(n):
            if not visited[i]:

                sizeOfComponent = [0]

                self.dfs(i, adj, visited, sizeOfComponent)

                result += (sizeOfComponent[0]) * (remainingNodes - sizeOfComponent[0])

                remainingNodes -= sizeOfComponent[0]

        return result


Approach1 = Solution


# Approach-2 : Using DFS (Calculating duplicates and divide by 2)
class Solution:

    def dfs(self, u: int, adj, visited: List[bool], sizeOfComponent: List[int]) -> None:
        # sizeOfComponent is a 1-element list standing in for C++ `long long &`
        visited[u] = True
        sizeOfComponent[0] += 1

        for v in adj[u]:

            if not visited[v]:
                self.dfs(v, adj, visited, sizeOfComponent)

    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for vec in edges:

            u = vec[0]
            v = vec[1]

            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n

        result = 0

        for i in range(n):
            if not visited[i]:

                sizeOfComponent = [0]

                self.dfs(i, adj, visited, sizeOfComponent)

                result += (sizeOfComponent[0]) * (n - sizeOfComponent[0])

        return result // 2


Approach2 = Solution


# Approach-3 : Using BFS
class Solution:

    def bfs(self, u: int, adj, visited: List[bool], Size: List[int]) -> None:
        # Size is a 1-element list standing in for C++ `long long &`

        que = deque()
        que.append(u)

        visited[u] = True
        Size[0] += 1

        while que:

            x = que.popleft()

            for v in adj[x]:

                if not visited[v]:
                    visited[v] = True
                    que.append(v)
                    Size[0] += 1

    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        adj = defaultdict(list)

        for vec in edges:

            u = vec[0]
            v = vec[1]

            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n

        remainingNodes = n

        result = 0

        for i in range(n):

            if not visited[i]:

                Size = [0]

                self.bfs(i, adj, visited, Size)

                result += (Size[0]) * (remainingNodes - Size[0])

                remainingNodes -= Size[0]

        return result


Approach3 = Solution


# Approach - 4 : DSU (In mo DS repo - Link below)
# https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Graph/Disjoint%20Set/Count%20Unreachable%20Pairs%20of%20Nodes%20in%20an%20Undirected%20Graph.cpp


if __name__ == "__main__":
    for cls in (Approach1, Approach2, Approach3):
        assert cls().countPairs(3, [[0, 1], [0, 2], [1, 2]]) == 0
        assert cls().countPairs(7, [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]) == 14
    print("ok")
