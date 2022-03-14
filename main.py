import random

randomnumber = random.randint(1, 9)

while True:
    print('guess a number')
    userinpute = int(input())
    if userinpute>randomnumber:
        print('it is too high!')
        continue
    elif userinpute<randomnumber:
        print('too low!')
        continue
    else:
        break

print("you guessed it!")
    