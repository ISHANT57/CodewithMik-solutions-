#     Company Tags  : Not known yet(Leetcode Premium) (But it's a modified version of cycle detection which is asked in many companies)
#     Leetcode Link : https://leetcode.com/problems/all-paths-from-source-lead-to-destination/
#
#     Since it's a Premium question, hence providing the description below
#     Description:
#     Given the edges of a directed graph, and two nodes source and destination of this graph,
#     determine whether or not all paths starting from source eventually end at destination, that is:
#
#     -At least one path exists from the source node to the destination node
#     -If a path exists from the source node to a node with no outgoing edges, then that node is equal to destination.
#     -The number of possible paths from source to destination is a finite number.
#
#     Return true if and only if all roads from source lead to destination.
#     Examples:
#
#     Example 1 :
#     Input: n = 3, edges = [[0,1],[0,2]], source = 0, destination = 2
#     Output: false
#     Explanation: It is possible to reach and get stuck on both node 1 and node 2.
#
#     Example 2 :
#     Input: n = 4, edges = [[0,1],[0,3],[1,2],[2,1]], source = 0, destination = 3
#     Output: false
#     Explanation: We have two possibilities: to end at node 3, or to loop over node 1 and node 2 indefinitely.
#
#     Example 3 :
#     Input: n = 4, edges = [[0,1],[0,2],[1,3],[2,3]], source = 0, destination = 3
#     Output: true
#
#     Example 4 :
#     Input: n = 3, edges = [[0,1],[1,1],[1,2]], source = 0, destination = 2
#     Output: false
#     Explanation: All paths from the source node end at the destination node, but there are an infinite number of paths,
#     uch as 0-1-2, 0-1-1-2, 0-1-1-1-2, 0-1-1-1-1-2, and so on.
#
#     Example 5 :
#     Input: n = 2, edges = [[0,1],[1,1]], source = 0, destination = 1
#     Output: false
#     Explanation: There is infinite self-loop at destination node.
#
#     Note:
#
#     The given graph may have self loops and parallel edges.
#     The number of nodes n in the graph is between 1 and 10000
#     The number of edges in the graph is between 0 and 10000
#     0 <= edges.length <= 10000
#     edges[i].length == 2
#     0 <= source <= n - 1
#     0 <= destination <= n - 1

from typing import List
from collections import defaultdict


# NOTE : I could have shown multiple approaches below (Using BFS, Kosaraju's algo, Graph color cycle detection etc. but they are already present in my Graph section)
# So, I am providing only DFS approach
class Solution:
    def dfs(self, mp, source: int, destination: int, inStack: List[bool], visited: List[bool]) -> bool:
        if len(mp[source]) == 0:
            return source == destination
        inStack[source] = True
        visited[source] = True

        for x in mp[source]:
            if inStack[x]:
                return False
            elif not visited[x] and not self.dfs(mp, x, destination, inStack, visited):
                return False

        inStack[source] = False
        return True

    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)  # map<int, vector<int>> (ordering not needed, dict is enough)
        edgeCount = len(edges)
        for i in range(edgeCount):
            u = edges[i][0]
            v = edges[i][1]

            adj[u].append(v)

        if len(adj[destination]) != 0:
            return False

        inStack = [False] * n
        visited = [False] * n
        return self.dfs(adj, source, destination, inStack, visited)


Approach1 = Solution


if __name__ == "__main__":
    s = Solution()
    assert s.leadsToDestination(3, [[0, 1], [0, 2]], 0, 2) is False
    assert s.leadsToDestination(4, [[0, 1], [0, 3], [1, 2], [2, 1]], 0, 3) is False
    assert s.leadsToDestination(4, [[0, 1], [0, 2], [1, 3], [2, 3]], 0, 3) is True
    assert s.leadsToDestination(3, [[0, 1], [1, 1], [1, 2]], 0, 2) is False
    assert s.leadsToDestination(2, [[0, 1], [1, 1]], 0, 1) is False
    print("ok")
