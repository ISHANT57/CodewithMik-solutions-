# MY YOUTUBE VIDEO ON THIS Qn : <coming soon>
# Leetcode Link               : https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# Company Tags                : Google

# Approach-1 (Without Sliding Window : Brute Force)
from typing import List


class Solution:
    def __init__(self):
        self.mp = {}  # unordered_map<string, int>
        self.totalWordsCount = 0
        self.substringSize = 0
        self.wordLength = 0

    def check(self, index: int, s: str) -> bool:
        temp = dict(self.mp)

        wordsSeen = 0

        for i in range(index, index + self.substringSize, self.wordLength):
            substring = s[i:i + self.wordLength]

            if substring in temp and temp[substring] > 0:
                temp[substring] -= 1
                wordsSeen += 1
            else:
                break

        return wordsSeen == self.totalWordsCount

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)

        self.wordLength = len(words[0])
        self.totalWordsCount = len(words)
        self.substringSize = self.totalWordsCount * self.wordLength

        for w in words:  # C++ loop variable shadowed s; renamed
            self.mp[w] = self.mp.get(w, 0) + 1

        result = []
        for i in range(0, n - self.substringSize + 1):
            if self.check(i, s):
                result.append(i)

        return result


Approach1 = Solution


# Approach-2 (Using Sliding Window)
# Coming soon   (not written by the instructor yet, so nothing to convert)


if __name__ == "__main__":
    assert Solution().findSubstring("barfoothefoobarman", ["foo", "bar"]) == [0, 9]
    assert Solution().findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]) == []
    assert Solution().findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]) == [6, 9, 12]
    print("All tests passed")
