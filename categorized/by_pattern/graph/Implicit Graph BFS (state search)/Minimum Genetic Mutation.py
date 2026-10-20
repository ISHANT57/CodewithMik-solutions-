# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=H3kSFSv-t30
# Company Tags                : Twitter
# Leetcode Link               : https://leetcode.com/problems/minimum-genetic-mutation/

from typing import List
from collections import deque


# Just like Word Ladder
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bankset = set(bank)

        visited = set()
        que = deque()
        que.append(start)
        visited.add(start)

        level = 0

        while que:
            n = len(que)

            while n:
                n -= 1
                curr = que.popleft()

                if curr == end:
                    return level

                for ch in "ACGT":
                    for i in range(len(curr)):
                        neighbour = curr[:i] + ch + curr[i + 1:]

                        if neighbour not in visited and neighbour in bankset:
                            visited.add(neighbour)
                            que.append(neighbour)
            level += 1

        return -1


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]) == 1
    assert Solution().minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]) == 2
    assert Solution().minMutation("AACCGGTT", "AACCGGTA", []) == -1
    print("ok")
