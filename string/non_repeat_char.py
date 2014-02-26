
def non_repeated_char(s):
    
    d = dict()
    for ch in s:
        if not d.get(ch):
            d[ch] = 1
        else:
            d[ch] += 1

    for ch in s:
        if d[ch] == 1:
            return ch

print non_repeated_char('aaaaadds')
