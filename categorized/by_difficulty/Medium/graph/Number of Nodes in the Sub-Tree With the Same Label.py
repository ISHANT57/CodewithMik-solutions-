# MY YOUTUBE VIDEO ON THIS Qn : Approach-1 : https://www.youtube.com/watch?v=4seuiuW8c0o
#                               Approach-2 : https://www.youtube.com/watch?v=yZ6IM8Q-0Ac
# Company Tags                : <soon>
# Leetcode Link               : https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/

from typing import List
from collections import defaultdict


# Approach-1 (DFS - adding counts from children at every node)
class Solution:
    def DFS(self, adj, u: int, parent: int, result: List[int], labels: str) -> List[int]:
        my_count = [0] * 26
        mylabel = labels[u]

        my_count[ord(mylabel) - ord('a')] = 1

        for v in adj[u]:
            if v == parent:
                continue

            child_count = [0] * 26
            child_count = self.DFS(adj, v, u, result, labels)

            for i in range(26):
                my_count[i] += child_count[i]

        result[u] = my_count[ord(mylabel) - ord('a')]

        return my_count

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj = defaultdict(list)

        for vec in edges:
            u = vec[0]
            v = vec[1]

            adj[u].append(v)
            adj[v].append(u)

        result = [0] * n

        self.DFS(adj, 0, -1, result, labels)

        return result


Approach1 = Solution


# Approach-2 (DFS - No need to add count at everynode)
class Solution:
    def DFS(self, adj, u: int, parent: int, result: List[int], labels: str, count: List[int]) -> None:
        mylabel = labels[u]

        count_before_exploring_my_subtree = count[ord(mylabel) - ord('a')]

        # explore my subtree children
        count[ord(mylabel) - ord('a')] += 1
        for v in adj[u]:
            if v == parent:
                continue

            self.DFS(adj, v, u, result, labels, count)

        count_after_exploring_my_subtree = count[ord(mylabel) - ord('a')]
        result[u] = count_after_exploring_my_subtree - count_before_exploring_my_subtree

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj = defaultdict(list)

        for vec in edges:
            u = vec[0]
            v = vec[1]

            adj[u].append(v)
            adj[v].append(u)

        result = [0] * n
        count = [0] * 26

        self.DFS(adj, 0, -1, result, labels, count)

        return result


Approach2 = Solution

if __name__ == "__main__":
    for S in (Approach1, Approach2):
        assert S().countSubTrees(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], "abaedcd") == [2,1,1,1,1,1,1]
        assert S().countSubTrees(4, [[0,1],[1,2],[0,3]], "bbbb") == [4,2,1,1]
        assert S().countSubTrees(5, [[0,1],[0,2],[1,3],[0,4]], "aabab") == [3,2,1,1,1]
    print("ok")
