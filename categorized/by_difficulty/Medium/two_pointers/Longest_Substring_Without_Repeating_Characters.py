from typing import List

# Company Tags  : Morgan Stanley, Amazon, Microsoft, Housing.com, Datazip Online Assessment (July, 2026)
# Leetcode Link : https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Approach-1 (Using set data structure and two pointer technique)
# Time : O(2*n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()  # unordered_set<char> -> set
        l = 0

        n = len(s)
        i = 0
        j = 0
        while j < n:
            if s[j] not in st:
                st.add(s[j])
                l = max(l, len(st))
                j += 1
            else:
                st.remove(s[i])
                i += 1
                #
                #     Example : "a b c d e a a"
                #     When you are at 5th index, you notice that you saw 'a' somewhere before, you delete it from set
                #     Now, you add this 'a' (5th index) in the set and move ahead at 6th index.
                #     Now, you see that 'a' (6th index) is somewhere behind because it's in the set.
                #     But you keep deleting from set until you delete this 'a' (5th index) from the set.
                #     So, effectively you are iterating array 2 times in worst case. So, time = O(2*n)
                #
        return l


Approach1 = Solution


# Approach-2 (Using map data strcture and two pointer technique)
# Time : O(n)
#
#     Instead of deleting character one by one, we can directly jump 'i' just after the last appearance of a character.
#     We will use to store indices of character. So, in that way we don't have to move 'i' one by one.
#     Now one thing to note,
#     Example : "a a b a a b z b b"
#     When you reach at index 4 ('a'), you move i = mp['a'] + 1. i.e. 'i' is now 4
#     Now, When you are at 5th index ('b'), you notice that you have '(b, 2)' in map. So, you make i = map['b'] + 1;
#     i.e. i becomes 3 but did you notice you had made i = 4 above. This is an issue.
#     So, we do this : i = max(i, mp[ch]+1); //which ever is larger we make that jump for 'i'
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0

        i, j = 0, 0
        mp = {}  # unordered_map<char, int> -> dict

        while j < n:
            ch = s[j]
            if ch not in mp:
                # If not in map, update map and calculate length
                mp[ch] = j
                res = max(res, j - i + 1)
            else:
                # if already present in map, make proper i jump and then calculate length
                i = max(i, mp[ch] + 1)
                mp[ch] = j  # Don't forget to update new index of ch
                res = max(res, j - i + 1)
            j += 1

        return res


Approach2 = Solution


# Approach-3 (Just simplifying Approach-2. Notice some statements are common in if and else block. Take them outside
# Time : O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0

        i, j = 0, 0
        mp = {}

        while j < n:
            ch = s[j]
            if ch in mp:
                i = max(i, mp[ch] + 1)
            mp[ch] = j
            res = max(res, j - i + 1)
            j += 1

        return res


Approach3 = Solution

if __name__ == "__main__":
    for S in (Approach1, Approach2, Approach3):
        assert S().lengthOfLongestSubstring("abcabcbb") == 3
        assert S().lengthOfLongestSubstring("bbbbb") == 1
        assert S().lengthOfLongestSubstring("pwwkew") == 3
        assert S().lengthOfLongestSubstring("") == 0
    print("ok")
