# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=Uu03ktYBWMY
# Company Tags                : <Soon>
# Leetcode Link               : https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

# Time Complexity -
# We fill the itemGraph and groupGraphs by traversing on each item and beforeItems causing O(n^2) in worst case.
# After that, Since we call Topological Sort for :
# 1) itemGraph - O(n + edges)
# 2) Group Graph - O(m + edges)
#
# Then, we run for loop ok itemOrder - O(n)
# Then we run for loop on groupOrder - O(m)
# Then at the end we make result - O(n)
# After summing up all, the biggest term is O(n^2)
# Hence worst case TC = O(n^2) Hope this helps.
# I will definitely cover TC in my videos further Thanks a lot (heart)

# **************************************** C++ -> Python ****************************************
# Using Topological sort of items and groups
from typing import List, Dict
from collections import deque, defaultdict


class Solution:
    def topoSort(self, adj: Dict[int, List[int]], indegree: List[int]) -> List[int]:
        que = deque()

        # 1. Fill que, indegree with 0
        for i in range(len(adj)):
            if indegree[i] == 0:
                que.append(i)

        # 2. Simple BFS
        result = []
        while que:
            u = que.popleft()
            result.append(u)

            for v in adj[u]:
                indegree[v] -= 1

                if indegree[v] == 0:
                    que.append(v)

        return result if len(result) == len(adj) else []

    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        # Step-1 (assign group numbers to all)
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        # Step-2 (Make itemGraph and itemIndegree) - For Topological Sorting
        itemGraph = {}  # unordered_map<int, vector<int>>
        itemIndegree = [0] * n
        for i in range(n):
            itemGraph[i] = []

        # Step-3 (Make groupGraph and groupIndegree) - For Topological Sorting
        groupGraph = {}  # unordered_map<int, vector<int>>
        groupIndegree = [0] * m
        for i in range(m):
            groupGraph[i] = []

        # Step-4 (Fill itemGraph, itemIndegree, groupGraph, groupIndegree)

        for i in range(n):

            for prev in beforeItems[i]:

                itemGraph[prev].append(i)
                itemIndegree[i] += 1

                if group[i] != group[prev]:
                    prevItemGroup = group[prev]
                    currItemGroup = group[i]

                    groupGraph[prevItemGroup].append(currItemGroup)
                    groupIndegree[currItemGroup] += 1

        # Step-5 (Call TopoSort for both Graphs)
        itemOrder = self.topoSort(itemGraph, itemIndegree)
        groupOrder = self.topoSort(groupGraph, groupIndegree)

        if not itemOrder or not groupOrder:
            return []

        groupToItemsInOrder = defaultdict(list)  # unordered_map<int, vector<int>>
        for item in itemOrder:
            itemGroup = group[item]
            groupToItemsInOrder[itemGroup].append(item)

        result = []
        for grp in groupOrder:  # (named 'group' in C++, renamed to avoid shadowing the parameter)
            result.extend(groupToItemsInOrder[grp])

        return result


Approach1 = Solution

if __name__ == "__main__":
    n, m = 8, 2
    group = [-1, -1, 1, 0, 0, 1, 0, -1]
    before = [[], [6], [5], [6], [3, 6], [], [], []]
    res = Solution().sortItems(n, m, list(group), [list(b) for b in before])
    assert sorted(res) == list(range(n))
    pos = {x: i for i, x in enumerate(res)}
    for i in range(n):
        for p in before[i]:
            assert pos[p] < pos[i]
    # items of same group must be contiguous
    gs = [group[x] if group[x] != -1 else ("s", x) for x in res]
    seen = set()
    for i, g in enumerate(gs):
        if i and gs[i - 1] != g:
            assert g not in seen
        seen.add(g)
    assert Solution().sortItems(8, 2, list(group), [[], [6], [5], [6], [3], [], [4], []]) == []
    print("ok", res)
