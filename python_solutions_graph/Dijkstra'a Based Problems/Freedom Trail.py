#     Scroll down to see JAVA code also
#
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=yUNjMFE1tGo
#     Company Tags                : GOOGLE
#     Leetcode Link               : https://leetcode.com/problems/freedom-trail
#     DP Solution                 : https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/DP/DP%20on%20Strings/Freedom%20Trail.cpp

from typing import List
from collections import defaultdict
import heapq

# Approach (Using DIjkstra's)
# T.C : O(nm log(nm)) where n = length of ring, m = length of keyword. n*m = maximum number of pairs we visit is the number of unique possible pairs and push and pop
      # operations will take log(n*m)
# S.C : O(n*m) pairs stored in heap
class Solution:
    def countSteps(self, ringIndex: int, i: int, n: int) -> int:
        dist       = abs(i - ringIndex)
        wrapAround = n - dist

        return min(dist, wrapAround)

    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        m = len(key)

        adj = defaultdict(list)  # char --> {indices in ring where char is present}
        for i in range(n):
            ch = ring[i]
            adj[ch].append(i)

        pq = []  # min-heap of [steps, ringIndex, keyIndex]
        heapq.heappush(pq, [0, 0, 0])

        visited = set()  # set<pair<int,int>>

        totalSteps = 0
        while pq:
            vec = heapq.heappop(pq)

            totalSteps = vec[0]
            ringIndex  = vec[1]
            keyIndex   = vec[2]

            if keyIndex == m:
                break

            if (ringIndex, keyIndex) in visited:
                continue

            visited.add((ringIndex, keyIndex))

            for nextIndex in adj[key[keyIndex]]:
                heapq.heappush(pq, [totalSteps + self.countSteps(ringIndex, nextIndex, n),
                                    nextIndex, keyIndex + 1])

        return totalSteps + m  # Note : totalSteps is for bringing each character to 12:00 position and then printing each of them will take m steps

Approach1 = Solution


if __name__ == "__main__":
    s = Solution()
    assert s.findRotateSteps("godding", "gd") == 4
    assert s.findRotateSteps("godding", "godding") == 13
    print("ok")
