from collections import defaultdict

#     Company Tags : Google, Amazon, SAP Labs
#     Qn Link      : https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1#
#
#     Alternative question (Asked in an interview) :
#     John goes to mall with his mom. He sees that there many toys. He insists his mom to buy him toys.
#     His mom told him ok fine, you can pick the toys but in two conditions :
#     1) You can pick toys in line (you can't skip any toy in between) (Hint: She is asking for a subarray)
#     2) You can have only two types of toys.
#
#     Find maximum number of toys that can be picked up by John.
#
#     So this question is nothing but : "Find the length of longest subarray/substring having k unique characters"


# It's a Classical sliding window problem
# We traverse the string two times with i and j pointer in worst case. Time : o(n+n) = O(n)
class Solution:
    def longestKSubstr(self, s: str, k: int) -> int:
        n = len(s)
        i = 0
        j = 0
        mp = defaultdict(int)  # unordered_map<char, int>
        maxLen = -1
        while j < n:
            mp[s[j]] += 1

            if len(mp) == k:
                maxLen = max(maxLen, j - i + 1)
            elif len(mp) > k:
                while len(mp) > k:
                    mp[s[i]] -= 1
                    if mp[s[i]] <= 0:
                        del mp[s[i]]
                    i += 1
            j += 1
        return maxLen


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().longestKSubstr("aabacbebebe", 3) == 7
    assert Solution().longestKSubstr("aaaa", 2) == -1
    print("All tests passed")
