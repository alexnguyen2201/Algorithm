
class uf_ds:
    parent_node = {}

    def make_set(self, u):
        for i in u:
            self.parent_node[i] = i

    def op_find(self, k):
        if self.parent_node[k] == k:
            return k
        return self.op_find(self.parent_node[k])

    def op_union(self, a, b):
        x = self.op_find(a)
        y = self.op_find(b)
        self.parent_node[x] = y


def display(u, data):
    print([data.op_find(i) for i in u])


u = [1, 3, 5, 7]
data = uf_ds()
data.make_set(u)
display(u, data)
data.op_union(1, 5)
display(u, data)
data.op_union(7, 1)
display(u, data)

"""
 Ban đầu 5, 1, 7, 3 mỗi thằng tự là parent node của chính nó.
 Và cũng là 4 disjoint sets.
 - Sau đó nối 5 và 1, Lấy 5 là parent node của 1.
 - Tiếp tục nối 1 và 7, Lấy 1 là parent node của 7.
 - Kết quả ta thu được 2 disjoint sets
 5--->1--->7     3
"""
