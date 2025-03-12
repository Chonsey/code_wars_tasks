def reverse_words(text):
    sp_text = text.split(' ')
    total = []
    for i in sp_text:
        rev_text = i[::-1]
        total.append(rev_text)
    return ' '.join(total)
    