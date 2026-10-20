# MY YOUTUBE VIDEO ON THIS Qn  : https://www.youtube.com/watch?v=QHRlC7O-lis
# Also popular as              : Minimum rotations to unlock a circular lock
# Company Tags                 : META
# Leetcode Link                : https://leetcode.com/problems/open-the-lock/
#
# Similar Question :  1. Word Ladder (Leetcode)
#                     2. Gene Mutation (Leetcode)
#                     3. Sequential Digits (Leetcode)
#                     4. Print all Jumping Numbers smaller than or equal to a given value (GFG)

from typing import List
from collections import deque


# Using BFS
# T.C : We have n = 10 slots in each wheel and we have w = 4 wheels. In worst case we will explore all possible combinations.
#       Total Combinations = O(n^w)
# S.C : In worst case we will store all possible combinations in queue O(n^w)
class Solution:
    def fillNeighbors(self, que: deque, curr: str, dead: set) -> None:
        # Python strings are immutable, so work on a list of chars (C++ mutates curr in place)
        curr = list(curr)
        for i in range(4):
            ch = curr[i]

            dec = '9' if ch == '0' else chr(ord(ch) - 1)
            inc = '0' if ch == '9' else chr(ord(ch) + 1)

            curr[i] = dec
            s = "".join(curr)
            if s not in dead:
                dead.add(s)
                que.append(s)

            curr[i] = inc
            s = "".join(curr)
            if s not in dead:
                dead.add(s)
                que.append(s)
            curr[i] = ch

    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)

        start = "0000"
        if start in dead:
            return -1

        que = deque()
        que.append(start)

        level = 0
        while que:
            n = len(que)

            while n > 0:
                n -= 1
                curr = que.popleft()
                if curr == target:
                    return level

                self.fillNeighbors(que, curr, dead)
            level += 1
        return -1


Approach1 = Solution

# (Java section of the original file skipped: duplicate of the C++ approach)

if __name__ == "__main__":
    assert Solution().openLock(["0201", "0101", "0102", "1212", "2002"], "0202") == 6
    assert Solution().openLock(["8888"], "0009") == 1
    assert Solution().openLock(["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888") == -1
    print("ok")
