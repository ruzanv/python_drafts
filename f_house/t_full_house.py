from full_house import is_full_house


def test_full_house(list1, value):
    if is_full_house(list1) == value:
        return True
    else:
        return False
