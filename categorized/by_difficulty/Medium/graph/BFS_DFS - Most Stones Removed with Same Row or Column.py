# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=ZsGTpXm966E
# Company Tags                : Google
# Leetcode Link               : https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
#
# Please see the "Disjoint Set" solution : https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Graph/Disjoint%20Set/Most%20Stones%20Removed%20with%20Same%20Row%20or%20Column.cpp

from typing import List


# ************************************************ C++ ************************************************
# T.C : O(n^2)
# S.C : O(n)
class Solution:
    def dfs(self, stones: List[List[int]], index: int, visited: List[bool]) -> None:
        visited[index] = True

        for i in range(self.n):
            if (not visited[i] and
                    ((stones[i][0] == stones[index][0]) or (stones[i][1] == stones[index][1]))):
                self.dfs(stones, i, visited)

    def removeStones(self, stones: List[List[int]]) -> int:
        self.n = len(stones)
        n = self.n
        visited = [False] * n

        count = 0
        for i in range(n):
            if visited[i]:
                continue
            self.dfs(stones, i, visited)
            count += 1

        return n - count


Approach1 = Solution

# (The Java section of the original file is a duplicate of the above and is skipped.)


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10**6)
    assert Solution().removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]) == 5
    assert Solution().removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]) == 3
    assert Solution().removeStones([[0,0]]) == 0
    print("ok")
