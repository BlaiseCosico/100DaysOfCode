from rpsClasses import Player, Roll, Rock, Paper, Scissors
import random

def print_header():
	print('-------------------------')
	print('---ROCK PAPER SCISSORS---')
	print('-------------------------')
	print()

def get_players_name():
	return input("Enter username: ")

def build_the_three_rolls():
	rolls = [
			Rock('Rock', ['Paper']),
			Paper('Paper', ['Scissors']),
			Scissors('Scissors', ['Rock'])
	]

	return rolls

def player_choice_convertion(c):
	choice = {
			'R':Rock('Rock', ['Paper']),
			'P':Paper('Paper', ['Scissors']),
			'S':Scissors('Scissors', ['Rock'])
	}
	return choice[c]
def main():
    print_header()

    rolls = build_the_three_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2, rolls)

def game_loop(player1, player2, rolls):
	count = 1
	while count < 3:
	    p2_roll = random.choice(rolls) # TODO: get random roll
	    choice = input('[R]ock, [P]aper or [S]cissors: ').upper() # TODO: have player choose a roll

	    if choice not in ['R','P','S']:
	    	choice = input('please enter a valid choice')
	    else:
	    	p1_roll = player_choice_convertion(choice)

	   
	    print(f'Computer chose {p2_roll.name}!')
	    
	    if p1_roll.name == p2_roll.name:
	    	print("It's a tie!")
	    elif p1_roll.can_defeat(p2_roll):
	    	print('You win!')
	    else:
	    	print('Sorry, try again')
	    	
	    

	    # display throws
	    # display winner for this round

	    count += 1

	# Compute who won


if __name__ == '__main__':
	main()