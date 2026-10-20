# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=AsAdKHkITBQ
# Company Tags                : Google, Facebook, Apple, Amazon, Netflix, Flipkart

# Complete the functions below
parent = []
rank = []


def find(x: int) -> int:
    if x == parent[x]:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def Union(x: int, y: int) -> None:
    x_parent = find(x)
    y_parent = find(y)

    if x_parent == y_parent:
        return

    if rank[x_parent] > rank[y_parent]:
        parent[y_parent] = x_parent
    elif rank[x_parent] < rank[y_parent]:
        parent[x_parent] = y_parent
    else:
        parent[x_parent] = y_parent
        rank[y_parent] += 1


if __name__ == "__main__":
    n = 6
    parent[:] = list(range(n))
    rank[:] = [0] * n
    Union(0, 1)
    Union(0, 2)
    assert find(0) == find(2)
    assert find(0) != find(3)
    Union(0, 3)
    assert find(0) == find(3)
    print("ok")
