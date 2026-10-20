#   MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=9qWMS8GLvdI
#   Company Tags                : Amazon, Microsoft
#   Leetcode Qn Link            : https://leetcode.com/problems/all-paths-from-source-to-target/

from typing import List
from collections import deque


# Approach - 1 (More like a Graph DFS)
class Solution:
    def DFS(self, adj: List[List[int]], start: int, temp: List[int], result: List[List[int]]) -> None:

        temp.append(start)
        if start == len(adj) - 1:
            result.append(temp[:])
        else:
            for x in adj[start]:
                self.DFS(adj, x, temp, result)
        temp.pop()

    def allPathsSourceTarget(self, adj: List[List[int]]) -> List[List[int]]:
        result = []
        for x in adj[0]:
            temp = []
            temp.append(0)
            self.DFS(adj, x, temp, result)
        return result


Approach1 = Solution


# Approach-2 (Similar to approach-1 but a little simple)
class Solution:
    def __init__(self):
        self.target = 0

    def dfs(self, adj: List[List[int]], start: int, temp: List[int], result: List[List[int]]) -> None:
        if start == self.target:
            result.append(temp[:])
            return

        for x in adj[start]:
            temp.append(x)
            self.dfs(adj, x, temp, result)
            temp.pop()

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        temp = []
        self.target = len(graph) - 1
        temp.append(0)
        self.dfs(graph, 0, temp, result)

        return result


Approach2 = Solution


# Approach-3 (Using BFS)
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)

        source = 0
        target = n - 1

        result = []
        temp = []

        que = deque()
        temp.append(0)
        que.append(temp)

        while que:
            currPath = que.popleft()

            lastNode = currPath[-1]

            if lastNode == target:
                result.append(currPath)
            else:
                for v in graph[lastNode]:
                    path = currPath[:]
                    path.append(v)
                    que.append(path)

        return result


Approach3 = Solution


if __name__ == "__main__":
    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    expected = sorted([[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]])
    for cls in (Approach1, Approach2, Approach3):
        assert sorted(cls().allPathsSourceTarget(graph)) == expected, cls
    print("ok")
