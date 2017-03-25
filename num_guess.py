import random
import time

MIN = 0
MAX = 1000

def perform_guessing(number,player1,player2,game_mode):

    silly_user = True
    while silly_user:
        try:
            p1_guess = int(raw_input("\n" + str(player1) + "'s Guess: "))
            silly_user = False
        except ValueError:
            print "Dear please give us a number."
    if game_mode == 1:
        p2_guess = random.randint(MIN, MAX)
        print "Computer's Guess:", p2_guess
    else:
        silly_user2 = True
        while silly_user2:
            try:
                p2_guess = int(raw_input(str(player2) + "'s Guess: "))
                silly_user2 = False
            except ValueError:
                print "Dear please give us a number."

    print 'Magic Number:', number

    player1_score = abs(p1_guess - number)
    player2_score = abs(p2_guess - number)

    return player1_score < player2_score

def main():

    print 'Welcome to the guessing game!'
    print 'A number will be randomly chosen from', MIN, 'to', MAX
    print 'The player will make a guess, and then the computer / another player will guess.'
    print 'Whoever is closest to the Number wins that round!'
    print 'First to reach 3 out of 5 rounds wins!'

    player1_wins = 0
    player2_wins = 0
    user_name = True
    n_cnt = 0
    while user_name:
        player1 = unicode(raw_input('\nYour name: '))
        if len(player1) < 3 or player1.isnumeric():
            n_cnt += 1
            if n_cnt > 1:
                print "seriously! get a proper Name"
            else:
                print "Aha! Smarty pants, you can't fool me. now try again"
                
        else:
            if n_cnt > 1:
                print "Finally! Welcome, " + str(player1)
            else:
                print "Hi "+ str(player1) + "! welcome."
            user_name = False
            n_cnt = 0
	    
    game_mode = int(raw_input('\nChoose to Play Against: \n1.Computer\n2.Friend \r'))
    if game_mode == 2:
        print "\nHi there!"
        user_name2 = True
        while user_name2:
            player2 = unicode(raw_input('Your name please: '))
            if len(player2) < 3 or player2.isnumeric():
                n_cnt += 1
                if n_cnt > 1:
                    print "seriously! get a proper Name. " + "\n" + str(player1) + "!, help your friend."
                else:
                    print "Aha! Smarty pants, you can't fool me."
            else:
                if n_cnt > 1:
                    print "Finally! Welcome, " + str(player2)
                else:
                    print "Hi " +str(player2) + "! Welcome to the game."
                user_name2 = False
    else:
        player2 = 'Computer'
        
    for rounds in range(5):
        if perform_guessing(random.randint(MIN, MAX), player1,player2,game_mode):
            player1_wins += 1
            print str(player1) + ' won that round!'

        else:
            player2_wins += 1
            if game_mode == 1:
                print 'You lost that round!'
            else:
                print str(player2) + ' won that round!'

        if player1_wins >= 3 or player2_wins >= 3:
            break

    if player1_wins > player2_wins:
        print "aand.. " + str(player1) + ', You won the GAME!'
    else:
        if game_mode == 1:
            print 'and.. You lost the GAME!'
        else:
           print "aand.. " + str(player2) + ', You won the Game!'
    play_again = raw_input('\nDo you want to play again: y/n: ')
    if play_again == 'y':
        print "\n\nGame Refreshing...\n\n"
        time.sleep(2)
        main()
    else:
        print "\nThank you " + str(player1)+ ", have a good day!\n"
        
if __name__ == '__main__':
    main()
