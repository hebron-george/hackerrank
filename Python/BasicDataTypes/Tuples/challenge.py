def create_hash(o):
    return hash(o)

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    print create_hash(tuple(integer_list))
