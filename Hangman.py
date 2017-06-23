import numpy

#  these are the functions that are later called on to make the hangman
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
#  I added many words to be guessed that are not commenly known or are certain phobias
guess_list = ["Achluophobia", "Agateophobia", "Anglophobia", "Arachibutyrophobia", "Arachnephobia", "Arithmophobia",
"Arrhenphobia", "Arsonphobia", "Ataxophobia", "Atelophobia", "Athazagoraphobia", "Atychiphobia", "Aulophobia",
"Auroraphobia", "Autophobia", "Aviophobia", "Chionophobia", "Dutchphobia", "Pagophobia", "alcazar", "bezoar",
"bibliopole", "cryptozoology","Acersecomic", "Hamartia", "Hiraeth", "Petrichor", "Vellichor", "Effervesence", "Psychopomp",
 "Mythopoeic", "Oneiromancy", "Sipapu", "Paracosm", "Sambhogakaya", "Palimpsest", "Hypnagogia", "Farctate", "Philodox",
"Gramercy", "Cavil", "Churlish", "Frisson", "Gargalesthesia", "Beldam", "Defalcation", "Vulpine", "Buccula", "Brontide",
"Morosoph", "Sylvan", "Hypermnesia", "Factotum", "Virago", "Lalochezia", "Mudita", "Komorebi", "Tsundoku", "Embasan",
"Voorpret", "Mamihlapinatapai", "Fernweh", "Meraki", "Jayus", "Hanyauku", "Gigil", "Lagon", "Hygge", "Waldeinsamket",
"Ubuntu", "Laotong", "Kuidaore", "Tidoptimist", "Sobremesa", "Goya", "Nunchi", "Prozvonit", "Shemomedjamo", "Manja",
"Backpfeifengesicht", "Pochemuchka", "Schadenfreude", "Taarradhin", "Tatemae", "Honne", "Fremdschamen", "Aware",
"Bricoleur", "Duende", "Saudade", "Hyggelig", "Tingo", "Kyoikumama", "Tartle", "Iktsuarpok", "Cafune", "Torschlusspanik",
"Ilunga", "Depaysement", "Kitsch", "Litost", "Toska", "Layogenic", "Rhwe", "Zeg", "Lagom", "Gezellig", "Kaelling",
"Verschlimmbesserung", "Orenda", "Weltschmerz", "Razbliuto", "Uitwaaien", "Qualunquismo", "Zalatwic", "Zhaghzhagh",
"Yuputka", "Slampadato","BTS", "Jimin", "Jeongkook", "V", "Suga", "Jin", "JHope", "Rapmonster"]

#  this is where the correct letters will go after teh function is called on
correct_letter = []

incorrect = 0
# so the words are completely random, this function will call the words in random order so no can memorise the order and
#  figure out the word that way
word = numpy.random.choice(guess_list)
#  this loop will keep the game going until the person either wins or loses the game
while True:
    printhangman(incorrect)
    solved = printbreak(word, correct_letter)
    if incorrect >= 6:
         break
    if solved:
        print 'You win!'
        break
#  the player would be asked to print there guess, and this would stop the player from being able to input more than one
#  or less than one letter
    guess = ""
    while len(guess) != 1:
        guess = raw_input("Guess a letter")
#  if the player guessed correclty, this function would say correct guess and replace the blank with the correct letter
    guess = guess[0]
    guess = guess.lower()
    if guess in word.lower():
        correct_letter.append(guess)
        print "Correct guess"
    else:
        incorrect = incorrect + 1
        print("You are wrong")
#  at the end, this function will print the word weither the player guessed it or not
print word