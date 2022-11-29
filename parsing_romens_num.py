# function parses numbers in roman and converts to numbers in arabic

def parsing_romen(romen):
    romens_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i, v in enumerate(romen):
        if i+1 < len(romen) and romens_values[romen[i]] < romens_values[romen[i+1]]:
            result -= romens_values[romen[i]]
        else:
            result += romens_values[romen[i]]
    return result
