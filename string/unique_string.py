#!/usr/bin/env python
# Check if string has all unique characters
# Using no additional data structures

def str_unique_iter(s):
    for i, ch in enumerate(s):
        for j, chr in enumerate(s):
            if i != j and ch == chr:
                return False
    return True

def str_unique_array(s):
    tmp = ['']*256
    for ch in s:
        if tmp[ord(ch)]: return False
        else: tmp[ord(ch)] = ch
    return True

def str_unique_bitvector(s):
    # assume string is lower case a - z

    checker = 0
    for ch in s:
        val = ord(ch) - ord('a')
        if (checker & (1 << val)) > 0: return False
        checker |= (1 << val)

    return True

if __name__ == "__main__":
    
    s = "azgefa"
    print "String %s is unique?: %s" % (s, str_unique_array(s))
    print "String %s is unique?: %s" % (s, str_unique_iter(s))
    print "String %s is unique?: %s" % (s, str_unique_bitvector(s))
    
