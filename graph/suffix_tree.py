#!/usr/bin/env python

def palindrome(seq):
    seqLen = len(seq)
    lstLen = 2 * seqLen + 1
    lst = []

    for i in xrange(lstLen):
        s = i/2
        e = s + i%2

        while s > 0 and e < seqLen and seq[s-1] == seq[e]:
            s -= 1
            e += 1

        lst.append(seq[s:e])

    return lst

if __name__ == "__main__":

    print palindrome('ababa')
