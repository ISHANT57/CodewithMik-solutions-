# MY YOUTUBE VIDEO ON THIS Qn   : https://www.youtube.com/watch?v=s4nRUC1SDDA
# Company Tags                  : Will update soon
# Leetcode Link                 : https://leetcode.com/problems/take-k-of-each-character-from-left-and-right

# Approach-1 (Brute Force - Recursion)
# T.C : O(2^n)
# S.C : O(1) (But recursion stack space we are taking = O(n) in worst case i.e. depth of recursion will be equal to length of string)
from typing import List


class Solution:

    def __init__(self):
        self.result = 2**31 - 1  # INT_MAX

    def solve(self, s: str, k: int, i: int, j: int, minutes: int, freq: List[int]) -> None:
        if freq[0] >= k and freq[1] >= k and freq[2] >= k:
            self.result = min(self.result, minutes)
            return
        if i > j:  # all characters visited
            return

        # Option-1 : Delete from left
        tempFreqLeft = list(freq)
        tempFreqLeft[ord(s[i]) - ord('a')] += 1
        self.solve(s, k, i + 1, j, minutes + 1, tempFreqLeft)

        # De;ete from right
        tempFreqRight = list(freq)
        tempFreqRight[ord(s[j]) - ord('a')] += 1
        self.solve(s, k, i, j - 1, minutes + 1, tempFreqRight)

    def takeCharacters(self, s: str, k: int) -> int:
        freq = [0] * 3  # a, b, c
        i = 0
        j = len(s) - 1
        minutes = 0
        self.solve(s, k, i, j, minutes, freq)

        return -1 if self.result == 2**31 - 1 else self.result


Approach1 = Solution


# Approach-2 (Sliding Window)
# T.C : O(n)
# S.C : O(1)
class Solution:
    # Khandani sliding window
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)

        count_a = 0  # delete
        count_b = 0  # delete
        count_c = 0  # delete
        for ch in s:
            if ch == 'a':
                count_a += 1
            elif ch == 'b':
                count_b += 1
            else:
                count_c += 1

        if count_a < k or count_b < k or count_c < k:
            return -1  # not possible to delete k characters

        i = 0
        j = 0
        notDeletedWindowSize = 0

        while j < n:
            if s[j] == 'a':
                count_a -= 1
            elif s[j] == 'b':
                count_b -= 1
            elif s[j] == 'c':
                count_c -= 1

            # if deletion count of any character becomes less than k, then shrink the window and bring them back
            while i <= j and (count_a < k or count_b < k or count_c < k):
                # ith pointer move to left
                if s[i] == 'a':
                    count_a += 1
                elif s[i] == 'b':
                    count_b += 1
                else:
                    count_c += 1
                i += 1

            notDeletedWindowSize = max(notDeletedWindowSize, j - i + 1)
            j += 1

        return n - notDeletedWindowSize  # minutes


Approach2 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2):
        assert S().takeCharacters("aabaaaacaabc", 2) == 8
        assert S().takeCharacters("a", 1) == -1
    print("All tests passed")
