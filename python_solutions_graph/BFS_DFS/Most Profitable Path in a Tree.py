# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=uJiDHHChF58
# Company Tags                : Intuit
# Leetcode Link               : https://leetcode.com/problems/most-profitable-path-in-a-tree

from typing import List
from collections import deque, defaultdict


# ****************************************************************** C++ ******************************************************************
# Approach-1 (DFS for Bob and DFS for Alice)
# T.C : O(n)
# S.C : O(n)
class Solution:
    def __init__(self):
        self.adj = defaultdict(list)  # unordered_map<int, vector<int>>
        self.bobMap = {}              # unordered_map<int, int>
        self.aliceIncome = 0

    def DFSBob(self, curr: int, t: int, visited: List[bool]) -> bool:
        visited[curr] = True
        self.bobMap[curr] = t

        if curr == 0:  # reached target
            return True

        for ngbr in self.adj[curr]:
            if not visited[ngbr]:
                if self.DFSBob(ngbr, t + 1, visited) == True:
                    return True

        del self.bobMap[curr]
        return False

    def DFSAlice(self, curr: int, t: int, income: int, visited: List[bool], amount: List[int]) -> None:
        visited[curr] = True

        if curr not in self.bobMap or t < self.bobMap[curr]:
            income += amount[curr]
        elif t == self.bobMap[curr]:
            income += int(amount[curr] / 2)  # C++ int division truncates toward zero

        if len(self.adj[curr]) == 1 and curr != 0:  # leaf node
            self.aliceIncome = max(self.aliceIncome, income)

        """
            {1} -> (2, 3)
            2 -> 1
            3 -> 1,....
            (1) ---- (2)
             |
             |
             (3)------.....
        """

        for ngbr in self.adj[curr]:
            if not visited[ngbr]:
                self.DFSAlice(ngbr, t + 1, income, visited, amount)

    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)  # n nodes (0 to n-1)

        self.aliceIncome = -2**31  # INT_MIN
        for edge in edges:
            u = edge[0]
            v = edge[1]

            self.adj[u].append(v)
            self.adj[v].append(u)

        # DFS on Bob for finding time to reach each node till 0
        time = 0
        visited = [False] * n
        self.DFSBob(bob, time, visited)

        income = 0
        visited = [False] * n  # visited.assign(n, false)
        self.DFSAlice(0, 0, income, visited, amount)

        return self.aliceIncome


Approach1 = Solution


# Approach-2 (DFS for Bob and BFS for Alice)
# T.C : O(n)
# S.C : O(n)
class Solution:
    def __init__(self):
        self.adj = defaultdict(list)  # unordered_map<int, vector<int>>
        self.bobMap = {}              # unordered_map<int, int>
        self.aliceIncome = 0

    def DFSBob(self, curr: int, t: int, visited: List[bool]) -> bool:
        visited[curr] = True
        self.bobMap[curr] = t

        if curr == 0:  # reached target
            return True

        for ngbr in self.adj[curr]:
            if not visited[ngbr]:
                if self.DFSBob(ngbr, t + 1, visited) == True:
                    return True

        del self.bobMap[curr]
        return False

    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)  # n nodes (0 to n-1)

        self.aliceIncome = -2**31  # INT_MIN
        for edge in edges:
            u = edge[0]
            v = edge[1]

            self.adj[u].append(v)
            self.adj[v].append(u)

        # DFS on Bob for finding time to reach each node till 0
        time = 0
        visited = [False] * n
        self.DFSBob(bob, time, visited)

        income = 0
        visited = [False] * n  # visited.assign(n, false)

        # BFS se karunga
        que = deque()
        # {node, time, income}
        que.append([0, 0, 0])

        while que:
            curr = que[0][0]
            t = que[0][1]
            income = que[0][2]

            que.popleft()

            if curr not in self.bobMap or self.bobMap[curr] > t:
                income += amount[curr]
            elif t == self.bobMap[curr]:
                income += int(amount[curr] / 2)  # C++ int division truncates toward zero

            if len(self.adj[curr]) == 1 and curr != 0:
                self.aliceIncome = max(self.aliceIncome, income)

            for ngbr in self.adj[curr]:
                if not visited[ngbr]:
                    que.append([ngbr, t + 1, income])

            visited[curr] = True

        return self.aliceIncome


Approach2 = Solution

# (The Java section of the original file duplicates the above and is skipped.)


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10**6)
    for S in (Approach1, Approach2):
        assert S().mostProfitablePath([[0,1],[1,2],[1,3],[3,4]], 3, [-2,4,2,-4,6]) == 6
        assert S().mostProfitablePath([[0,1]], 1, [-7280,2350]) == -7280
    print("ok")
