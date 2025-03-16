import sys

def isinteger(argument):
    try:
        int(argument)
        return True
    except :
        return False

def fun_odd_even_zero(argument):
    nombre = int(argument)
    if nombre == 0:
        print('Je suis zéro')
    elif nombre % 2 == 0:
        print('Je suis pair')
    else:
        print('Je suis impair')

def check_func():
    if len(sys.argv) > 2:
        print('Erreur : Fournissez exactement un argument.')
    elif not isinteger(sys.argv[1]):
        print('Erreur : L\'argument n\'est pas un entier.')
    else:
        fun_odd_even_zero(sys.argv[1])

check_func()
