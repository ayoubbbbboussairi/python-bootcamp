import sys

def fun_rev_swap (str) :
    rev_str = str[::-1]
    swap_rev_str = rev_str.swapcase()
    return(swap_rev_str)

def fun() :
    if len(sys.argv) > 1 :
        str = " ".join(sys.argv[1:])
        s = fun_rev_swap(str)
        print(s)
    else :
        print("usage ,,,,,,,,")

fun()