#function for counting vowels in string
def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    result = [i for i in string if i in vowels]
    return len(result)
