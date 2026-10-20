# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=xQ3vjWwFRuI
# Company Tags                : Flipkart, Microsoft
# GfG Link                    : https://practice.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1

from typing import List
import heapq

INT_MAX = 2**31 - 1


# Time : O(E * log(V))
# E = number of edges
# V = number of vertices
class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex S.
    # adj is the C++ "vector<vector<int>> adj[]": adj[node] is a list of [adjNode, dist]
    def dijkstra(self, V: int, adj: List[List[List[int]]], S: int) -> List[int]:

        pq = []  # min heap of (distance, node)

        result = [INT_MAX] * V

        result[S] = 0
        heapq.heappush(pq, (0, S))
        # NOTE - You can add a visited vector to avoid revisiting a node again and again. It will reduce the time complexity.

        while pq:

            d, node = heapq.heappop(pq)

            for vec in adj[node]:

                adjNode = vec[0]
                dist = vec[1]

                if d + dist < result[adjNode]:

                    result[adjNode] = d + dist
                    heapq.heappush(pq, (d + dist, adjNode))

        return result


Approach1 = Solution


if __name__ == "__main__":
    # V=3, edges 0-1 (1), 1-2 (3), 0-2 (6) undirected
    adj = [[[1, 1], [2, 6]], [[0, 1], [2, 3]], [[1, 3], [0, 6]]]
    assert Solution().dijkstra(3, adj, 2) == [4, 3, 0]
    assert Solution().dijkstra(3, adj, 0) == [0, 1, 4]
    print("ok")
