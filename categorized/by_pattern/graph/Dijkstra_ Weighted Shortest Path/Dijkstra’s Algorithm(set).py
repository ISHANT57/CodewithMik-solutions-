# MY YOUTUBE VIDEO ON THIS Qn   : https://www.youtube.com/watch?v=3qIoYIMidpc
# Company Tags                  : Flipkart, Microsoft
# GfG Link                      : https://practice.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1

from typing import List
import bisect

INT_MAX = 2**31 - 1


# Time : O(E * log(V))
# E = number of edges
# V = number of vertices
class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex S.
    # adj is the C++ "vector<vector<int>> adj[]": adj[node] is a list of [adjNode, dist]
    def dijkstra(self, V: int, adj: List[List[List[int]]], S: int) -> List[int]:
        # C++ std::set<pair<int,int>> is emulated by a sorted list of (dist, node) tuples
        # (bisect.insort to insert, bisect_left + pop to erase, index 0 == *pq.begin()).
        pq = []

        result = [INT_MAX] * V

        result[S] = 0
        bisect.insort(pq, (0, S))

        while pq:

            it = pq[0]
            d = it[0]
            node = it[1]
            pq.pop(0)  # pq.erase(it)

            for vec in adj[node]:

                adjNode = vec[0]
                dist = vec[1]

                if d + dist < result[adjNode]:

                    if result[adjNode] != INT_MAX:
                        iter_ = bisect.bisect_left(pq, (result[adjNode], adjNode))
                        pq.pop(iter_)
                        # OR, pq.erase({result[adjNode], adjNode});

                    result[adjNode] = d + dist
                    bisect.insort(pq, (d + dist, adjNode))

        return result


Approach1 = Solution


if __name__ == "__main__":
    adj = [[[1, 1], [2, 6]], [[0, 1], [2, 3]], [[1, 3], [0, 6]]]
    assert Solution().dijkstra(3, adj, 2) == [4, 3, 0]
    assert Solution().dijkstra(3, adj, 0) == [0, 1, 4]
    print("ok")
