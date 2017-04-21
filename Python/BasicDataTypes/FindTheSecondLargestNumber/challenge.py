def get_second_largest(a):
    a = list(set(a))  # remove duplicates
    a.sort()  # sort to get second largest by index
    return a[-2]

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    print get_second_largest(arr)