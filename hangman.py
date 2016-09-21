from random import randrange

def getword(rand_num):
    with open('wordlist.txt','rb') as f:
        count = 1
        for line in f:
            if count != rand_num:
                count += 1
            else:
                return line.strip('\n')

def noose(hn):
    stage = {1:"Wrong letter, 4 chances left!",2:"Wrong letter, 3 chances left!",\
    3:"Wrong letter, 2 chances left!",4:"Wrong letter, 1 chance left!"}
    print stage[hn]

def replacer(word,word_dash,l):
    dash_list = list(word_dash)
    ind = 0
    first_ind = True
    cond = True
    while cond:
        if first_ind:
            ind = word.find(l)
            dash_list[ind] = l
            first_ind = False
        else:
            ind = word.find(l,ind+1)
            if ind == -1:
                break
            dash_list[ind] = l

    word_dash = ''.join(dash_list)
    return word_dash

def main():

    with open('wordlist.txt','rb') as f:
        linecount = 0
        for line in f:
            linecount += 1

    rand_num = randrange(1,linecount + 1)

    word = getword(rand_num)
    hangnum = 0
    length = len(word)
    word_dash = '_' * length
    tried_letters = set()

    while word_dash != word:
        print word_dash
        l = raw_input('Enter letter:')
        if len(l) != 1 or l.isalpha() == False:
            print "Please enter a valid letter!"
        elif l in tried_letters:
            print "You already tried that letter!"
        elif l in word:
            tried_letters.update(l)
            word_dash = replacer(word,word_dash,l)
        else:
            tried_letters.update(l)
            hangnum += 1
            if hangnum == 5:
                break
            else:
                noose(hangnum)

    if word_dash == word:
        print "Congratulations, you got the word '{0}'!".format(word)
        inp = raw_input("Play again?[y]")
        if inp == 'y':
            main()
    else:
        print "Wrong letter, you died!"
        print "The word was '{0}'. Better luck next time!".format(word)
        inp = raw_input("Play again?[y]")
        if inp == 'y':
            main()

main()
