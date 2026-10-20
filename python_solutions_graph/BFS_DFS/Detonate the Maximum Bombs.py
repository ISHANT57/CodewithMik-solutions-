#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=fGSPLQ1la90
#     Company Tags                : GOOGLE
#     Leetcode Link               : https://leetcode.com/problems/detonate-the-maximum-bombs/

from typing import List
from collections import defaultdict, deque


# Approach-1 (Using DFS)
class Solution:
    # typedef long long LL; -> Python ints are arbitrary precision
    def DFS(self, u: int, visited: set, adj) -> None:

        visited.add(u)

        for v in adj[u]:
            if v not in visited:  # Not visited
                self.DFS(v, visited, adj)

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)

        adj = defaultdict(list)

        for i in range(n):
            for j in range(n):

                if i == j:  # same bomb
                    continue

                x1 = bombs[i][0]
                y1 = bombs[i][1]
                r1 = bombs[i][2]

                x2 = bombs[j][0]
                y2 = bombs[j][1]
                r2 = bombs[j][2]

                # Make a directed edge from i to j if i can detonate j as well

                distance = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)

                if r1 * r1 >= distance:
                    adj[i].append(j)

        result = 0
        visited = set()

        for i in range(n):
            self.DFS(i, visited, adj)
            count = len(visited)
            result = max(result, count)
            visited.clear()

        return result


Approach1 = Solution


# Approach-2 (Using BFS)
class Solution:
    # typedef long long LL; -> Python ints are arbitrary precision
    def BFS(self, u: int, adj) -> int:
        visited = set()
        que = deque()
        que.append(u)
        visited.add(u)

        while que:

            temp = que.popleft()

            for v in adj[temp]:

                if v not in visited:
                    que.append(v)
                    visited.add(v)

        return len(visited)

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)

        adj = defaultdict(list)

        for i in range(n):
            for j in range(n):

                if i == j:  # same bomb
                    continue

                x1 = bombs[i][0]
                y1 = bombs[i][1]
                r1 = bombs[i][2]

                x2 = bombs[j][0]
                y2 = bombs[j][1]
                r2 = bombs[j][2]

                # Make a directed edge from i to j if i can detonate j as well

                distance = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)

                if r1 * r1 >= distance:
                    adj[i].append(j)

        result = 0

        for i in range(n):
            count = self.BFS(i, adj)
            result = max(result, count)

        return result


Approach2 = Solution


if __name__ == "__main__":
    for cls in (Approach1, Approach2):
        assert cls().maximumDetonation([[2, 1, 3], [6, 1, 4]]) == 2
        assert cls().maximumDetonation([[1, 1, 5], [10, 10, 5]]) == 1
        assert cls().maximumDetonation([[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]) == 5
    print("ok")
