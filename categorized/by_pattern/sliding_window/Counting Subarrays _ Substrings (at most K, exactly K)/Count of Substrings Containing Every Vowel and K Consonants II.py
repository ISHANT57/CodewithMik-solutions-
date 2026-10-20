# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=8FP1kkYf2U4
# Company Tags                : will update soon
# Leetcode Link               : https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii

from typing import List
from collections import defaultdict


# Approach (Sliding Window Khandani Template)
# T.C : O(2*n) ~ O(n)
# S.C : O(n)
class Solution:
    def isVowel(self, ch: str) -> bool:
        return ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'

    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)

        mp = defaultdict(int)  # to keep count of vowels in a current window
        # S.C : O(5) constant

        # Preprocessing to be able to find index of just next consonant
        nextCons = [0] * n  # S.C : O(n)
        lastConsIdx = n
        # T.C : O(n)
        for i in range(n - 1, -1, -1):
            nextCons[i] = lastConsIdx
            if not self.isVowel(word[i]):  # consonant
                lastConsIdx = i

        i = 0
        j = 0
        count = 0
        cons = 0
        # T.C : O(2*n) ~ O(n)
        while j < n:
            ch = word[j]
            if self.isVowel(ch):
                mp[ch] += 1
            else:
                cons += 1

            # cons must be always == k
            while cons > k:
                ch = word[i]
                if self.isVowel(ch):
                    mp[ch] -= 1
                    if mp[ch] == 0:
                        del mp[ch]
                else:
                    cons -= 1
                i += 1

            while i < n and len(mp) == 5 and cons == k:  # valid window
                idx = nextCons[j]  # it will tell me the next consonant after jth index
                count += idx - j  # most important part
                ch = word[i]
                if self.isVowel(ch):
                    mp[ch] -= 1
                    if mp[ch] == 0:
                        del mp[ch]
                else:
                    cons -= 1
                i += 1

            j += 1

        return count


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().countOfSubstrings("aeioqq", 1) == 0
    assert Solution().countOfSubstrings("aeiou", 0) == 1
    assert Solution().countOfSubstrings("ieaouqqieaouqq", 1) == 3
    print("ok")
