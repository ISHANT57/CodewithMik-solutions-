# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=qDHd9n_XGQ8
# Company Tags                : Google
# Leetcode Link               : https://leetcode.com/problems/keys-and-rooms/

from typing import List

# Using DFS : O(m+n)
class Solution:
    def __init__(self):
        self.count = 1

    def dfs(self, rooms: List[List[int]], u: int, visited: List[bool]) -> None:
        visited[u] = True

        for node in rooms[u]:
            if not visited[node]:
                self.dfs(rooms, node, visited)

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n

        self.dfs(rooms, 0, visited)

        for x in visited:
            if x == False:
                return False
        return True

Approach1 = Solution


if __name__ == "__main__":
    assert Solution().canVisitAllRooms([[1],[2],[3],[]]) == True
    assert Solution().canVisitAllRooms([[1,3],[3,0,1],[2],[0]]) == False
    print("ok")
