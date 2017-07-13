'''
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0042
'''
import sys

class Item:
    def __init__(self, p=0, c=0):
        self.set(p, c)

    def set(self, p=0, c=0):
        self.p = p
        self.c = c

def dp(C, items):
    return 0, 0

def main(argv):
    C = 50
    items = [
        Item(60, 10),
        Item(100, 20),
        Item(120, 30),
        Item(210, 45),
        Item(10, 4),
    ]

    c, p = dp(C, items)
    return

if __name__ == '__main__':
    main(sys.argv)
