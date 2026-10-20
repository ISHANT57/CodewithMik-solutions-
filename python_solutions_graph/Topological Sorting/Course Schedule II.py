#     MY YOUTUBE VIDEO ON THIS Qn : BFS - https://www.youtube.com/watch?v=W1WhSN9wAw0
#     				  DFS - https://www.youtube.com/watch?v=yiR95dxinjs
#     Company Tags                : Accolite, Amazon, Flipkart, Microsoft, Moonfrog Labs, OYO Rooms
#     Leetcode Link               : https://leetcode.com/problems/course-schedule-ii/

import sys
from collections import defaultdict, deque
from typing import List

sys.setrecursionlimit(10000)


# Approach-1 (Using BFS Topological Sort Concept)
class Solution:
    # Using Kahn's algorithm
    def topologicalSortCheck(self, adj, n: int, indegree: List[int]) -> List[int]:
        que = deque()
        count = 0
        result = []

        for i in range(n):
            if indegree[i] == 0:
                result.append(i)
                count += 1
                que.append(i)

        while que:
            u = que.popleft()

            for v in adj[u]:

                indegree[v] -= 1

                if indegree[v] == 0:
                    result.append(v)
                    count += 1
                    que.append(v)

        if count != n:
            return []

        return result

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        indegree = [0] * numCourses  # kahn's algo

        for vec in prerequisites:
            a = vec[0]
            b = vec[1]

            # b ---> a
            adj[b].append(a)

            # arrow ja raha hai 'a' me
            indegree[a] += 1

        # if cycle is present, not possible

        return self.topologicalSortCheck(adj, numCourses, indegree)


Approach1 = Solution


# Approach-2 (Using DFS)
class Solution:
    def __init__(self):
        self.hasCycle = False

    def DFS(self, adj, u: int, visited: List[bool], st: List[int], inRecursion: List[bool]):
        visited[u] = True
        inRecursion[u] = True

        # pehle mere ('u' ke node ke ) bachho ko daalo
        for v in adj[u]:
            if inRecursion[v] == True:
                self.hasCycle = True
                return

            if not visited[v]:
                self.DFS(adj, v, visited, st, inRecursion)

        # ab mujhe daalo stack me
        st.append(u)
        inRecursion[u] = False

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        visited = [False] * numCourses
        inRecursion = [False] * numCourses
        self.hasCycle = False

        st = []  # list used as stack

        for vec in prerequisites:
            a = vec[0]
            b = vec[1]

            # b--->a
            adj[b].append(a)

        for i in range(numCourses):
            if not visited[i]:
                self.DFS(adj, i, visited, st, inRecursion)

        result = []

        if self.hasCycle:
            return []

        while st:
            result.append(st.pop())

        return result


Approach2 = Solution

if __name__ == "__main__":
    def valid(order, n, pre):
        pos = {c: i for i, c in enumerate(order)}
        return sorted(order) == list(range(n)) and all(pos[b] < pos[a] for a, b in pre)

    pre = [[1, 0], [2, 0], [3, 1], [3, 2]]
    for A in (Approach1, Approach2):
        assert valid(A().findOrder(4, pre), 4, pre)
        assert A().findOrder(2, [[1, 0], [0, 1]]) == []
        assert A().findOrder(1, []) == [0]
    print("ok")
