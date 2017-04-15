from __future__ import print_function


def createNumStr(N):
    s = ""
    for i in range(1, N+1):
        s += str(i)

    return s


def print1ToN(N):
    num_str = createNumStr(N)
    print(num_str)


if __name__ == '__main__':
    n = int(raw_input())
    print1ToN(n)