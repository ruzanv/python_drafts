def check_sequence(lst):
    if lst[1] == lst[0]+1 and lst[2] == lst[1]+1:
        return 1
    elif lst[1] == lst[0]-1 and lst[2] == lst[1]-1:
        return -1
    else:
        return 0
