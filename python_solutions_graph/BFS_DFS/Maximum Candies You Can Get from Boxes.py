# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=fGa9jczRS2o
# Company Tags                : will update later
# Leetcode Link               : https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes

from typing import List
from collections import deque


# ****************************************************************** C++ ******************************************************************
# Approach-1 (Using DFS)
# T.C : O(n), where n =  number of boxes, we don't visit any box more than once
# S.C : O(n)
class Solution:

    def dfs(self, box: int, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], visited: set, foundBoxes: set) -> int:

        if box in visited:
            return 0

        if status[box] == 0:
            foundBoxes.add(box)
            return 0

        visited.add(box)
        candiesCollected = candies[box]

        for insideBox in containedBoxes[box]:
            candiesCollected += self.dfs(insideBox, status, candies, keys, containedBoxes, visited, foundBoxes)

        for boxKey in keys[box]:
            status[boxKey] = 1  # can be opened
            if boxKey in foundBoxes:
                candiesCollected += self.dfs(boxKey, status, candies, keys, containedBoxes, visited, foundBoxes)

        return candiesCollected

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:

        candiesCollected = 0
        visited = set()
        foundBoxes = set()
        # T.C : O(n) visiting all box only once , n = number of boxes
        # S.C : O(n)
        for box in initialBoxes:
            candiesCollected += self.dfs(box, status, candies, keys, containedBoxes, visited, foundBoxes)

        return candiesCollected


Approach1 = Solution


# Approach-2 (Using BFS)
# T.C : O(n), where n =  number of boxes, we don't visit any box more than once
# S.C : O(n)
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:

        candiesCollected = 0
        visited = set()
        foundBoxes = set()
        # T.C : O(n) visiting all box only once , n = number of boxes
        # S.C : O(n)

        que = deque()  # insert those which you have now and you can open it
        for box in initialBoxes:
            foundBoxes.add(box)
            if status[box] == 1:
                que.append(box)
                visited.add(box)
                candiesCollected += candies[box]

        while que:
            box = que.popleft()

            for insideBox in containedBoxes[box]:
                foundBoxes.add(insideBox)
                if status[insideBox] == 1 and insideBox not in visited:
                    que.append(insideBox)
                    visited.add(insideBox)
                    candiesCollected += candies[insideBox]

            for boxKey in keys[box]:
                status[boxKey] = 1  # can be opened in future if we reach this box
                if boxKey in foundBoxes and boxKey not in visited:
                    que.append(boxKey)
                    visited.add(boxKey)
                    candiesCollected += candies[boxKey]

        return candiesCollected


Approach2 = Solution

# (The Java section of the original file duplicates the above and is skipped.)


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10**6)
    for S in (Approach1, Approach2):
        assert S().maxCandies([1,0,1,0], [7,5,4,100], [[],[],[1],[]], [[1,2],[3],[],[]], [0]) == 16
        assert S().maxCandies([1,0,0,0,0,0], [1,1,1,1,1,1], [[1,2,3,4,5],[],[],[],[],[]], [[1,2,3,4,5],[],[],[],[],[]], [0]) == 6
    print("ok")
