from alphabet_numbers import alpha_num

def test_al_num(lst_one, lst_two, dict_one):
    if alpha_num(lst_one, lst_two) == dict_one:
        return True
    else:
        return False
