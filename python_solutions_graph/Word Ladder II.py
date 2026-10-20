# Company Tags  : Amazon, Yelp
# Leetcode Link : https://leetcode.com/problems/word-ladder-ii/
#
# I will be back with more and simpler approaches soon

# Approach-1 (Using BFS and DFS) i.e. Using Concept of Word Ladder I
from typing import List, Dict, Set
from collections import deque, defaultdict


class Solution:
    def __init__(self):
        self.adj: Dict[str, Set[str]] = defaultdict(set)  # unordered_map<string, unordered_set<string>>
        self.result: List[List[str]] = []

    def pushAdjacentWords(self, mp: Dict[str, bool], visited: Dict[str, int], que: deque, curr: str) -> None:

        temp = list(curr)  # strings are immutable in Python
        for i in range(len(curr)):

            for o in range(ord('a'), ord('z') + 1):
                ch = chr(o)
                if temp[i] == ch:
                    continue

                temp[i] = ch
                t = "".join(temp)

                if t in mp and t != curr:
                    if t not in visited:
                        visited[t] = visited.setdefault(curr, 0) + 1  # C++ visited[curr] inserts 0 if absent
                        que.append(t)
                        self.adj[curr].add(t)
                    elif visited[t] == visited.setdefault(curr, 0) + 1:
                        self.adj[curr].add(t)

            temp[i] = curr[i]

    def DFS(self, currWord: str, endWord: str, path: List[str]) -> None:
        path.append(currWord)  # Push current word

        if currWord == endWord:
            self.result.append(list(path))
            path.pop()
            return

        for x in list(self.adj[currWord]):
            self.DFS(x, endWord, path)

        path.pop()  # Pop current word to Backtrack

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        self.adj.clear()
        self.result = []
        # First add words in a map for easy access
        mp = {}
        visited = {}
        for word in wordList:
            mp[word] = False  # means this word is not visited yet

        # The endWord should be in the list
        if endWord not in mp:
            return []

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
                    break
                self.pushAdjacentWords(mp, visited, que, curr)
            level += 1

        # So here we have sortest path till endWord = level
        # We now do a DFS on our special adjacency list
        # What's special ? the edge is always from a node to a node to next level
        path = []
        self.DFS(beginWord, endWord, path)
        return self.result


Approach1 = Solution

if __name__ == "__main__":
    r = Solution().findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
    assert sorted(r) == sorted([["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]), r
    assert Solution().findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == []
    print("ok")
