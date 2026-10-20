# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=7xvAJkNMHO0
# Company Tag                 : will update later
# Leetcode Link               : https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string

# Approach-1 (Brute Force)
# T.C : O(n^3)
# S.C : O(n), for temp string of length n
from typing import List


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)

        for length in range(k, n + 1):  # 'len' in C++; renamed to avoid shadowing Python builtin

            result = ""

            for start in range(0, n - length + 1):  # trying all possible substr of len
                temp = s[start:start + length]  # [start ... start+len]

                ones = 0
                for ch in temp:
                    ones += 1 if ch == '1' else 0

                # Keep it if it's beautiful and smaller than current best.
                if ones == k:
                    if not result or temp < result:
                        result = temp

            # if we find result of k size, then it's smallest , no need to move to k++
            if result:
                return result
        return ""


Approach1 = Solution


# Approach-2 (Sliding Window)
# T.C : O(n^2)
# S.C : O(1)
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        i = 0
        ones = 0  # number of '1's in window [i, j]
        result = ""

        for j in range(n):
            if s[j] == '1':
                ones += 1

            # remove extra 1's, then trim leading 0's
            # (i < n guard added: C++ reads the '\0' terminator when i == n; Python would raise IndexError)
            while i < n and (ones > k or s[i] == '0'):
                if s[i] == '1':
                    ones -= 1
                i += 1

            if ones == k:
                temp = s[i:j + 1]
                if (not result
                        or j - i + 1 < len(result)
                        or (j - i + 1 == len(result) and temp < result)):

                    result = temp

        return result


Approach2 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2):
        assert S().shortestBeautifulSubstring("100011001", 3) == "11001"
        assert S().shortestBeautifulSubstring("1011", 2) == "11"
        assert S().shortestBeautifulSubstring("000", 1) == ""
    print("All tests passed")
