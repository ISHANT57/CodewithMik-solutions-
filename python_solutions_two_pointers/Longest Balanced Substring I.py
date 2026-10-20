from typing import List

# Scroll below to see JAVA code also (Java section skipped in this Python port)
#
# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=tEUJZkSgxuA
# Company Tags                : Will update later
# Leetcode Link               : https://leetcode.com/problems/longest-balanced-substring-i


# *************************************************************** C++ *************************************************
# Approach (try all subarrays)
# T.C : O(n^2)
# S.C : O(1)
class Solution:

    def checkBalanced(self, freq: List[int]) -> bool:
        common = 0
        for i in range(26):
            if freq[i] == 0:
                continue
            if common == 0:
                common = freq[i]
            elif freq[i] != common:
                return False

        return True

    def longestBalanced(self, s: str) -> int:
        n = len(s)

        maxL = 0

        for i in range(n):
            freq = [0] * 26

            for j in range(i, n):
                freq[ord(s[j]) - ord('a')] += 1

                # i..j
                if self.checkBalanced(freq):
                    maxL = max(maxL, j - i + 1)

        return maxL


Approach1 = Solution

if __name__ == "__main__":
    assert Solution().longestBalanced("abbac") == 4
    assert Solution().longestBalanced("zzabccy") == 4
    assert Solution().longestBalanced("aba") == 2
    print("ok")
