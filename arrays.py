import pandas as pd

XSIZE = 5  # 100
YSIZE = 5  # 60


class arrays():

    def __init__(self, XSIZE=100, YSIZE=60):
        self.xsize = XSIZE
        self.ysize = YSIZE
        self.now = self.empty_Frame()
        # self.principalArray= self.empty_Frame()

    def empty_Frame(self):
        return pd.DataFrame([[0]*self.xsize]*self.ysize)

    def sum_neighbor(self, x, y):
        return self.now.loc[y-1:y+1, x-1:x+1].sum().sum()

    def do_tick(self):
        self.result = self.empty_Frame()
        for y in range(self.ysize):
            for x in range(self.xsize):
                sum = self.sum_neighbor(x, y) - self.now[x][y]
                self.result[x][y] = self.tha_rulez(sum,self.now[x][y])
        self.now = self.result

    def tha_rulez(self, sum, isalive):
        # Si una célula está viva y tiene dos o tres vecinas vivas, sobrevive.
        if (sum == 3 or sum == 2) and isalive: return 1
        # Si una célula está muerta y tiene tres vecinas vivas, nace.
        if sum == 3 and not isalive: return 1
        # Si una célula está viva y tiene más de tres vecinas vivas, muere.
        if sum > 3 and isalive: return 0
        return 0

a = arrays(XSIZE, YSIZE)

a.now.loc[1:3,2] = 1
print(a.now)
a.do_tick()
print(a.now)

a.do_tick()
print(a.now)

pass
