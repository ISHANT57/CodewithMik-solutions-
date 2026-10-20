# MY YOUTUBE VIDEO ON THEORY OF MINIMUM SPANNING TREE            - https://youtu.be/xxvY2UX7YPg
# MY YOUTUBE VIDEO ON Prim's Algorithm for MINIMUM SPANNING TREE - https://www.youtube.com/watch?v=V9gXzD7g8fw
# Company Tags                                                   - Amazon, Cisco, Samsung
# Qn Link                                                        - https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1

import heapq
from typing import List


# Approach-1 : Using Priority_queue
class Solution:
    # typedef pair<int, int> P  -> tuple (weight, node)
    # Function to find sum of weights of edges of the Minimum Spanning Tree.
    # adj: list of V lists, each entry is [neighbor, weight]
    def spanningTree(self, V: int, adj: List[List[List[int]]]) -> int:
        pq = []  # min-heap via heapq (greater<P> in C++)
        heapq.heappush(pq, (0, 0))
        inMST = [False] * V
        sum = 0

        while pq:
            p = heapq.heappop(pq)

            wt = p[0]
            node = p[1]

            if inMST[node] == True:
                continue

            inMST[node] = True  # added to mst
            sum += wt

            for tmp in adj[node]:
                neighbor = tmp[0]
                neighbor_wt = tmp[1]

                if inMST[neighbor] == False:
                    heapq.heappush(pq, (neighbor_wt, neighbor))

        return sum


Approach1 = Solution


# Approach-2 :Without using Priority_queue
class Solution:
    def minKey(self, V: int, inMST: List[bool], key: List[int]) -> int:
        minValue = float('inf')
        min_index = None
        for v in range(V):
            if inMST[v] == False and key[v] < minValue:
                min_index = v
                minValue = key[v]
        return min_index

    # graph: V x V adjacency matrix, 0 means no edge
    def spanningTree(self, V: int, E: int, graph: List[List[int]]) -> int:
        key = [float('inf')] * V
        parent = [0] * V
        inMST = [False] * V

        parent[0] = -1
        key[0] = 0  # so that we start from vertex '0'
        # since we need all V vertices in our MST
        # 0 will be included in the beginning (key[0] = 0 is minimum) ,
        # we will need V-1 more vertices to cover whole graph
        for count in range(1, V):
            u = self.minKey(V, inMST, key)
            inMST[u] = True

            for v in range(V):
                if graph[u][v] != 0 and inMST[v] == False and graph[u][v] < key[v]:
                    key[v] = graph[u][v]
                    parent[v] = u
        sum = 0
        for i in range(1, V):
            sum += key[i]
        return sum


Approach2 = Solution

if __name__ == "__main__":
    adj = [[[1, 5], [2, 1]], [[0, 5], [2, 3]], [[1, 3], [0, 1]]]
    assert Approach1().spanningTree(3, adj) == 4
    graph = [[0, 5, 1], [5, 0, 3], [1, 3, 0]]
    assert Approach2().spanningTree(3, 3, graph) == 4
    print("ok")
