import sys
import string



def text_analyser(s):    
    '''
displays the sums of its upper-case characters, lower-case characters, punctuation characters and spaces.
'''

    count = 0
    countlower = 0
    countupper = 0
    countspace = 0
    countpunctuation = 0
    i=0
    while i < len(s) :
        count = count + 1
        if s[i].islower() :
            countlower = countlower + 1
        elif s[i].isupper() :
            countupper = countupper + 1
        elif s[i].isspace() :
            countspace = countspace + 1
        elif s[i] in string.punctuation :
            countpunctuation = countpunctuation + 1
        i = i + 1
    print('le nombre de caractere is :',count)
    print ('lower letter(s) is :',countlower)
    print('upper letter(s) is :', countupper)
    print('les spaces is : ', countspace)
    print('les punctuations :', countpunctuation)

def test_fun (arg):
    try:
        str(arg)
        return True
    except:
        print('enter a string')
        return False
def main () :
    if len(sys.argv) == 2 and test_fun(sys.argv[1]):
        text_analyser(sys.argv[1])
    else:
        print('ereur')

if __name__ == "__main__":
    main()


    
