# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=FfA-2CrWVJw
# Company Tags                : META
# Leetcode Link               : https://leetcode.com/problems/validate-binary-tree-nodes/description/
#
# Find another Binary Tree Solution - https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Tree/Validate%20Binary%20Tree%20Nodes.cpp

from typing import List


########################################## Python (converted from C++) ##########################################
# Approach-1 (Using DSU)
class Solution:
    def __init__(self):
        self.parent = []
        self.components = 0

    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def Union(self, par: int, child: int) -> bool:
        child_ka_parent = self.find(child)

        # child_ka_parent != child --> Child had already some other parent
        if child_ka_parent != child:
            return False

        parent_ka_parent = self.find(par)
        # parent_ka_parent == child_ka_parent ---> Parallel edge (It means, already they were connected by another edge)
        if parent_ka_parent == child_ka_parent:
            return False

        self.parent[child] = par
        self.components -= 1
        return True

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        self.components = n
        self.parent = [0] * n
        for i in range(n):
            self.parent[i] = i

        for i in range(n):
            if leftChild[i] >= 0 and not self.Union(i, leftChild[i]):
                return False
            if rightChild[i] >= 0 and not self.Union(i, rightChild[i]):
                return False

        return self.components == 1


Approach1 = Solution

# Approach-2 (Using simple BFS or DFS and Binary Tree Property)
# Find it in my "Binary Tree" repo - https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Tree/Validate%20Binary%20Tree%20Nodes.cpp
# (Not included in the source file; only a link to another repo.)


if __name__ == "__main__":
    assert Solution().validateBinaryTreeNodes(4, [1, -1, 3, -1], [2, -1, -1, -1]) is True
    assert Solution().validateBinaryTreeNodes(4, [1, -1, 3, -1], [2, 3, -1, -1]) is False
    assert Solution().validateBinaryTreeNodes(2, [1, 0], [-1, -1]) is False
    print("ok")
