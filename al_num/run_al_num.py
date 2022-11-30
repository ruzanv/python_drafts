from test_dict_al_num import test_al_num
from string import ascii_lowercase

lst_numbers = [x for x in range(1, 29)]

lst_letters = [a for a in ascii_lowercase]

alphabet_number = dict(zip([x for x in range(1, 29)], [a for a in ascii_lowercase]))

if __name__ == '__main__':
    print(test_al_num(lst_numbers, lst_letters, alphabet_number))
