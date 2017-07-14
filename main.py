'''
下記の例題から数値は拝借
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0042
'''
import sys
import numpy as np

class Item:
    def __init__(self, p=0, c=0):
        self.set(p, c)

    def set(self, p=0, c=0):
        self.p = p
        self.c = c

def dp(C, items):
    m = np.zeros((len(items), C + 1))
    for i in range(1, len(items)):
        for j in range(C + 1):
            if items[i].c < j:
                m[i][j] = max(m[i-1][j], m[i-1][j-items[i].c]+items[i].p)
            else:
                m[i][j] = m[i-1][j]
    return m[-1][-1]

def main(argv):
    C = 50
    items = [
        Item(60, 10),
        Item(100, 20),
        Item(120, 30),
        Item(210, 45),
        Item(10, 4),
    ]

    print(dp(C, items))

    return

if __name__ == '__main__':
    main(sys.argv)
