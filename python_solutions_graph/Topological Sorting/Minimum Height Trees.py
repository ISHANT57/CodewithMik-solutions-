# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=ZXANlaEuYvQ
# Company Tags                : GOOGLE
# Leetcode Link               : https://leetcode.com/problems/minimum-height-trees/
#
# NOTE : You can do a brute force to do DFS from each node treating them as root and keep finding the Height in every case. That will give TLE.

# **************************************************** C++ -> Python ********************************************
# Using Topological Sorting
# T.C : O(V+E)
# S.C : O(V+E)
from typing import List
from collections import deque, defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        result = []
        indegree = [0] * n
        adj = defaultdict(list)  # map<int, vector<int>>

        for vec in edges:
            u = vec[0]
            v = vec[1]
            indegree[u] += 1
            indegree[v] += 1
            adj[u].append(v)
            adj[v].append(u)

        que = deque()
        for i in range(n):
            if indegree[i] == 1:  # adding all leafs node so that we can remove them later
                que.append(i)

        while n > 2:
            size = len(que)
            n -= size  # removing nodes with indegreee 1

            while size > 0:
                size -= 1
                u = que.popleft()
                for v in adj[u]:
                    indegree[v] -= 1
                    if indegree[v] == 1:
                        que.append(v)

        while que:
            result.append(que.popleft())
        return result


Approach1 = Solution

if __name__ == "__main__":
    assert sorted(Solution().findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])) == [1]
    assert sorted(Solution().findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]])) == [3, 4]
    assert Solution().findMinHeightTrees(1, []) == [0]
    print("ok")
