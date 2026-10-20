# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=kGv33AiGhdc
# Company Tags                : Google, Facebook, Apple, Amazon, Netflix, Flipkart

class DSU:
    def __init__(self, n: int):
        self.parent = [0] * n
        self.size = [0] * n

        for i in range(n):
            self.parent[i] = i
            self.size[i] = 1

    def find(self, x: int) -> int:
        if x == self.parent[x]:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def Union(self, x: int, y: int) -> None:
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent == y_parent:
            return

        if self.size[x_parent] > self.size[y_parent]:
            self.parent[y_parent] = x_parent
            self.size[x_parent] += self.size[y_parent]
        elif self.size[x_parent] < self.size[y_parent]:
            self.parent[x_parent] = y_parent
            self.size[y_parent] += self.size[x_parent]
        else:
            self.parent[x_parent] = y_parent
            self.size[y_parent] += self.size[x_parent]


def main():
    dsu = DSU(6)
    dsu.Union(0, 1)
    dsu.Union(0, 2)

    # if 0 and 3 are not on same Component yet
    if dsu.find(0) == dsu.find(3):
        print("In same component")
    else:
        print("Not in same component")

    # Now we will Union 0 and 3
    dsu.Union(0, 3)
    if dsu.find(0) == dsu.find(3):
        print("In same component")
    else:
        print("Not in same component")


if __name__ == "__main__":
    main()
    d = DSU(6)
    d.Union(0, 1)
    d.Union(0, 2)
    assert d.find(0) != d.find(3)
    d.Union(0, 3)
    assert d.find(0) == d.find(3)
    assert d.size[d.find(0)] == 4
    print("ok")
