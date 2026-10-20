# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=p4y_rQeB2mg
# Company Tags                : ADOBE
# Leetcode Link               : https://leetcode.com/problems/maximum-total-importance-of-roads

from typing import List

# ***************************************************************************** C++ *****************************************************************************
# Approach (using degree and assiging value greedily)
# T.C : O(E + nlogn)
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # n = total number of nodes numbered from 0 to n-1

        degree = [0] * n

        for vec in roads:
            u = vec[0]
            v = vec[1]

            degree[u] += 1
            degree[v] += 1

        degree.sort()  # ascedning order

        value = 1
        sum_ = 0

        for i in range(n):
            sum_ += (degree[i] * value)
            value += 1

        return sum_

Approach1 = Solution


if __name__ == "__main__":
    assert Solution().maximumImportance(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]) == 43
    assert Solution().maximumImportance(5, [[0,3],[2,4],[1,3]]) == 20
    print("ok")
