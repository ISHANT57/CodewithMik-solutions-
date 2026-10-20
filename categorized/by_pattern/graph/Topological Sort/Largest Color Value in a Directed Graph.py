#            Scroll below to see JAVA code as well (Java section skipped in this Python port)
#
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=V6LnZaX7zpk
#     Company Tags                : META
#     Leetcode Link               : https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

from collections import defaultdict, deque
from typing import List


# ***************************************** C++ (ported to Python) *****************************************
# Approach (Using Topological Sorting with BFS)
# T.C : O(V+E)
# S.C : O(V+E)
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        N = len(colors)

        indegree = [0] * N

        for vec in edges:
            u = vec[0]
            v = vec[1]

            adj[u].append(v)
            indegree[v] += 1

        que = deque()
        t = [[0] * 26 for _ in range(N)]

        for i in range(N):
            if indegree[i] == 0:
                que.append(i)
                t[i][ord(colors[i]) - ord('a')] = 1

        answer = 0

        countNodes = 0

        while que:

            u = que.popleft()

            countNodes += 1

            answer = max(answer, t[u][ord(colors[u]) - ord('a')])

            for v in adj[u]:

                for i in range(26):

                    t[v][i] = max(t[v][i], t[u][i] + (1 if ord(colors[v]) - ord('a') == i else 0))

                indegree[v] -= 1
                if indegree[v] == 0:
                    que.append(v)

        if countNodes < N:
            return -1

        return answer


Approach1 = Solution

# Approach-2 (Using DFS - Soon)  (not implemented in the source)

if __name__ == "__main__":
    assert Solution().largestPathValue("abaca", [[0, 1], [0, 2], [2, 3], [3, 4]]) == 3
    assert Solution().largestPathValue("a", [[0, 0]]) == -1
    print("ok")
