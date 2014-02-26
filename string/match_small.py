#Question 2: Given a filename and a string, 
# see if the entire string can be duplicated 
# by the filename by only removing characters from the filename.

bigstr = 'some_random_file_name.ccx'
smallstr = 'me_dm_nam.cx'

def match(smallstr, bigstr):
    
    last_index = 0
    for i, chs in enumerate(smallstr):
        for j, chb in enumerate(bigstr):
            if chs == chb and j >= last_index:
                last_index = j
                break
            if j == len(bigstr) - 1:
                return False

    return True

import difflib
def match_faster(smallstr, bigstr):
    s = difflib.SequenceMatcher(None, bigstr, smallstr)
    # http://fossies.org/dox/Python-2.7.3/difflib_8py_source.html
    opcode = s.get_opcodes()
    for op in opcode:
        if op[0] not in ("delete", "equal"):
            return False
    return True

print smallstr
print bigstr
print match(smallstr, bigstr)

        



