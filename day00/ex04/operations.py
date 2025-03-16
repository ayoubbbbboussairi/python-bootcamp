import sys

def calculator(A,B) :
    A = int (A)
    B = int  (B)
    sum = A + B
    diff = A - B
    multi = A * B

    print('la somme ', sum)
    print('la difference ', diff)
    print('la multiplication', multi)
    
    if B != 0 :
        div = A / B
        modulo = A % B
    elif B == 0:
        print('la division : impossible de diviser par 0')
        print('le modulo : impossible de diviser sur 0')
        return
    print('la division', div)
    print('le modulo', modulo)

def test_int(A,B):
    try:
        int(A) and int(B)
        return True
    except :
        return False
    
def main():
    if len(sys.argv) == 3 and test_int(sys.argv[1],sys.argv[2]) :
        calculator(sys.argv[1],sys.argv[2])
    else:
        print('enter 2 number')

if __name__ == "__main__":
    main()