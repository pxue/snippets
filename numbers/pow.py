def pow(x, b):
    # code in O(log(n)) time
    # return x^b, b can be negative
    # x is double
    # b is integer

    if b == 0:
        return 1
    r = pow(x, b/2)
    if (b%2 == 0): #even
        return r*r
    else:
        if b > 0:
            return x*r*r
        else:
            return (r*r)/x

    # O(b) time solution
    #for i in xrange(abs(b)):
        #if b < 0:
            #r = r/x
        #else:
            #r = r*x

    # O(log(n)) time solution
    # c = log_b(a) = 0 -> a = 1, b = anything
    # k = 1
    # we need to reduce problem by half each time
    # T(n/2)


#print pow(5.5, 2), "30.25"
print pow(5.5, -2), "0.033"
#print pow(5.5, 0), "1"
