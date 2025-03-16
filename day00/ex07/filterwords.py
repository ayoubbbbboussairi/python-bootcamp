import sys
import string

def filter(s,n):
    #supp les punctuation
    s = ''.join(caractere for caractere in s if caractere not in string.punctuation)
    i = 0
    s1 = s.split()
    mot_filtr = [ splited for splited in s1 if (len(splited) > int(n))] 
    # Afficher les mots filtrés
    print(', '.join(mot_filtr))

def typearg(s,n):
    try:
        str(s) and int (n)
        return True
    except:
        return False
    
def main():
    try :
        if (len(sys.argv) == 3 or typearg(sys.argv[1],sys.argv[2])):
            filter(sys.argv[1],sys.argv[2])
    except:
        print('error ')

if __name__ == "__main__" :
    main()