
def kadanestr(s):
    local_max = max = 0
    last_character = longest_char = ""

    for ch in s:
        if ch == last_character:
            local_max += 1
            if local_max > max:
                max = local_max
                longest_char = ch
        else:
            local_max = 1
            last_character = ch

    return longest_char
            
print kadanestr("aaabbcdffffffexxxzzzzggg")
