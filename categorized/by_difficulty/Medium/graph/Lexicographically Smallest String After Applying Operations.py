#      Scroll below to see JAVA code also (Java sections skipped in this Python port)
#
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=SUkbctHiREI
#     Company Tags                : will update later
#     Leetcode Link               : https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations

from typing import List
from collections import deque
import sys

sys.setrecursionlimit(1000000)  # Approach-2 recurses once per distinct reachable string


# ****************************************************************** C++ (ported to Python) ******************************************************************
# Approach-1 (Using BFS)
# T.C : O(n^2)
# More Detailed TC : O(n × (n / gcd(n, b)) × (10 / gcd(10, a))) -> Here, n / gcd(n, b) represents the number of unique rotations possible,
# and 10 / gcd(10, a) represents the number of distinct digit patterns achievable through repeated additions modulo 10.
# S.C : O(n^2)
class Solution:
    def rotate(self, s: str, b: int) -> str:
        # C++ mutates the string in place via reference; Python strings are immutable,
        # so we work on a list of chars and return the new string.
        s = list(s)
        s.reverse()
        s[:b] = s[:b][::-1]
        s[b:] = s[b:][::-1]
        return "".join(s)

    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        smallestString = s

        visited = set()
        que = deque()
        que.append(s)
        visited.add(s)

        while que:
            curr = que.popleft()

            if curr < smallestString:
                smallestString = curr

            # Add a to the digits
            temp = list(curr)
            for i in range(1, len(temp), 2):
                temp[i] = chr(((ord(temp[i]) - ord('0') + a) % 10) + ord('0'))
            temp = "".join(temp)

            if temp not in visited:
                visited.add(temp)
                que.append(temp)

            # Rotate right by b
            curr = self.rotate(curr, b)
            if curr not in visited:
                visited.add(curr)
                que.append(curr)

        return smallestString


Approach1 = Solution


# Approach-2 (Using DFS)
# T.C : O(n^2)
# More Detailed TC : O(n × (n / gcd(n, b)) × (10 / gcd(10, a))) -> Here, n / gcd(n, b) represents the number of unique rotations possible,
# and 10 / gcd(10, a) represents the number of distinct digit patterns achievable through repeated additions modulo 10.
# S.C : O(n^2)
class Solution:
    def rotate(self, s: str, b: int) -> str:
        # C++ mutates the string in place via reference; here we return the new string.
        s = list(s)
        s.reverse()
        s[:b] = s[:b][::-1]
        s[b:] = s[b:][::-1]
        return "".join(s)

    def dfs(self, curr: str, a: int, b: int, visited: set, smallestString: List[str]) -> None:
        # smallestString is a 1-element list standing in for C++ `string &`
        if curr in visited:
            return
        visited.add(curr)
        if curr < smallestString[0]:
            smallestString[0] = curr

        added = list(curr)
        for i in range(1, len(added), 2):
            added[i] = chr(((ord(added[i]) - ord('0') + a) % 10) + ord('0'))
        self.dfs("".join(added), a, b, visited, smallestString)

        curr = self.rotate(curr, b)
        self.dfs(curr, a, b, visited, smallestString)

    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        visited = set()
        smallestString = [s]
        self.dfs(s, a, b, visited, smallestString)
        return smallestString[0]


Approach2 = Solution


if __name__ == "__main__":
    for cls in (Approach1, Approach2):
        assert cls().findLexSmallestString("5525", 9, 2) == "2050"
        assert cls().findLexSmallestString("74", 5, 1) == "24"
        assert cls().findLexSmallestString("0011", 4, 2) == "0011"
    print("ok")
