# calculates the sweetest ice cream in the list

def sweetest_icecream(lst):
    result = list()
    for i in lst:
        result.append(i.add())
    return max(result)
