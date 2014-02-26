#!/usr/bin/env python

def reverse(s):
    
    l = s.split(' ')

    return ' '.join(l[::-1])

print reverse("Do or do not, there is no try.")
