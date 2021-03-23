def is_even1(value):
    return not value & 1


def is_even2(value):
    return value % 10 in [0, 2, 4, 6, 8]


if __name__ == '__main__':
    assert is_even1(3) == False
    assert is_even1(4) == True
    assert is_even2(5) == False
    assert is_even2(6) == True
