import random

def play():

    user = input("Enter 'r' for rock, 'p' for paper and 's' for scissors: ")
    computer = random.choice(['r','p','s'])
    if user == computer:
        return "It's a tie!"

    elif is_win(user, computer):
        return "You win!"

    return "You lost!"

def is_win(player, opponent):
    #r>s, p>r, s>p
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent =='p'):
        return True

print(play())