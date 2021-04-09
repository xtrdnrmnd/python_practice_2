class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def isPrime(self):
        i = 0
        for itemss in self.items:
            if itemss % 2 != 0:
                d = 3
                while d * d <= itemss and itemss % d != 0:
                    d += 2
                if (d * d > itemss):
                    i += 1
        return i
