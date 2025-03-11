def to_jaden_case(string):
    spl_string = string.split()
    big_string  = []
    for el in spl_string:
        big_str = el.capitalize()
        big_string.append(big_str)
    result = ' '.join(big_string)
    return result