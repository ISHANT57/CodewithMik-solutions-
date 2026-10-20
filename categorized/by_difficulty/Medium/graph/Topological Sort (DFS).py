# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=WbbYZRr4arw
# Company Tags                : Moonfrog Labs, Flipkart, Morgan Stanley, Accolite, Amazon, Microsoft

# NOTE : This assumes that, we don't have cycle in the given directed graph. You can simply add few things in the same code to check for cycle also
# Or, see this : https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Graph/Topological%20Sorting/Course%20Schedule.cpp
import sys
from typing import List

sys.setrecursionlimit(10000)


class Solution:

    def DFS(self, adj: List[List[int]], u: int, visited: List[bool], st: List[int]) -> None:
        visited[u] = True

        # pehle mere ('u' ke node ke ) bachho ko daalo
        for v in adj[u]:
            if not visited[v]:
                self.DFS(adj, v, visited, st)

        # ab mujhe daalo stack me
        st.append(u)  # stack<int> -> list (append = push, pop = pop)

    # Function to return list containing vertices in Topological order.
    def topoSort(self, V: int, adj: List[List[int]]) -> List[int]:
        visited = [False] * V
        st = []

        for i in range(V):
            if not visited[i]:
                self.DFS(adj, i, visited, st)

        result = []

        while st:
            result.append(st.pop())

        return result


Approach1 = Solution

if __name__ == "__main__":
    adj = [[], [], [3], [1], [0, 1], [0, 2]]
    res = Solution().topoSort(6, adj)
    pos = {x: i for i, x in enumerate(res)}
    assert len(res) == 6 and all(pos[u] < pos[v] for u in range(6) for v in adj[u])
    print("ok", res)
