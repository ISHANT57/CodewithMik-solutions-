# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=LVV5_MOzdq4
# Company Tags                : Will update soon
# Leetcode Link               : https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting

from collections import defaultdict, deque
from typing import List

# ************************************************************ C++ ************************************************
# Approach - Using BFS and Cycle Checks
# T.C : ~O(n)
# S.C : ~O(n)
class Solution:

    def BFS(self, start: int, adj, visited: List[bool]) -> int:
        que = deque()  # {node, path length}
        que.append((start, 0))
        maxDistance = 0

        while que:
            currNode, dist = que.popleft()

            for ngbr in adj[currNode]:
                if not visited[ngbr]:
                    visited[ngbr] = True
                    que.append((ngbr, dist+1))
                    maxDistance = max(maxDistance, dist+1)

        return maxDistance

    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        adj = defaultdict(list)  # unordered_map<int, vector<int>>

        for i in range(n):
            u = i
            v = favorite[i]
            # u --> v
            adj[v].append(u)  # reversed graph - so that we can find the path length after traversal

        longestCycleEmplCount = 0
        happyCoupleEmplCount = 0  # cycle length = 2 waalo se kitna milpaega total

        visited = [False] * n

        for i in range(n):

            if not visited[i]:
                # {node, abtak ka node count}
                mp = {}

                currNode = i
                currNodeCount = 0

                while not visited[currNode]:  # until cycle is not detected
                    visited[currNode] = True
                    mp[currNode] = currNodeCount

                    nextNode = favorite[currNode]  # favorite node of curr node
                    currNodeCount += 1

                    if nextNode in mp:  # already visited hai ye. Matlab cycle detect hogaya hai
                        cycleLength = currNodeCount - mp[nextNode]
                        longestCycleEmplCount = max(longestCycleEmplCount, cycleLength)

                        if cycleLength == 2:  # happy couple case
                            # currNode <-> nextNode = 2 nodes
                            visitedNodes = [False] * n
                            visitedNodes[currNode] = True
                            visitedNodes[nextNode] = True
                            happyCoupleEmplCount += 2 + self.BFS(currNode, adj, visitedNodes) + self.BFS(nextNode, adj, visitedNodes)
                        break
                    currNode = nextNode

        return max(happyCoupleEmplCount, longestCycleEmplCount)

Approach1 = Solution


if __name__ == "__main__":
    assert Solution().maximumInvitations([2,2,1,2]) == 3
    assert Solution().maximumInvitations([1,2,0]) == 3
    assert Solution().maximumInvitations([3,0,1,4,1]) == 4
    print("ok")
