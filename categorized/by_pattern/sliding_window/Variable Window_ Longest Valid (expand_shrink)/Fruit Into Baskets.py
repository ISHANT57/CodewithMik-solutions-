from typing import List
from collections import defaultdict

#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=QBi5_btsse4
#     Company Tag                 : will update later
#     Leetcode Link               : https://leetcode.com/problems/fruit-into-baskets/description/


# *************************************************************** C++ *************************************************
# Approach (Sliding Window using map)
# T.C : O(n)
# S.C : O(n)
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)

        mp = defaultdict(int)  # unordered_map<int, int>

        i = 0
        j = 0
        count = 0

        while j < n:
            mp[fruits[j]] += 1

            if len(mp) <= 2:
                count = max(count, j - i + 1)
            else:
                mp[fruits[i]] -= 1
                if mp[fruits[i]] == 0:
                    del mp[fruits[i]]
                i += 1

            j += 1
        return count


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().totalFruit([1, 2, 1]) == 3
    assert Solution().totalFruit([0, 1, 2, 2]) == 3
    assert Solution().totalFruit([1, 2, 3, 2, 2]) == 4
    print("All tests passed")
