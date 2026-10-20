from typing import List
import heapq

#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=_HptwlLP8sI
#     Comoany Tags                : Netease Games
#     Leetcode Link               : https://leetcode.com/problems/most-profit-assigning-work/description/


# Approach-1 (Using max-heap)
# T.C : O(nlogn + mlogn)
# S.C : O(n)
# Note: heapq is a min-heap, so we push negated (prof, diff) to simulate C++ priority_queue<pair<int,int>> (max heap).
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(difficulty)
        m = len(worker)

        pq = []  # max heap of pairs (stored negated)

        for i in range(n):
            diff = difficulty[i]
            prof = profit[i]

            heapq.heappush(pq, (-prof, -diff))

        worker.sort(reverse=True)  # descending order

        i = 0
        totalProfit = 0
        while i < m and pq:
            if -pq[0][1] > worker[i]:  # pq.top().second
                heapq.heappop(pq)
            else:
                totalProfit += -pq[0][0]  # pq.top().first
                i += 1

        return totalProfit


# Approach-2 (Using Binary Search)
# T.C : O(nlogn)
# S.C : O(n)
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(difficulty)
        m = len(worker)

        vec = []
        for i in range(n):
            vec.append([difficulty[i], profit[i]])

        vec.sort()

        # Pre-processing to find the maximum profit till index i at constant time
        for i in range(1, len(vec)):
            vec[i][1] = max(vec[i][1], vec[i - 1][1])

        totalProfit = 0
        for i in range(m):

            workerDiffLevel = worker[i]

            # apply b.search on vec
            l, r = 0, len(vec) - 1
            maxProfit = 0
            while l <= r:
                mid = l + (r - l) // 2
                if vec[mid][0] <= workerDiffLevel:
                    maxProfit = max(maxProfit, vec[mid][1])
                    l = mid + 1
                else:
                    r = mid - 1

            totalProfit += maxProfit

        return totalProfit


# Approach-3 (Using simple iteration and sorting)
# T.C : O(nlogn + mlogm + m + n)
# S.C : O(n)
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(difficulty)
        m = len(worker)

        vec = []
        for i in range(n):
            vec.append([difficulty[i], profit[i]])

        vec.sort()

        worker.sort()

        totalProfit = 0
        j = 0  # pointing to vec
        maxProfit = 0

        for i in range(m):

            while j < n and worker[i] >= vec[j][0]:
                maxProfit = max(maxProfit, vec[j][1])
                j += 1

            totalProfit += maxProfit

        return totalProfit


if __name__ == "__main__":
    print(Solution().maxProfitAssignment([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7]))  # expected 100
    print(Solution().maxProfitAssignment([85, 47, 57], [24, 66, 99], [40, 25, 25]))  # expected 0
