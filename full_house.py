# function that indicates the presence of a full house

def is_full_house(list1):
    set_full_house = list(set(list1))
    if len(set_full_house) != 2:
        return False
    elif list1.count(set_full_house[0]) == 3 and list1.count(set_full_house[1]) == 2:
        return True
    elif list1.count(set_full_house[1]) == 3 and list1.count(set_full_house[0]) == 2:
        return True
    else:
        return False