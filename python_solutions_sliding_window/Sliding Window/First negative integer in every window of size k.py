# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=-uc7OCrjp8g
# Company Tags                : Amazon, MentorGraphics
# Qn Link                     : https://practice.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1#
# (GFG problem; the original is a free function, wrapped in class Solution here)

from typing import List
from collections import deque


class Solution:
    def printFirstNegativeInteger(self, A: List[int], N: int, k: int) -> List[int]:
        dll = deque()  # You can use queue, dequeue etc as well (std::list -> deque)
        result = []
        i = 0
        j = 0

        while j < N:
            if A[j] < 0:
                dll.append(A[j])

            if j - i + 1 == k:
                neg = 0 if not dll else dll[0]
                result.append(neg)
                if A[i] < 0 and dll:
                    dll.popleft()
                i += 1
            j += 1
        return result


Approach1 = Solution


# Approach-2 (Another good way to solve this)
class Solution:
    def printFirstNegativeInteger(self, A: List[int], N: int, K: int) -> List[int]:

        deq = deque()
        result = []

        for i in range(K):
            if A[i] < 0:
                deq.append(i)

        for i in range(K, N):
            if deq:
                result.append(A[deq[0]])
            else:
                result.append(0)

            while deq and deq[0] < i - K + 1:
                deq.popleft()

            if A[i] < 0:
                deq.append(i)

        if deq:
            result.append(A[deq[0]])
        else:
            result.append(0)

        return result


Approach2 = Solution


if __name__ == "__main__":
    for A in (Approach1, Approach2):
        assert A().printFirstNegativeInteger([-8, 2, 3, -6, 10], 5, 2) == [-8, 0, -6, -6]
        assert A().printFirstNegativeInteger([12, -1, -7, 8, -15, 30, 16, 28], 8, 3) == [-1, -1, -7, -15, -15, 0]
    print("ok")
