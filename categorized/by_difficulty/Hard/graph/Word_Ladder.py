# Company Tags  : Microsoft, Amazon
# Leetcode Link : https://leetcode.com/problems/word-ladder/
from typing import List, Dict
from collections import deque


class Solution:
    def pushAdjacentWords(self, mp: Dict[str, bool], que: deque, curr: str) -> None:
        n = len(curr)
        curr = list(curr)  # strings are immutable in Python
        for i in range(n):
            temp = curr[i]
            # check for all letters at index i
            for o in range(ord('a'), ord('z') + 1):
                curr[i] = chr(o)
                s = "".join(curr)
                if s in mp and mp[s] == False:  # not visited
                    mp[s] = True  # mark visited
                    que.append(s)
            curr[i] = temp

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if len(wordList) == 0:
            return 0
        # First add words in a map for easy access
        mp = {}

        for word in wordList:
            mp[word] = False  # means this word is not visited yet

        # The endWord should be in the list
        if endWord not in mp:
            return 0

        level = 1  # beginWord is at level 1

        que = deque()
        que.append(beginWord)

        # Just do a BFS traversal
        while que:
            n = len(que)
            while n > 0:
                n -= 1
                curr = que.popleft()
                if curr == endWord:
                    return level
                self.pushAdjacentWords(mp, que, curr)
            level += 1

        # we never found the end word
        return 0


Approach1 = Solution

if __name__ == "__main__":
    assert Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
    assert Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    print("ok")
