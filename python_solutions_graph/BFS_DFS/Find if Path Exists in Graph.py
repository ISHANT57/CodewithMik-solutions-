#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=mbR1XSXidEE
#     Company Tags                : Microsoft, Adobe, Amazon, Morgan Stanley, Samsung
#     Leetcode Link               : https://leetcode.com/problems/find-if-path-exists-in-graph/

from typing import List
from collections import defaultdict, deque

# NOTE : Soon, I will upload the Union Find approach for this Qn as well


# Using DFS : O(m+n)
class Solution:

    def check(self, mp, node: int, dest: int, visited: List[bool]) -> bool:
        if node == dest:
            return True

        if visited[node]:
            return False

        visited[node] = True
        for it in mp[node]:
            if self.check(mp, it, dest, visited):
                return True
        return False

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        if source == destination:
            return True

        mp = defaultdict(list)

        for vec in edges:
            u = vec[0]
            v = vec[1]

            mp[u].append(v)
            mp[v].append(u)

        visited = [False] * n
        return self.check(mp, source, destination, visited)


Approach1 = Solution


# Using BFS : O(m+n)
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        mp = defaultdict(list)

        for vec in edges:
            u = vec[0]
            v = vec[1]

            mp[u].append(v)
            mp[v].append(u)

        visited = [False] * n

        que = deque()
        que.append(source)
        visited[source] = True

        while que:
            node = que.popleft()
            if node == destination:
                return True

            for it in mp[node]:
                if not visited[it]:
                    visited[it] = True
                    que.append(it)

        return False


Approach2 = Solution


if __name__ == "__main__":
    for cls in (Approach1, Approach2):
        assert cls().validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2) is True
        assert cls().validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5) is False
    print("ok")
