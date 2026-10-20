# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=3tgekNXWXsY
# Company Tags                :  Amazon, Cisco, Samsung
# GfG Link                    : https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1

from typing import List


class Solution:
    # DSU Code
    def __init__(self):
        self.parent = []
        self.rank = []

    def find(self, x: int) -> int:
        if x == self.parent[x]:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def Union(self, x: int, y: int) -> None:
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent == y_parent:
            return

        if self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
        elif self.rank[x_parent] < self.rank[y_parent]:
            self.parent[x_parent] = y_parent
        else:
            self.parent[x_parent] = y_parent
            self.rank[y_parent] += 1

    def Kruskal(self, vec: List[List[int]]) -> int:
        sum = 0
        for temp in vec:
            u = temp[0]
            v = temp[1]
            wt = temp[2]

            parent_u = self.find(u)
            parent_v = self.find(v)

            if parent_u != parent_v:
                self.Union(u, v)
                sum += wt

        # if(edgesConnexted != V-1)
        #     "It's not a MST" - REMEMBER THIS ALWAYS if anyone asks you how to check if we formed an MST or not

        return sum

    # Function to find sum of weights of edges of the Minimum Spanning Tree.
    # adj: list of V lists, each entry is [neighbor, weight] (C++ vector<vector<int>> adj[])
    def spanningTree(self, V: int, adj: List[List[List[int]]]) -> int:
        self.parent = [0] * V
        self.rank = [0] * V

        for i in range(V):
            self.parent[i] = i

        vec = []

        for i in range(V):
            for temp in adj[i]:
                u = i
                v = temp[0]
                d = temp[1]

                vec.append([u, v, d])

        lam = lambda v1: v1[2]

        vec.sort(key=lam)

        return self.Kruskal(vec)


Approach1 = Solution

if __name__ == "__main__":
    # GfG example: V=3, edges 0-1 (5), 1-2 (3), 0-2 (1) -> 4
    adj = [[[1, 5], [2, 1]], [[0, 5], [2, 3]], [[1, 3], [0, 1]]]
    assert Solution().spanningTree(3, adj) == 4
    print("ok")
