import random

randomnumber = random.randint(1, 9)

while True:
    userinpute = int(input('type your guess:'))
    if userinpute>randomnumber:
        print('it is too high!')
        continue
    elif userinpute<randomnumber:
        print('too low!')
        continue
    else:
        break

print("you guessed it!")
    