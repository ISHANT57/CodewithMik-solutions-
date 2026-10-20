# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=z7mPg_xT5xk
# Company Tags                : Google, Facebook, Amazon
# Leetcode Qn Link            : https://leetcode.com/problems/clone-graph/

from typing import Optional, List
from collections import deque


# Definition for a Node (provided by LeetCode).
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# Approach-1 (DFS) Using vector as map
class Solution:

    def DFS(self, node: 'Node', clone_node: 'Node', visited: list) -> None:
        visited[node.val] = clone_node

        for x in node.neighbors:
            if visited[x.val] is None:
                clone = Node(x.val)
                clone_node.neighbors.append(clone)
                self.DFS(x, clone, visited)
            else:
                clone_node.neighbors.append(visited[x.val])

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # cloned the given node
        clone_node = Node(node.val)

        # Now, clone its neighbours and recursively their neighbours
        # But if a node reappears, then we need to access that cloned node
        # So, store them in a vector (list) to access

        visited = [None] * 101  # Using contraints given
        # We could use map also if constraints are not clear (i.e. unordered_map<Node*, Node*> visited;)
        visited[node.val] = clone_node

        self.DFS(node, clone_node, visited)

        return clone_node


Approach1 = Solution


# Approach-2 DFS (Using unordered_map)
class Solution:

    def __init__(self):
        self.mp = {}  # unordered_map<Node*, Node*> -> dict keyed by node object

    def DFS(self, node: 'Node', clone_node: 'Node') -> None:

        for n in node.neighbors:

            if n not in self.mp:

                clone = Node(n.val)
                self.mp[n] = clone
                clone_node.neighbors.append(clone)

                self.DFS(n, clone)

            else:

                clone_node.neighbors.append(self.mp[n])

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        self.mp.clear()

        # cloned the given node
        clone_node = Node(node.val)

        # Now, cloe its neighbours and recursively their newighbours
        # But if a node reappears, then we need to access that cloned node
        # So, store them in a map <Node*, Node*>

        self.mp[node] = clone_node

        self.DFS(node, clone_node)

        return clone_node


Approach2 = Solution


# Approach-3 (BFS) - Using vector as map
class Solution:
    def BFS(self, que: deque, visited: list) -> None:
        while que:
            node = que.popleft()

            # go for neighbors. Note that we are filling neighbors of "node"
            # if we find a neighbor, we need to push it's clone to the corresponding
            # cloned node's neighbors only(i.e. inside visited[x.val].neighbors). See below for clarity
            for x in node.neighbors:
                if visited[x.val] is None:
                    clone = Node(x.val)
                    visited[node.val].neighbors.append(clone)
                    # i.e. adding cloned neighbors to cloned node
                    # adding this new node to visited as well for future access
                    visited[x.val] = clone
                    que.append(x)
                else:
                    visited[node.val].neighbors.append(visited[x.val])
                    # i.e. adding cloned neighbors to cloned node

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clone_node = Node(node.val)

        # similar to what we did above in DFS
        visited = [None] * 101
        visited[node.val] = clone_node

        que = deque()
        que.append(node)

        self.BFS(que, visited)

        return clone_node


Approach3 = Solution


# Approach-4 BFS (Using unordered_map)
class Solution:

    def __init__(self):
        self.mp = {}  # unordered_map<Node*, Node*> -> dict keyed by node object

    def DFS(self, node: 'Node', clone_node: 'Node') -> None:

        for n in node.neighbors:

            if n not in self.mp:

                clone = Node(n.val)
                self.mp[n] = clone
                clone_node.neighbors.append(clone)

                self.DFS(n, clone)

            else:

                clone_node.neighbors.append(self.mp[n])

    def BFS(self, que: deque) -> None:

        while que:

            node = que.popleft()
            clone_node = self.mp[node]

            for n in node.neighbors:

                if n not in self.mp:

                    clone = Node(n.val)
                    self.mp[n] = clone
                    clone_node.neighbors.append(clone)

                    # self.DFS(n, clone)
                    que.append(n)

                else:

                    clone_node.neighbors.append(self.mp[n])

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        self.mp.clear()

        # cloned the given node
        clone_node = Node(node.val)

        # Now, cloe its neighbours and recursively their newighbours
        # But if a node reappears, then we need to access that cloned node
        # So, store them in a map <Node*, Node*>

        self.mp[node] = clone_node

        que = deque()
        que.append(node)
        self.BFS(que)

        return clone_node


Approach4 = Solution


if __name__ == "__main__":
    def build(adjList):
        nodes = [Node(i + 1) for i in range(len(adjList))]
        for i, nb in enumerate(adjList):
            nodes[i].neighbors = [nodes[j - 1] for j in nb]
        return nodes[0]

    def serialize(node):
        seen, order, stack = {}, [], [node]
        seen[node] = True
        while stack:
            cur = stack.pop()
            order.append(cur)
            for nb in cur.neighbors:
                if nb not in seen:
                    seen[nb] = True
                    stack.append(nb)
        order.sort(key=lambda x: x.val)
        return [[nb.val for nb in n.neighbors] for n in order], order

    adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
    for A in (Approach1, Approach2, Approach3, Approach4):
        orig = build(adjList)
        clone = A().cloneGraph(orig)
        ser, nodes = serialize(clone)
        _, onodes = serialize(orig)
        assert ser == adjList
        assert all(a is not b for a, b in zip(nodes, onodes))
        assert A().cloneGraph(None) is None
    print("ok")
