#          Scroll below to see JAVA code as well (Java section skipped in this Python port)
#
#     MY YOUTUBE VIDEO ON THIS Qn : DFS - https://www.youtube.com/watch?v=DsAIuJmiT1c
#                                   BFS - Let me know if you want a video on this)
#                                   DSU - Let me know if you want a video on this)
#     Company Tags                : Amazon
#     Leetcode Link               : https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

from typing import List
from collections import defaultdict


# ******************************************************************* C++ (ported to Python) ************************************************************************
# Approach-1 (DFS)
# T.C : O(m* ( V+E)), we try DFS m times
# S.C : O(V+E)
class Solution:

    def DFS(self, adj, curr: str, visited: List[int]) -> str:
        visited[ord(curr) - ord('a')] = 1

        minChar = curr

        for v in adj[curr]:

            if visited[ord(v) - ord('a')] == 0:
                minChar = min(minChar, self.DFS(adj, v, visited))

        return minChar

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)
        adj = defaultdict(list)  # unordered_map<char, vector<char>>

        for i in range(n):
            u = s1[i]
            v = s2[i]

            adj[u].append(v)
            adj[v].append(u)

        m = len(baseStr)
        result = []  # list of chars, joined at the end (C++ string push_back)

        for i in range(m):
            ch = baseStr[i]

            visited = [0] * 26

            result.append(self.DFS(adj, ch, visited))

        return "".join(result)


Approach1 = Solution


# Approach-2 (BFS - Let me know if you want a video on this)
# (not implemented in the original source)


# Approach-3 (DSU - Let me know if you want a video on this)
# (not implemented in the original source)


if __name__ == "__main__":
    assert Solution().smallestEquivalentString("parker", "morris", "parser") == "makkek"
    assert Solution().smallestEquivalentString("hello", "world", "hold") == "hdld"
    assert Solution().smallestEquivalentString("leetcode", "programs", "sourcecode") == "aauaaaaada"
    print("ok")
