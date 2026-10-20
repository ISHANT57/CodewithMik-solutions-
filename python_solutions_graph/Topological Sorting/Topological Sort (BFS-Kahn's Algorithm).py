# MY YOUTUBE VIDE ON THIS Qn		: https://www.youtube.com/watch?v=uVl4ftleTes
# Company Tags                        : Accolite, Amazon, Flipkart, Microsoft, Moonfrog Labs, OYO Rooms
# GfG Link                            : https://practice.geeksforgeeks.org/problems/topological-sort/1#
# Related Leetcode Qn                 : Course Schedule, Course Schedule II
# Course Schedule (Leetcode - 207)    : https://leetcode.com/problems/course-schedule/
# Course Schedule II (Leetcode - 210) : https://leetcode.com/problems/course-schedule-ii/
# Solution (Course Schedule)          : https://github.com/MAZHARMIK/Leetcode-May-Challenge-2020/blob/master/Course%20Schedule%20(C%2B%2B)
# Solution (Course Schedule II)       : https://github.com/MAZHARMIK/Leetcode-July-Challenge-2020/blob/master/Course%20Schedule%20II%20(C%2B%2B)
# NOTE: This can also be used to check if the graph contains cycle or not (Please see Line:56 below)


# NOTE : This assumes that, we don't have cycle in the given directed graph. You can simply add few things in the same code to check for cycle also
# Or, see this : https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Graph/Topological%20Sorting/Course%20Schedule.cpp
from typing import List
from collections import deque


class Solution:
    # Function to return list containing vertices in Topological order.
    def topoSort(self, N: int, adj: List[List[int]]) -> List[int]:
        que = deque()
        indegree = [0] * N

        # 1
        for u in range(N):
            for v in adj[u]:
                indegree[v] += 1

        # 2. Fill que, indegree with 0
        for i in range(N):
            if indegree[i] == 0:
                que.append(i)

        # 3. Simple BFS
        result = []
        while que:
            u = que.popleft()
            result.append(u)

            for v in adj[u]:
                indegree[v] -= 1

                if indegree[v] == 0:
                    que.append(v)

        return result


Approach1 = Solution

if __name__ == "__main__":
    adj = [[], [], [3], [1], [0, 1], [0, 2]]
    res = Solution().topoSort(6, adj)
    pos = {x: i for i, x in enumerate(res)}
    assert len(res) == 6 and all(pos[u] < pos[v] for u in range(6) for v in adj[u])
    print("ok", res)
