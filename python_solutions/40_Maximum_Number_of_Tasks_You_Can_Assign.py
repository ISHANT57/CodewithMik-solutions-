#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=7tGM7XA06MI
#     Company Tags                : Will update soon
#     Leetcode Link               : https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign

from typing import List
import bisect  # used in place of C++ multiset (sorted list + bisect), since Python has no multiset


# Approach (Binary Search on Answer)
# T.C : O(MLogM+NLogN+Min(M,N)∗Log(Min(M,N))∗Log(Min(M,N))), M = tasks.size(), N = workers.size()
# S.C : O(M)
class Solution:
    def check(self, tasks: List[int], workers: List[int], pills: int, strength: int, mid: int) -> bool:
        pillsUsed = 0
        # multiset<int> -> sorted list (ascending); st[-1] == *prev(st.end())
        st = sorted(workers[:mid])  # best mid workers

        for i in range(mid - 1, -1, -1):
            reqrd = tasks[i]

            if st[-1] >= reqrd:
                st.pop()
            elif pillsUsed >= pills:
                return False
            else:
                # find the weakest worker which can do this strong task using pills
                idx = bisect.bisect_left(st, reqrd - strength)  # lower_bound
                if idx == len(st):
                    return False
                del st[idx]
                pillsUsed += 1

        return True

    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        m = len(tasks)
        n = len(workers)

        l = 0
        r = min(m, n)

        tasks.sort()
        workers.sort(reverse=True)  # greater<int>()

        result = 0

        while l <= r:
            mid = l + (r - l) // 2

            if self.check(tasks, workers, pills, strength, mid):
                result = mid
                l = mid + 1
            else:
                r = mid - 1

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.maxTaskAssign([3, 2, 1], [0, 3, 3], 1, 1))  # 3
    print(s.maxTaskAssign([5, 4], [0, 0, 0], 1, 5))  # 1
    print(s.maxTaskAssign([10, 15, 30], [0, 10, 10, 10, 10], 3, 10))  # 2
