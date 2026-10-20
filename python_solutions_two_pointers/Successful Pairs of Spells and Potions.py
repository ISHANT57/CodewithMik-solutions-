# MY YOUTUBE VIDEO ON THIS Qn : <soon>
# Company Tags                : MICROSOFT
# Leetcode Link               : https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

from typing import List


# Approach-1 : Using lower_bound STL
# In my Binary Search sub-repo - https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Arrays/Binary%20Search/Successful%20Pairs%20of%20Spells%20and%20Potions.cpp
# (Code lives in another file, not in this source)


# Approach-2 : Using self written Binary Search for lower bound
# In my Binary Search sub-repo - https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Arrays/Binary%20Search/Successful%20Pairs%20of%20Spells%20and%20Potions.cpp
# (Code lives in another file, not in this source)


# Approach-3 (Using 2 pointers)
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        sortedSpells = []
        for i in range(len(spells)):
            sortedSpells.append((spells[i], i))

        # Sort the 'spells with index' and 'potions' array in increasing order.
        sortedSpells.sort()
        potions.sort()

        answer = [0] * len(spells)
        m = len(potions)
        potionIndex = m - 1

        # For each 'spell' find the respective 'minPotion' index.
        for spell, index in sortedSpells:

            while potionIndex >= 0 and spell * potions[potionIndex] >= success:
                potionIndex -= 1
            answer[index] = m - (potionIndex + 1)

        return answer


Approach3 = Solution


if __name__ == "__main__":
    assert Solution().successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7) == [4, 0, 3]
    assert Solution().successfulPairs([3, 1, 2], [8, 5, 8], 16) == [2, 0, 2]
    print("ok")
