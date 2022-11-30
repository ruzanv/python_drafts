from count_vowels import count_vowels

def test_count_vow(string, true_num):
    if count_vowels(string) == true_num:
        return True
    else:
        return False