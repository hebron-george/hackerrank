def get_n_squares(param):
    return [digit*digit for digit in range(0, param)]

if __name__ == '__main__':
    n = int(raw_input())
    squares = get_n_squares(n)
    for i in squares:
        print str(i)
