import sys
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ' ' : '/'}

def trenslate_msg(msg) :
    tr_msg = ' '.join(MORSE_CODE_DICT[c] for c in msg.upper())
    print(tr_msg)

def main():
    try:
        if (len(sys.argv) > 1):
            s = ' '.join(sys.argv[1:])
        trenslate_msg(s)
    except:
        print('pleas enter a message to trenslate')

if __name__ == "__main__":
    main()