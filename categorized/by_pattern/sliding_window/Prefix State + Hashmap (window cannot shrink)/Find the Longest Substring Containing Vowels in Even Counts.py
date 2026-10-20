# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=6Xf5LfM-ciI
# Company Tags                : Yogiyo (Food delivering app)
# Leetcode Link               : https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

# NOTE : Why sliding window is not a feasible for this ?
# Example : "leetcodeisgreat"
# When i is at index 1 and j is at index 5, you don't know if we should move i to right or ignore jth character.

from typing import List


# Approach-1 (Using map to store states)
# T.C : O(n)
# S.C : O(1)
# (Original C++ used an undeclared name `stateMap` in the lookup; it is the same map `mp`.)
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mp = {}  # unordered_map<string, int>

        # Initialize an array to track the count of each vowel
        vowelCount = [0] * 5  # Count of 'a', 'e', 'i', 'o', 'u'

        currentState = "00000"  # Initial state where all vowels have even counts
        mp[currentState] = -1

        maxLength = 0

        for i in range(len(s)):
            # Update count for the vowel encountered
            if s[i] == 'a':
                vowelCount[0] = (vowelCount[0] + 1) % 2
            elif s[i] == 'e':
                vowelCount[1] = (vowelCount[1] + 1) % 2
            elif s[i] == 'i':
                vowelCount[2] = (vowelCount[2] + 1) % 2
            elif s[i] == 'o':
                vowelCount[3] = (vowelCount[3] + 1) % 2
            elif s[i] == 'u':
                vowelCount[4] = (vowelCount[4] + 1) % 2

            # Create a string representing the current parity state of vowels
            currentState = ""
            for j in range(5):
                currentState += str(vowelCount[j])

            # Check if we've seen this state before
            if currentState in mp:
                # Calculate the length of the substring
                maxLength = max(maxLength, i - mp[currentState])
            else:
                # Store the first occurrence of this state
                mp[currentState] = i

        return maxLength


Approach1 = Solution


# Approach-2 (Using map to store states and using XOR to make states)
# T.C : O(n)
# S.C ; O(1)
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Map to store the first occurrence of a state of vowel parities
        mp = {}

        # Initialize an array to track the parity of each vowel
        state = [0] * 5  # [a, e, i, o, u] initialized to 0 (even count)

        currentState = "00000"  # Start with all vowels having an even count
        mp[currentState] = -1

        maxLength = 0

        for i in range(len(s)):
            # Update state based on the vowel encountered
            if s[i] == 'a':
                state[0] ^= 1  # Flip between even/odd for 'a'
            elif s[i] == 'e':
                state[1] ^= 1  # Flip for 'e'
            elif s[i] == 'i':
                state[2] ^= 1  # Flip for 'i'
            elif s[i] == 'o':
                state[3] ^= 1  # Flip for 'o'
            elif s[i] == 'u':
                state[4] ^= 1  # Flip for 'u'

            # Create a string representation of the current state
            currentState = ""
            for j in range(5):
                currentState += str(state[j])

            # Check if we've seen this state before
            if currentState in mp:
                # Calculate the length of the substring
                maxLength = max(maxLength, i - mp[currentState])
            else:
                # Store the first occurrence of this state
                mp[currentState] = i

        return maxLength


Approach2 = Solution


# Approach-3 (using Mask and Xor property
# T.C : O(n)
# S.C : O(32) ~ O(1) - Maximum 2^5 states possible
# This belongs to Bit_Magic repository as well (You will find the link to this question in Bit_magic repository as well)
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mp = {}
        mask = 0
        mp[mask] = -1
        maxL = 0
        for i in range(len(s)):
            val = 0
            if s[i] == 'a':
                val = (1 << 0)
            elif s[i] == 'e':
                val = (1 << 1)
            elif s[i] == 'i':
                val = (1 << 2)
            elif s[i] == 'o':
                val = (1 << 3)
            elif s[i] == 'u':
                val = (1 << 4)

            mask = mask ^ val  # xor nikala

            if mask not in mp:  # agar past me nahi dekha to map me daaldo
                mp[mask] = i

            maxL = max(maxL, i - mp[mask])  # maxL nikaal lo
        return maxL


Approach3 = Solution


if __name__ == "__main__":
    for A in (Approach1, Approach2, Approach3):
        assert A().findTheLongestSubstring("eleetminicoworoep") == 13
        assert A().findTheLongestSubstring("leetcodeisgreat") == 5
        assert A().findTheLongestSubstring("bcbcbc") == 6
    print("ok")
