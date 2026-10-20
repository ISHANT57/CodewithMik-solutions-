# Company Tags  : Uber (Phone screening)
# Leetcode Link : https://leetcode.com/problems/parallel-courses/
# Since, It's a Premium Question, so I am providing here the question and examples as well:
#
# Given K courses required to graduate and array of those courses. Some needs to be taken before others.
# [i,j] - course i must be taken in a semester that is prior to course j.
# You can take as many courses as you want every semester.
#
# Find a minimum number of semesters you need to finish all K courses. If not possible - throw some exception or whatever.
#
# Example 1:
#
# 3, [[1,0], [1,2]].
#
# 3 courses to graduate.
# Course 1 must be take before course 0.
# Course 1 must be taken before course 2.
#
# First semester you take course 1. Second semester you take course 0 and 2.
#
# Output: 2.
#
# Example 2:
#
# 2, [[0,1], [1,0]
#
# 2 courses to graduate.
# Course 0 must be taken before course 1.
# Course 1 must be take before course 0.
#
# Output:
# Exception aka "not possible."
#
# NOTE (translation): the original C++ loops courses 1..N (LeetCode 1136 style, 1-indexed);
# the example above with course 0 is kept as written by the author, code is unchanged.

# It's a variation of Kahn's algorithm
from typing import List, Dict
from collections import deque, defaultdict


class Solution:
    def topologicalSortBFS(self, adj: Dict[int, List[int]], N: int, indegree: List[int]) -> int:
        que = deque()
        for i in range(1, N + 1):
            if indegree[i] == 0:
                que.append(i)

        count = 0
        result = 0
        while que:
            result += 1
            n = len(que)
            while n > 0:
                n -= 1
                curr = que.popleft()
                count += 1
                for x in adj[curr]:
                    indegree[x] -= 1
                    if indegree[x] == 0:
                        que.append(x)
        return result if count == N else -1

    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        adj = defaultdict(list)  # unordered_map<int, vector<int>>
        indegree = [0] * (N + 1)
        for relation in relations:
            x = relation[0]
            y = relation[1]
            adj[x].append(y)
            indegree[y] += 1

        return self.topologicalSortBFS(adj, N, indegree)


Approach1 = Solution

if __name__ == "__main__":
    assert Solution().minimumSemesters(3, [[1, 3], [2, 3]]) == 2
    assert Solution().minimumSemesters(3, [[1, 2], [2, 3], [3, 1]]) == -1
    print("ok")
