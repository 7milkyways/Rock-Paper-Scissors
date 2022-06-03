import random


#initializing a Boolean to loop code when ever we get user errors
start_over = True

print("___WELCOME___ \n")
print("___BEAT THE COMPUTER TO SAVE THE PRINCESS___ \n")
print("GUIDELINES: \n")
print("ROCK(R) BEATS SCISSORS(S)\n")
print("SCISSORS(S) BEATS PAPER(P)\n")
print("PAPER(P) BEATS ROCK(R)\n")


while (start_over == True):
    allowed_moves = ["R", "P", "S"]
    player = input("MAKE YOU MOVE: ")
    computer = random.choice(allowed_moves)
    
    player = player.upper()
    print('Player('+player+') : Computer('+computer+')\n')
    

    if player not in allowed_moves:
        print("NOT A VALIED MOVE \n")
        start_over = True
    
    else:
        if player == computer:
            print("IT'S A TIE \n")
            print("YOU STILL HAVE SOME HOPE \n")
            start_over = True
        
        elif player == "R":
            
            if computer == "S":
                print(":) YEEEHHH YOU SAVED THE PRINCESS\n")
                print("YOU WON")
                break
            elif computer == "P":
                print(":( OOOH NO YOU LOSSED THE PRINCESS\n")
                print('YOU LOSE')
                break
        elif player == "S":
            
            if computer == "P":
                print(":) YEEEHHH YOU SAVED THE PRINCESS\n")
                print("YOU WON")
                break
            elif computer == "R":
                print(":( OOOH NO YOU LOSSED THE PRINCESS\n")
                print('YOU LOSE')
                break
        elif player == "P":
            
            if computer == "R":
                print(":) YEEEHHH YOU SAVED THE PRINCESS\n")
                print("YOU WON")
                break
            elif computer == "S":
                print(":( OOOH NO YOU LOSSED THE PRINCESS\n")
                print('YOU LOSE')
                break
