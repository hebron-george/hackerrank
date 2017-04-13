

class Divider(object):

    def __init__(self):
        pass

    def intDivide(self, a, b):
        a = int(a)
        b = int(b)

        return int(a/b)

    def floatDivide(self, a, b):
        a = float(a)
        b = float(b)

        return a/b

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

    divider = Divider()
    print divider.intDivide(a,b)
    print divider.floatDivide(a,b)