class UnionFind:

    def __init__(self, cap):
        self.cap = cap
        self.size = 0
        self.p = list(range(cap))
        self.rank = [0] * cap
        self.left_ch = list(range(cap))
        self.ans = [-1] * cap

    def append(self, n, d):
        already = self.find(d)
        ind = self.left_ch[already]
        self.ans[ind] = n
        self.size += 1
        if self.cap == self.size: return
        self.union(already, ind)

        ind = (self.cap + (ind - 1)) % self.cap
        while self.ans[ind] != -1:
            new_ind = self.left_ch[self.find(ind)]
            self.union(already, ind)
            ind = new_ind
        self.left_ch[self.find(already)] = ind

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        if (x := self.find(x)) == (y := self.find(y)):
            return False

        if self.rank[x] < self.rank[y]:
            self.p[x] = y
        else:
            self.p[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

        return True

    def count_eq(self):
        return len(set(self.p))

    def get_ans(self):
        return self.ans


def uf_solution(tasks):
    for task in tasks:
        uf = UnionFind(len(task))
        task = sorted(task, key=lambda x: -x[2])
        for i in task:
            num, deadline, fine = map(int, i)
            uf.append(num, deadline - 1)
        print(uf.ans)


tasks = [[(4, 3, 50), (3, 1, 30), (1, 3, 25), (5, 3, 20), (2, 4, 10)],
         [(4, 1, 70), (1, 3, 25), (5, 4, 15), (2, 5, 10), (3, 2, 45)]]

uf_solution(tasks)
