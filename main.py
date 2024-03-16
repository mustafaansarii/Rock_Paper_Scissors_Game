import random
import gradio as gr

def play_game(player_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        result = "You win!"
    else:
        result = "Computer wins!"
    
    return f"You chose {player_choice}, computer chose {computer_choice}. {result}"

iface = gr.Interface(play_game, "text", "text")
iface.launch()
