import random

secret   = random.randint(1, 10)



counter = 0

while counter < 5:
    try:
        guess = int(raw_input("?\n"))
    except ValueError:
        print "please enter number"
        continue

    counter += 1

    if secret == guess:
        print "You win"
        break
    elif secret > guess:
        print ">"
        continue
    elif secret < guess:
        print "<"
        continue
else:
    print 'Looser!'

