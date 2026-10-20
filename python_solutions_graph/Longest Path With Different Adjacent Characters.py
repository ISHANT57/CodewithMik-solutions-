# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=EA8dP63iVPk
# Company Tags                : Microsoft
# Leetcode Link               : https://leetcode.com/problems/longest-path-with-different-adjacent-characters/
# Similar Qn in Tree          : Binary Tree Maximum Path Sum - YouTube  : https://www.youtube.com/watch?v=Op6YFcs8R9M
#                                                              Leetcode : https://leetcode.com/problems/binary-tree-maximum-path-sum/

import sys
from collections import defaultdict
from typing import List

sys.setrecursionlimit(10**6)

# DFS - (Similar to Binary Tree Maximum Path Sum)
class Solution:

    def DFS(self, adj, curr: int, parent: int, s: str) -> int:

        longest = 0
        second_longest = 0

        for child in adj[curr]:
            if child == parent:
                continue

            child_longest_length = self.DFS(adj, child, curr, s)

            if s[child] == s[curr]:
                continue

            if child_longest_length > second_longest:
                second_longest = child_longest_length

            if second_longest > longest:
                longest, second_longest = second_longest, longest

        koi_ek_acha = max(longest, second_longest) + 1  # Why this 1 ? Because including the curr node itself

        only_root_acha = 1  # only curr node is valid, rest children have duplicate character

        neeche_hi_milgaya_answer = longest + second_longest + 1

        self.result = max(self.result, neeche_hi_milgaya_answer, koi_ek_acha, only_root_acha)

        return max(koi_ek_acha, only_root_acha)

    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        self.result = 0
        adj = defaultdict(list)  # unordered_map<int, vector<int>>

        for i in range(1, n):
            u = i
            v = parent[i]

            adj[u].append(v)
            adj[v].append(u)

        self.DFS(adj, 0, -1, s)

        return self.result

Approach1 = Solution


if __name__ == "__main__":
    assert Solution().longestPath([-1,0,0,1,1,2], "abacbe") == 3
    assert Solution().longestPath([-1,0,0,0], "aabc") == 3
    print("ok")
