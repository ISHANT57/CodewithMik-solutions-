# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=c11UizbJYZU
# Company Tags                : Amazon (many times), Meta
# Leetcode Link               : https://leetcode.com/problems/partition-labels/

from typing import List


# Approach-1 (basic approach that we should come up with in first call)
# T.C : O(n)
# S.C : O(1)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)

        result = []

        # last occurance of each character
        # unordered_map<char, int> mp;
        mp = [-1] * 26
        for i in range(n):
            idx = ord(s[i]) - ord('a')
            mp[idx] = i

        i = 0
        while i < n:
            end = mp[ord(s[i]) - ord('a')]

            j = i
            while j < end:
                end = max(end, mp[ord(s[j]) - ord('a')])
                j += 1
            result.append(j - i + 1)
            i = j + 1

        return result


Approach1 = Solution


# Approach-2 (Clean code)
# T.C : O(n)
# S.C : O(1)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)

        result = []

        # last occurance of each character
        # unordered_map<char, int> mp;
        mp = [-1] * 26
        for i in range(n):
            idx = ord(s[i]) - ord('a')
            mp[idx] = i

        i = 0
        start = 0
        end = 0
        while i < n:
            end = max(end, mp[ord(s[i]) - ord('a')])
            if i == end:
                result.append(end - start + 1)
                start = end + 1
            i += 1

        return result


Approach2 = Solution


if __name__ == "__main__":
    for A in (Approach1, Approach2):
        assert A().partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
        assert A().partitionLabels("eccbbbbdec") == [10]
    print("ok")
