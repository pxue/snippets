
def lcs(str1, str2):
    max_length = local_max = 0

    n = len(str1)
    m = len(str2)

    table = dict()

    for i in xrange(n+1):
        for j in xrange(m+1):
            counter += 1
            if i == 0 or j == 0:
                table[i, j] = 0
            elif str1[i-1] == str2[j-1]:
                table[i, j] = table[i-1, j-1] + 1
            else:
                table[i, j] = max(table[i-1, j], table[i, j-1])

    return table

l =  lcs('acbdegcedbg', 'begcfeubk')
print l
m = 0
for x in l.values():
    m = max(m, x)
print m
# b e g c e b => 6
