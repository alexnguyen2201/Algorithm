class DSU:
    def __init__(self):
        self.p = {}
        self.sum = {}

    def find(self, a):
        if a not in self.p:
            return

        if self.p[a] != a:
            self.p[a] = self.find(self.p[a])
        return self.p[a]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.p[root_a] = root_b
            self.sum[root_b] = self.sum[root_b] + self.sum[root_a]

    def insert(self, a):
        self.p[a] = a
        self.sum[a] = 1
