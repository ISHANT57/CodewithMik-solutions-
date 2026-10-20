#     Company Tags  : Google
#     Leetcode Link : https://leetcode.com/problems/the-maze/
#     Description
#
#     There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up,
#     down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
#     Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.
#     The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders
#     of the maze are all walls. The start and destination coordinates are represented by row and column indexes.
#
#     1.There is only one ball and one destination in the maze.
#     2.Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
#     3.The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
#     5.The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
#
#     Example 1:
#     Input:
#     map =
#         [
#          [0,0,1,0,0],
#          [0,0,0,0,0],
#          [0,0,0,1,0],
#          [1,1,0,1,1],
#          [0,0,0,0,0]
#         ]
#     start = [0,4]
#     end = [3,2]
#     Output:
#     false

# Two approaches :  DFS and BFS

import sys
from collections import deque
from typing import List

sys.setrecursionlimit(100000)


class Solution:
    def __init__(self):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.end_x = 0
        self.end_y = 0
        self.visited = []

    # ********************DFS************************
    def DFS(self, maze: List[List[int]], x: int, y: int) -> bool:
        if x == self.end_x and y == self.end_y:
            return True

        if self.visited[x][y]:
            return False

        self.visited[x][y] = True
        for p in self.directions:
            x_ = x + p[0]
            y_ = y + p[1]

            # The only difference here with normal DFS is that in this case, the neighbors are
            # those nodes where the balls hits a wall. That's where it explores other paths.
            while x_ >= 0 and x_ < len(maze) and y_ >= 0 and y_ < len(maze[0]) and maze[x_][y_] == 0:
                x_ += p[0]
                y_ += p[1]

            x_ -= p[0]
            y_ -= p[1]
            if not self.visited[x_][y_] and self.DFS(maze, x_, y_):
                return True
        return False

    # ********************BFS************************
    def BFS(self, maze: List[List[int]], x: int, y: int) -> bool:
        que = deque()
        que.append((x, y))
        self.visited[x][y] = True
        while que:
            curr = que.popleft()

            if curr[0] == self.end_x and curr[1] == self.end_y:
                return True

            for p in self.directions:
                x_ = curr[0] + p[0]
                y_ = curr[1] + p[1]

                # The only difference here with normal BFS is that in this case, the neighbors are
                # those nodes where the balls hits a wall. That's where it explores other paths.
                while x_ >= 0 and x_ < len(maze) and y_ >= 0 and y_ < len(maze[0]) and maze[x_][y_] == 0:
                    x_ += p[0]
                    y_ += p[1]

                x_ -= p[0]
                y_ -= p[1]

                if not self.visited[x_][y_]:
                    que.append((x_, y_))
                    self.visited[x_][y_] = True

        return False

    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        x = start[0]
        y = start[1]
        self.visited = [[False] * 101 for _ in range(101)]
        self.end_x = destination[0]
        self.end_y = destination[1]

        return self.DFS(maze, x, y)


Approach1 = Solution

if __name__ == "__main__":
    maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
    assert Solution().hasPath(maze, [0, 4], [3, 2]) is False
    assert Solution().hasPath(maze, [0, 4], [4, 4]) is True
    s = Solution()
    s.visited = [[False] * 101 for _ in range(101)]
    s.end_x, s.end_y = 4, 4
    assert s.BFS(maze, 0, 4) is True  # BFS helper tested directly (hasPath calls DFS, as in the source)
    print("ok")
