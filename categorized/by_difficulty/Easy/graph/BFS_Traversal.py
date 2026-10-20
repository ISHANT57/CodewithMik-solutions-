# BFS Traversal (plain graph traversal demo, no LeetCode/GfG problem; source has no comment block)
# Original C++ was a standalone program with main(); ported as functions + __main__.

from collections import defaultdict, deque


# C++ map<int, vector<int>> -> defaultdict(list)
def addEdge(adj, u, v):
    adj[u].append(v)


def BFS(adj, V, start):
    visited = [0] * V
    que = deque()
    out = []

    que.append(start)
    # Mark a node visited as soon as it's pushed into queue
    visited[start] = 1
    while que:
        curr = que.popleft()
        print(curr, end=" ")
        out.append(curr)
        for i in adj[curr]:
            if visited[i] == 0:
                que.append(i)
                # Mark a node visited as soon as it's pushed into queue
                visited[i] = 1
    return out


if __name__ == "__main__":
    V = 4
    adj = defaultdict(list)

    addEdge(adj, 0, 1)
    addEdge(adj, 0, 2)
    addEdge(adj, 1, 2)
    addEdge(adj, 2, 0)
    addEdge(adj, 2, 3)
    addEdge(adj, 3, 3)

    print("This is the graph : ")
    for i in range(V):
        print(i, "-> ", end="")
        for j in adj[i]:
            print(j, end=" ")
        print()

    print("\nThis is the BFS : ")
    order = BFS(adj, V, 0)
    print()
    assert order == [0, 1, 2, 3]
