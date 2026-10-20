from typing import List

# MY YOUTUBE VIDEO ON THIS Qn : https://youtu.be/NYk3IuJinuc
# Company Tags                : Accolite, MentorGraphics, Adobe, Amazon, Directi, Goldman Sachs, Groupon,
#                               InMobi, MakeMyTrip, Ola Cabs, One97, Oracle, Paytm, Polycom,
#                               SAP Labs, Snapdeal, TinyOwl, Visa, Microsoft
#
# Leetcode Link               : https://leetcode.com/problems/search-a-2d-matrix/
# GfG Link                    : https://practice.geeksforgeeks.org/problems/search-in-a-matrix17201720/1


# Approach-1 O(m*n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        i, j = 0, n - 1

        while i < m and j >= 0:
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else:
                return True

        return False


Approach1 = Solution


# Approach-2 (Using Binary Search) O(log(m*n))
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        start = 0
        end = m * n - 1

        while start <= end:
            mid = start + (end - start) // 2

            row = mid // n
            col = mid % n

            if matrix[row][col] > target:
                end = mid - 1
            elif matrix[row][col] < target:
                start = mid + 1
            else:
                return True

        return False


Approach2 = Solution


if __name__ == "__main__":
    mat = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    for sol in (Approach1(), Approach2()):
        assert sol.searchMatrix(mat, 3) is True
        assert sol.searchMatrix(mat, 13) is False
    print("OK")
