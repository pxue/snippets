import random

def sort(a):

    if len(a) < 2: return a

    for i in xrange(len(a)):
        cur = a[i]
        j = i

        print i, cur
        while j > 0 and a[j-1]>cur:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1

    return a

if __name__ == '__main__':
    
    r = random.sample(range(1, 30), 20)
    print r
    
    print "SORTED ARRAY", sort(r)
