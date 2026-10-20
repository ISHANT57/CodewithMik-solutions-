#     MY YOUTUBE VIDEO ON THIS Qn :   BFS - https://www.youtube.com/watch?v=lqjlGGMjSMU
#                                     DFS - https://www.youtube.com/watch?v=X1TIkW4C254
#     Company Tags                : Apple, Twitter, Meta, Accolite, Amazon, Flipkart, Microsoft, Moonfrog Labs, OYO Rooms
#     Leetcode Link               : https://leetcode.com/problems/course-schedule/
#     GfG Link                    : https://practice.geeksforgeeks.org/problems/prerequisite-tasks/1?

import sys
from collections import defaultdict, deque
from typing import List

sys.setrecursionlimit(10000)


# Approach-1 (Using BFS Cycle Check - Kahn's Algorithm (Topological Sort)
class Solution:

    def topologicalSortCheck(self, adj, n: int, indegree: List[int]) -> bool:
        que = deque()

        count = 0

        for i in range(n):
            if indegree[i] == 0:
                count += 1
                que.append(i)

        while que:
            u = que.popleft()

            for v in adj[u]:

                indegree[v] -= 1

                if indegree[v] == 0:
                    count += 1
                    que.append(v)

        if count == n:  # I was able to visit all nodes (course)
            return True  # i.e. I was able to finish all courses

        return False  # means there was a cycle and I couldn't complete all courses

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

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


# Approach-2 (Using DFS Cycle Check)
class Solution:
    def isCycleDFS(self, adj, u: int, visited: List[bool], inRecursion: List[bool]) -> bool:
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

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = defaultdict(list)
        visited = [False] * numCourses
        inRecursion = [False] * numCourses

        for vec in prerequisites:
            a = vec[0]
            b = vec[1]

            # b ---> a
            adj[b].append(a)

        for i in range(numCourses):
            if not visited[i] and self.isCycleDFS(adj, i, visited, inRecursion):
                return False

        return True


Approach2 = Solution

if __name__ == "__main__":
    for A in (Approach1, Approach2):
        assert A().canFinish(2, [[1, 0]]) is True
        assert A().canFinish(2, [[1, 0], [0, 1]]) is False
    print("ok")
