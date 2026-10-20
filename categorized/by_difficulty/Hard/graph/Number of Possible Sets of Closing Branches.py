# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=80pGUfUcBwQ
# Company Tags                : will soon update
# Leetcode Link               : https://leetcode.com/problems/number-of-possible-sets-of-closing-branches

from typing import List

# Approach (Using Floyd Warshal) - Because of following reasons
# It asks for shortest distance between every pair of vertices
# Since the number of vertices is very less 1 <= n <= 10 , we can apply Floyd Warshal - T.C :  O(n^3) of Floyd Warshal
# T.C : O((2^n) * (n^3))
# S.C : O(n^2)
class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        result = 0

        # O(2^n * (n^3))
        for set_ in range(1 << n):  # trying all possible subsets

            grid = [[10**9] * n for _ in range(n)]  # updated graph

            # Update the Graph based on the selected nodes - present in set
            for it in roads:
                u = it[0]
                v = it[1]
                wt = it[2]

                # [[1,0,11],[1,0,16],[0,2,13]]
                if (set_ >> u & 1) and (set_ >> v & 1):
                    grid[u][v] = min(grid[u][v], wt)
                    grid[v][u] = min(grid[v][u], wt)

            for i in range(n):
                grid[i][i] = 0

            # Floyd Warshall to find shortest distance from any node to any other node
            for via in range(n):
                for i in range(n):
                    for j in range(n):
                        grid[i][j] = min(grid[i][j], grid[i][via] + grid[via][j])

            # Check if all shortest paths <= maxDistance
            ok = True
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue

                    if (set_ >> i & 1) and (set_ >> j & 1):
                        if grid[i][j] > maxDistance:
                            ok = False
                            break

            if ok == True:
                result += 1

        return result

Approach1 = Solution


if __name__ == "__main__":
    assert Solution().numberOfSets(3, 5, [[0,1,2],[1,2,10],[0,2,10]]) == 5
    assert Solution().numberOfSets(3, 5, [[0,1,20],[0,1,10],[1,2,2],[0,2,2]]) == 7
    assert Solution().numberOfSets(1, 10, []) == 2
    print("ok")
