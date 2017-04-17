def isDivisibleBy4(y):
    return True if y % 4 == 0 else False


def isDivisibleBy100(y):
    return True if y % 100 == 0 else False


def isDivisibleBy400(y):
    return True if y % 400 == 0 else False


def is_leap(y):
    if isDivisibleBy400(y):
        return True
    elif isDivisibleBy4(y) and not isDivisibleBy100(y):
        return True
    else:
        return False


if __name__ == "__main__":
    year = int(raw_input())
    print is_leap(year)

