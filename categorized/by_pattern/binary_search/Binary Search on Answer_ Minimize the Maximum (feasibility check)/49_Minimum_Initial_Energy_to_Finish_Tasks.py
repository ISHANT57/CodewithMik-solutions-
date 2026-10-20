#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=Bw0HySng9wo
#     Company Tags                : Will update soon
#     Leetcode Link               : https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/

from typing import List


# Approach (Binary search on answer + greedy sorting)
# T.C : O(n*logn)
# S.C : O(1)
class Solution:

    def isPossible(self, tasks: List[List[int]], mid: int) -> bool:
        for task in tasks:
            actual = task[0]
            minimum = task[1]

            if minimum > mid:
                return False

            mid -= actual

        return True

    def minimumEffort(self, tasks: List[List[int]]) -> int:
        n = len(tasks)

        l = 0
        r = 10**9

        result = 2**31 - 1  # INT_MAX

        # sort by (minimum - actual) descending
        lambda_key = lambda task: -(task[1] - task[0])

        tasks.sort(key=lambda_key)

        while l <= r:
            mid = l + (r - l) // 2

            if self.isPossible(tasks, mid):
                result = mid
                r = mid - 1
            else:
                l = mid + 1

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.minimumEffort([[1, 2], [2, 4], [4, 8]]))  # 8
    print(s.minimumEffort([[1, 3], [2, 4], [10, 11], [10, 12], [8, 9]]))  # 32
    print(s.minimumEffort([[1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]]))  # 27
