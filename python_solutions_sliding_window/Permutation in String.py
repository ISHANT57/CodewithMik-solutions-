# MY YOUTUBE VIDEO ON THIS QN : https://www.youtube.com/watch?v=iTwwvsyUsi4
# Company Tags                : Microsoft, Amazon
# Leetcode Link               : https://leetcode.com/problems/permutation-in-string

# Approach-1 (Brute Force) - TLE
# T.C : O(n! * m)
# S.C : O(n)
from typing import List


class Solution:
    def __init__(self):
        self.n = 0
        self.result = False

    # s1 is a list of chars here so that it can be swapped in place (like C++ string&)
    def solve(self, idx: int, s1: List[str], s2: str) -> None:
        if idx == self.n:
            if "".join(s1) in s2:
                self.result = True
            return

        for i in range(idx, self.n):
            s1[i], s1[idx] = s1[idx], s1[i]

            self.solve(idx + 1, s1, s2)

            s1[i], s1[idx] = s1[idx], s1[i]

            # Early exit if a permutation has been found in s2
            if self.result == True:
                return

    def checkInclusion(self, s1: str, s2: str) -> bool:
        self.n = len(s1)
        self.result = False  # Reset result for each call

        self.solve(0, list(s1), s2)

        return self.result  # Return whether a permutation of s1 is found in s2


Approach1 = Solution


# Approach-2 (Using Sorting and Comparing) - ACCEPTED
# T.C : O((m-n) * nlogn)
# S.C : O(n)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        # If s1 is longer than s2, it cannot be a substring
        if n > m:
            return False

        # Sort the string s1
        sorted_s1 = "".join(sorted(s1))

        # Iterate over each substring of s2 of length equal to s1
        for i in range(0, m - n + 1):
            # Extract a substring of length n from s2 starting at index i
            temp = s2[i:i + n]

            # Sort the substring
            temp = "".join(sorted(temp))

            # If the sorted substring matches the sorted s1, return true
            if temp == sorted_s1:
                return True

        # No permutation found in s2
        return False


Approach2 = Solution


# Approach-3 (Sliding Window) - ACCEPTED
# T.C : O(m+n)
# S.C : O(26)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        # If s1 is larger than s2, no permutation can exist
        if n > m:
            return False

        # Frequency vectors for s1 and the current window in s2
        s1_freq = [0] * 26
        s2_freq = [0] * 26

        # Fill frequency of characters in s1
        for i in range(n):
            s1_freq[ord(s1[i]) - ord('a')] += 1

        # Slide the window over s2
        i = 0  # left index of the sliding window
        j = 0  # right index of the sliding window
        while j < m:
            # Include a new character from the right end of the window
            s2_freq[ord(s2[j]) - ord('a')] += 1

            # Check if the current window size matches the size of s1
            if j - i + 1 > n:
                # If we have passed the size of s1, we need to remove the leftmost character
                s2_freq[ord(s2[i]) - ord('a')] -= 1
                i += 1

            # Check if the current window's frequency matches s1's frequency
            if s1_freq == s2_freq:
                return True

            j += 1

        # No matching window found
        return False


Approach3 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2, Approach3):
        assert S().checkInclusion("ab", "eidbaooo") is True
        assert S().checkInclusion("ab", "eidboaoo") is False
    print("All tests passed")
