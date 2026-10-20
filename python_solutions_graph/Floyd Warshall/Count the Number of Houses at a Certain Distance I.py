#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=Uhy8lnno7hE
#     Company Tags                : will soon update
#     Leetcode Link               : https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/

from typing import List


# **************************************************************** C++ ****************************************************************
# T.C : O(n^3)
# S.C : O(n^2)
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        grid = [[100000] * (n + 1) for _ in range(n + 1)]

        for j in range(1, n):
            grid[j][j + 1] = 1
            grid[j + 1][j] = 1
        grid[x][y] = 1
        grid[y][x] = 1

        for via in range(1, n + 1):

            for i in range(1, n + 1):
                for j in range(1, n + 1):

                    grid[i][j] = min(grid[i][j], grid[i][via] + grid[via][j])

        result = [0] * n
        for i in range(1, n + 1):
            for j in range(1, n + 1):

                if i != j:
                    val = grid[i][j]
                    result[val - 1] += 1

        return result


Approach1 = Solution


if __name__ == "__main__":
    s = Solution()
    assert s.countOfPairs(3, 1, 3) == [6, 0, 0]
    assert s.countOfPairs(5, 2, 4) == [10, 8, 2, 0, 0]
    assert s.countOfPairs(4, 1, 1) == [6, 4, 2, 0]
    print("ok")
