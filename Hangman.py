import numpy


def printhangman(numberwrong):
    print "  |-----|"

    if numberwrong >= 1:
        print "  |     0"
    else:
        print "  |      "
    if numberwrong >= 2:
        print "  |     |"
    else:
        print "  |      "
    if numberwrong >= 3:
        print "  |   / | \\"
    else:
        print "  |      "
    if numberwrong >= 4:
        print "  |     |"
    else:
        print "  |      "
    if numberwrong == 5:
        print "  |    /"
    elif numberwrong >= 6:
        print "  |    / \\"
    else:
        print "  |      "
    print "  |______"


def printbreak(word, correctletters):
    solved = True
    for a in word:
        a = a.lower()
        if a in correctletters:
            print a,
        else:
            print "_ ",
            solved = False
    print ""
    print ""
    return solved

guess_list = ["Achluophobia", "Agateophobia", "Anglophobia", "Arachibutyrophobia", "Arachnephobia", "Arithmophobia",
"Arrhenphobia", "Arsonphobia", "Ataxophobia", "Atelophobia", "Athazagoraphobia", "Atychiphobia", "Aulophobia",
"Auroraphobia", "Autophobia", "Aviophobia", "Chionophobia", "Dutchphobia", "Pagophobia"]


correct_letter = []

incorrect = 0

word = numpy.random.choice(guess_list)

while True:
    printhangman(incorrect)
    solved = printbreak(word, correct_letter)
    if incorrect >= 6:
         break
    if solved:
        print 'You win!'
        break

    guess = ""
    while len(guess) != 1:
        guess = raw_input("Guess a letter")

    guess = guess[0]
    if guess in word:
        correct_letter.append(guess)
        print "Correct guess"
    else:
        incorrect = incorrect + 1
        print("You are wrong");
print word