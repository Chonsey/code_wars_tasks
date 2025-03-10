



def abbrev_name(name):
    spl_names = name.split()
    big_names = []
    for i in spl_names:
        big_names.append(i[0].upper())
    result = big_names[0]+'.'+ big_names[1]
    return result