#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=w0QJQtMxUfk
#     Company Tags                : Will update soon
#     Leetcode Link               : https://leetcode.com/problems/separate-squares-i/description/

from typing import List


# Approach (Binary search on answer)
# T.C : O(n * log(range)), range = max (y+side) value - min y value
# S.C : O(1)
class Solution:
    def check(self, squares: List[List[int]], mid_y: float, total: float) -> bool:
        bot_area = 0.0

        for square in squares:
            y = float(square[1])
            l = float(square[2])

            boty = y
            topy = y + l

            if mid_y >= topy:
                # full square below
                bot_area += l * l
            elif mid_y > boty:
                # partial area below
                bot_area += (mid_y - boty) * l

        return bot_area >= total / 2.0  # Is bottom area more than above ?

    def separateSquares(self, squares: List[List[int]]) -> float:
        low = float(2**31 - 1)  # INT_MAX
        high = float(-2**31)  # INT_MIN
        total = 0.00000

        for square in squares:
            x = float(square[0])
            y = float(square[1])
            l = float(square[2])
            total += l * l

            low = min(low, y)
            high = max(high, y + l)

        result_y = 0.00000

        while high - low > 1e-5:
            mid_y = low + (high - low) / 2

            result_y = mid_y

            if self.check(squares, mid_y, total) == True:  # bottom area is greater
                # shift mid_y down side to balance area
                high = mid_y
            else:
                low = mid_y

        return result_y


if __name__ == "__main__":
    s = Solution()
    print(s.separateSquares([[0, 0, 1], [2, 2, 1]]))  # 1.0
    print(s.separateSquares([[0, 0, 2], [1, 1, 1]]))  # 1.16667
