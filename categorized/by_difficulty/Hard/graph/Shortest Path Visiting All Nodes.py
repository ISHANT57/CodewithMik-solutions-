# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=m73DRkEo8Ko
# Company Tags                : GOOGLE
# Leetcode Link               : https://leetcode.com/problems/shortest-path-visiting-all-nodes/
#
# -------->  Find Q&A in the bottom of this page
#
# Time Complexity : O(2^N * N^2).
# Notice the while loop that performs the BFS traversal of the graph.
# In the worst case, the while loop can run 2^N iterations, where N is the number of nodes in the graph.
# This is because the program explores all possible combinations of nodes using bit masking i.e. each bit can be either 0 or 1 (2 possibilities) ---> 2^N
# Within each iteration, there is a nested loop that iterates through the neighbors of the current node.
# In the worst case, this inner loop iterates N times for each node.
# So, the overall time complexity is 0(2^N * N^2).

from typing import List
from collections import deque


class Solution:
    # typedef pair<int, int> P -> tuple (node, mask)

    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)

        if n == 1 or n == 0:
            return 0

        que = deque()

        vis = set()  # C++ std::set of pairs -> Python set of tuples (hash lookup)
        # Instead of set, you can also use : visited = [[False] * finalState for _ in range(n)]
        # Just like done in Java code below

        allVisitedState = (1 << n) - 1  # if all nodes visited then

        for i in range(n):
            maskValue = (1 << i)

            que.append((i, maskValue))

            vis.add((i, maskValue))

        result = 0

        # Implementing BFS
        while que:
            N = len(que)
            result += 1
            while N > 0:
                N -= 1

                curr = que.popleft()

                currNode = curr[0]
                currMask = curr[1]

                for adj in graph[currNode]:
                    nextMask = currMask | (1 << adj)

                    if nextMask == allVisitedState:
                        return result

                    if (adj, nextMask) not in vis:
                        vis.add((adj, nextMask))
                        que.append((adj, nextMask))

        return -1


Approach1 = Solution

# (Java section of the original file skipped: duplicate of the C++ approach)

# ******** Q&A *********
# Qn : what is the need of bit masking? i mean cant we simply use a 2d array which tracks the state of (parent, child)
# i.e if i am coming from 0th node and going to 1st node then, i will simply set it as isvisited[0][1] = true.
# next time, when i come in this same situation i.e 0 to 1, i can simply check if isvisited[0][1] = true or not.
#
# Ans : That's such an IMPORTANT qn you asked.  Actually i took a very small example in my YouTube video.
# In big examples- the repeated path can be large as well .
# For example :  you came to 3 via 0,1,2
# Path - 0 -> 1  -> 2 -> 3
#
# Suppose you came to 3 via 0,4,2,3
# Here if you notice, you came to 3 from 2 but the entire path is different.
# Hence keeping track of only precise node will not be enough, we need entire trail path to see if we have seen the path before or not.

if __name__ == "__main__":
    assert Solution().shortestPathLength([[1, 2, 3], [0], [0], [0]]) == 4
    assert Solution().shortestPathLength([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]) == 4
    assert Solution().shortestPathLength([[]]) == 0
    print("ok")
