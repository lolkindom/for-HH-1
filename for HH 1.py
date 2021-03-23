def is_even(value):
    return not value & 1


if __name__ == '__main__':
    assert is_even(3) == False
    assert is_even(4) == True
