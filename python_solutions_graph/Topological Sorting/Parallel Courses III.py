# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=743cYtf3DJI
# Company Tags                : Uber
# Leetcode Link               : https://leetcode.com/problems/parallel-courses-iii/

# ****************************************************** C++ -> Python ******************************************************
# Approach-1 (Using Simple Topological sorting)
# T.C : O(V+E)
from typing import List
from collections import deque, defaultdict


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = defaultdict(list)  # unordered_map<int, vector<int>>
        indegree = [0] * n

        for vec in relations:
            u = vec[0] - 1
            v = vec[1] - 1

            adj[u].append(v)
            indegree[v] += 1

        que = deque()
        maxTime = [0] * n  # maxTime[i] = maximum time taken by ith course to complete

        for i in range(n):
            if indegree[i] == 0:
                que.append(i)
                maxTime[i] = time[i]

        while que:

            u = que.popleft()

            for v in adj[u]:
                # Finishing time of v will depend on the maximum time of its pre-requisites
                maxTime[v] = max(maxTime[v], maxTime[u] + time[v])
                indegree[v] -= 1
                if indegree[v] == 0:
                    que.append(v)

        return max(maxTime)


Approach1 = Solution

# Approach-2 (Using DFS Topological Sort) - Soon I will update here

if __name__ == "__main__":
    assert Solution().minimumTime(3, [[1, 3], [2, 3]], [3, 2, 5]) == 8
    assert Solution().minimumTime(5, [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], [1, 2, 3, 4, 5]) == 12
    print("ok")
