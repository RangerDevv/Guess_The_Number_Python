import random

randomnumber = random.randint(1, 9)

userinput = input()

if userinput=='hello':
    print('hello world')
    print(randomnumber)

# if statements
    if userinput==randomnumber:
        print('you have guessed the right number')
    elif userinput>randomnumber:
        print('its too high!')