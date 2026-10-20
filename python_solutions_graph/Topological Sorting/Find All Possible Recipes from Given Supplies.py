#     Scroll below to see JAVA code also (Java sections skipped in this Python port)
#
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=4Tixc5mU-Pk
#     Company Tags                :
#     Leetcode Link               : https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies

from collections import defaultdict, deque
from typing import List


# ************************************ C++ (ported to Python) ************************************
# Approach-1 - Brute Force
# T.C : (n^2 * m)
# S.C : O(n+S)
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        result = []

        st = set(supplies)

        cooked = [False] * n

        count = n
        while count > 0:  # while(count--)
            count -= 1

            for j in range(n):
                if cooked[j]:
                    continue

                banpaega = True
                for k in range(len(ingredients[j])):
                    if ingredients[j][k] not in st:
                        banpaega = False
                        break

                if banpaega:
                    st.add(recipes[j])
                    result.append(recipes[j])
                    cooked[j] = True
        return result


Approach1 = Solution


# Approach-2 - Using Topological Sorting
# T.C : (n + m + S)
# S.C : O(n+S)
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        st = set(supplies)

        # adj
        adj = defaultdict(list)  # ing ---> recipe

        indegree = [0] * n
        for i in range(n):
            for ing in ingredients[i]:
                if ing not in st:
                    adj[ing].append(i)
                    indegree[i] += 1

        que = deque()
        for i in range(n):
            if indegree[i] == 0:
                que.append(i)

        result = []
        while que:
            i = que.popleft()
            recipe = recipes[i]
            result.append(recipe)

            for idx in adj[recipe]:
                indegree[idx] -= 1
                if indegree[idx] == 0:
                    que.append(idx)

        return result


Approach2 = Solution

if __name__ == "__main__":
    for A in (Approach1, Approach2):
        assert A().findAllRecipes(["bread"], [["yeast", "flour"]], ["yeast", "flour", "corn"]) == ["bread"]
        r = A().findAllRecipes(["bread", "sandwich"], [["yeast", "flour"], ["bread", "meat"]], ["yeast", "flour", "meat"])
        assert r == ["bread", "sandwich"], r
        r = A().findAllRecipes(["bread", "sandwich", "burger"],
                               [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]],
                               ["yeast", "flour", "meat"])
        assert sorted(r) == ["bread", "burger", "sandwich"]
    print("ok")
