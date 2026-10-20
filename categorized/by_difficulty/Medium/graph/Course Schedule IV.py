#     Scroll below to see JAVA code also (Java sections skipped in this Python port)
#
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=ScJNPlYz1J4
#     Company Tags                : Amazon
#     Leetcode Link               : https://leetcode.com/problems/course-schedule-iv/description/

import sys
from collections import defaultdict, deque
from typing import List

sys.setrecursionlimit(10000)


# ************************************ C++ (ported to Python) ************************************
# Approach-1 (Using DFS) You can use BFS as well
# T.C : O(Q * (V+E))
# S.C : O(V+E)
class Solution:

    def dfs(self, adj, src: int, dest: int, visited: List[bool]) -> bool:
        visited[src] = True

        if src == dest:
            return True  # yes we can reach to dest

        isReacheable = False
        for adjNode in adj[src]:
            if not visited[adjNode]:
                isReacheable = isReacheable or self.dfs(adj, adjNode, dest, visited)

        return isReacheable

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)

        for edge in prerequisites:
            u = edge[0]
            v = edge[1]

            adj[u].append(v)  # u --> v

        Q = len(queries)
        result = [False] * Q

        for i in range(Q):
            u = queries[i][0]  # source.
            v = queries[i][1]  # Dest.

            visited = [False] * numCourses
            result[i] = self.dfs(adj, u, v, visited)  # You can use BFS as well

        return result


Approach1 = Solution


# Approach-2 (Using preprocessing and DFS) - You can use BFS as well
# T.C : O(V^2 * (V+E))
# S.C : O(V+E)
class Solution:
    # Perform DFS and mark prerequisites for each node
    def dfs(self, adj, visited: List[bool], src: int, target: int) -> bool:
        visited[src] = True

        if src == target:
            return True

        isPrerequisite = False
        for adjNode in adj[src]:
            if not visited[adjNode]:
                isPrerequisite = isPrerequisite or self.dfs(adj, visited, adjNode, target)
        return isPrerequisite

    def preprocess(self, numCourses: int, adjList, isPrerequisite: List[List[bool]]):
        for u in range(numCourses):
            for v in range(numCourses):
                if u != v:
                    visited = [False] * numCourses
                    if self.dfs(adjList, visited, u, v):
                        isPrerequisite[u][v] = True

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = defaultdict(list)
        for edge in prerequisites:
            adjList[edge[0]].append(edge[1])

        isPrerequisite = [[False] * numCourses for _ in range(numCourses)]
        self.preprocess(numCourses, adjList, isPrerequisite)

        Q = len(queries)
        result = [False] * Q

        for i in range(Q):
            u = queries[i][0]  # source.
            v = queries[i][1]  # Dest.

            result[i] = isPrerequisite[u][v]

        return result


Approach2 = Solution


# Approach-3 (Kahn's Algorithm)
# T.C : O(V^2 + V + E) -> Processing Nodes (each node pushed once in queue) = O(V), Processing edges = O(E), Inserting prerequisites (each node can have ~V prerequisites in worst case): O(V^2)
# S.C : O(V+E)
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        for edge in prerequisites:
            u = edge[0]
            v = edge[1]
            adj[u].append(v)
            indegree[v] += 1

        que = deque()
        for i in range(numCourses):
            if not indegree[i]:
                que.append(i)

        # Map from the node as key to the set of prerequisite nodes.
        mp = defaultdict(set)
        while que:
            node = que.popleft()

            for ngbr in adj[node]:
                # Add node and prerequisite of node to the prerequisites of adj
                mp[ngbr].add(node)
                for prereq in list(mp[node]):  # worst case , it has V prerequisites - O(V) time
                    mp[ngbr].add(prereq)

                indegree[ngbr] -= 1
                if not indegree[ngbr]:
                    que.append(ngbr)

        Q = len(queries)
        result = [False] * Q
        for i in range(Q):
            src = queries[i][0]
            dest = queries[i][1]

            isReachable = src in mp[dest]
            result[i] = isReachable

        return result


Approach3 = Solution

if __name__ == "__main__":
    for A in (Approach1, Approach2, Approach3):
        assert A().checkIfPrerequisite(2, [[1, 0]], [[0, 1], [1, 0]]) == [False, True]
        assert A().checkIfPrerequisite(2, [], [[1, 0], [0, 1]]) == [False, False]
        assert A().checkIfPrerequisite(3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]]) == [True, True]
    print("ok")
