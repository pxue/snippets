
def removed(l):

    z = 0
    for i in l:
        z = z ^ i

    del l[2]

    for i in l:
        z = z ^ i

    return z


l = [1,2,3,4,5,6]
print "list is", l
print "we are going to remove 3"
print removed(l)
