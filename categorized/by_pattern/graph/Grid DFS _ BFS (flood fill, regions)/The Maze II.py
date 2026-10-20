#     Company Tags  : Google, NetEase
#     Leetcode Link : https://leetcode.com/problems/the-maze-ii/
#
#     Description
#
#     There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down,
#     left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
#     Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the
#     destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded)
#     to the destination (included). If the ball cannot stop at the destination, return -1. The maze is represented by a binary
#     2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls.
#     The start and destination coordinates are represented by row and column indexes.
#
#     1.There is only one ball and one destination in the maze.
#     2.Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
#     3.The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
#     4.The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
#
#     Example :
#       Input:
#       (rowStart, colStart) = (0,4)
#       (rowDest, colDest)= (4,4)
#       0 0 1 0 0
#       0 0 0 0 0
#       0 0 0 1 0
#       1 1 0 1 1
#       0 0 0 0 0
#
#       Output:  12
#       Explanation:
#       (0,4)->(0,3)->(1,3)->(1,2)->(1,1)->(1,0)->(2,0)->(2,1)->(2,2)->(3,2)->(4,2)->(4,3)->(4,4)

#     2 Approaches : DFS, BFS

import sys
from collections import deque
from typing import List

sys.setrecursionlimit(100000)


# Approach-1 (DFS)
class Solution:
    def __init__(self):
        self.end_x = 0
        self.end_y = 0
        self.m = 0
        self.n = 0
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.t = []

    def DFS(self, maze: List[List[int]], x: int, y: int):

        for dir in self.directions:
            steps = 0
            x_ = x
            y_ = y

            while x_ >= 0 and x_ < self.m and y_ >= 0 and y_ < self.n and maze[x_][y_] == 0:
                x_ += dir[0]
                y_ += dir[1]
                steps += 1

            x_ -= dir[0]
            y_ -= dir[1]
            steps -= 1

            # I will go to x_,y_ only if I get better result
            # That's why we don't have to keep track of visited nodes in this prpblem
            # If I find that there is a better path to reach (x_, y_) i.e. from (x, y)
            # we update the value and move ahead
            if self.t[x][y] + steps < self.t[x_][y_]:
                self.t[x_][y_] = self.t[x][y] + steps
                self.DFS(maze, x_, y_)

    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        self.end_x = destination[0]
        self.end_y = destination[1]
        self.m = len(maze)
        self.n = len(maze[0])
        self.t = [[2**31 - 1] * self.n for _ in range(self.m)]

        self.t[start[0]][start[1]] = 0
        self.DFS(maze, start[0], start[1])

        return -1 if self.t[self.end_x][self.end_y] == 2**31 - 1 else self.t[self.end_x][self.end_y]


Approach1 = Solution


# Approach-2 (BFS)
class Solution:
    def __init__(self):
        self.end_x = 0
        self.end_y = 0
        self.m = 0
        self.n = 0
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.t = []

    # NOTE: the C++ BFS is declared int but has no return statement; the result is unused, so nothing is returned here
    def BFS(self, maze: List[List[int]], x: int, y: int):
        que = deque()
        que.append((x, y))

        while que:
            curr = que.popleft()

            for dir in self.directions:
                x_ = curr[0]
                y_ = curr[1]
                steps = 0
                while x_ >= 0 and x_ < self.m and y_ >= 0 and y_ < self.n and maze[x_][y_] == 0:
                    x_ += dir[0]
                    y_ += dir[1]
                    steps += 1

                x_ -= dir[0]
                y_ -= dir[1]
                steps -= 1

                if self.t[curr[0]][curr[1]] + steps < self.t[x_][y_]:
                    self.t[x_][y_] = self.t[curr[0]][curr[1]] + steps
                    que.append((x_, y_))

    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        self.end_x = destination[0]
        self.end_y = destination[1]
        self.m = len(maze)
        self.n = len(maze[0])
        self.t = [[2**31 - 1] * self.n for _ in range(self.m)]

        self.t[start[0]][start[1]] = 0
        self.BFS(maze, start[0], start[1])

        return -1 if self.t[self.end_x][self.end_y] == 2**31 - 1 else self.t[self.end_x][self.end_y]


Approach2 = Solution

if __name__ == "__main__":
    maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
    for A in (Approach1, Approach2):
        assert A().shortestDistance(maze, [0, 4], [4, 4]) == 12
        assert A().shortestDistance(maze, [0, 4], [3, 2]) == -1
    print("ok")
