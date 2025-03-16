import random

def guess_num():
    n = random.randint(1,99)
    print ('This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType \'exit\' to end the game.\nGood luck!')
    count = 0
    while True:
        num = int(input ('What\'s your guess between 1 and 99?'))
        if( num == 'exit'):
            break
        try:
            n = int(n)
        except:
            print("Veuillez entrer un nombre valide.")
            continue
        count = count + 1
        if(num > n):
            print('Too high!')
        elif(num < n):
            print('Too low!')
        elif (num == n):
            print('Congratulations, you ve got it!')
            print(f"You won in {count} attempts!")
            break

if __name__ == "_main_":
    guess_num()