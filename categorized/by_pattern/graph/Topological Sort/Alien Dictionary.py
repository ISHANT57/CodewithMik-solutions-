#     Company Tags  : Airbnb, Amazon, Apple, Bloomberg, Cohesity, Facebook, Flipkart, Google, Microsoft, Oracle, Pinterest,
#                     Pocket, Gems, Snapchat, Square, Twitter, Uber, VMware, .Star
#     Leetcode Link : https://leetcode.com/problems/alien-dictionary/
#
#     It's a Premium Qn, so the Description has been added below:
#      There is a new alien language which uses the latin alphabet.
#      However, the order among letters are unknown to you.
#
#      You receive a list of words from the dictionary, where words are sorted lexicographically
#      by the rules of this new language.
#
#      Derive the order of letters in this language.
#
#      Example - 1
#      Input  : [ "wrt", "wrf", "er", "ett", "rftt" ]
#
#      Output : "wertf".
#
#     Exmaple - 2
#     Input : [ "z", "x", "z" ]
#
#      Output: ""
#
#      Explanation: The order is invalid, so return "".
#
#
#      Note:
#      You may assume all letters are in lowercase.
#      If the order is invalid, return an empty string.
#      There may be multiple valid order of letters, return any one of them is fine.

#     This is a popular question which tests your knowledge on "Topological Sorting".
#     Why "Topological Sorting" ?
#     Whenever any question deals with ordering (which comes first) and there are nodes, then do think about Topological Sorting. It may be a hint.

from collections import deque
from typing import Dict, List, Set


# Approach-1 (Topological Sorting : BFS(Kahn's Algorithm)
class Solution:
    def __init__(self):
        self.result = ""

    # unordered_map<char, set<char>> -> dict of char -> set (C++ set iterates in sorted order, so we use sorted() when iterating)
    def buildGraph(self, adj: Dict[str, Set[str]], words: List[str], indegree: List[int]):
        n = len(words)

        # First insert all unique characters
        for word in words:
            for ch in word:
                adj[ch] = set()

        # Connect letters (find dependencies)
        for i in range(1, n):
            first = words[i - 1]
            second = words[i]

            l = min(len(first), len(second))
            for j in range(l):
                u = first[j]
                v = second[j]
                if u != v:
                    indegree[ord(v) - ord('a')] += 1
                    adj[u].add(v)
                    break

                # if second is a prefix of first, we have wrong order
                if j + 1 == l and len(first) > len(second):
                    adj.clear()
                    return

    def kahnsAlgo(self, adj: Dict[str, Set[str]], V: int, indegree: List[int]):
        que = deque()
        for i in range(26):
            ch = chr(i + ord('a'))
            if indegree[i] == 0 and ch in adj:
                que.append(ch)

        count = len(que)
        while que:
            curr = que.popleft()
            self.result += curr
            for x in sorted(adj[curr]):
                indegree[ord(x) - ord('a')] -= 1
                if indegree[ord(x) - ord('a')] == 0:
                    count += 1
                    que.append(x)

        if count != V:
            self.result = ""

    def alienOrder(self, words: List[str]) -> str:
        adj = {}
        indegree = [0] * 26

        self.buildGraph(adj, words, indegree)
        V = len(adj)
        self.kahnsAlgo(adj, V, indegree)

        return self.result


Approach1 = Solution

# Approach-2 (DFS - Coming Soon)  (not implemented in the source)

if __name__ == "__main__":
    assert Solution().alienOrder(["wrt", "wrf", "er", "ett", "rftt"]) == "wertf"
    assert Solution().alienOrder(["z", "x", "z"]) == ""
    assert Solution().alienOrder(["abc", "ab"]) == ""
    print("ok")
