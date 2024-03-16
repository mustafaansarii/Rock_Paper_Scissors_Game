import random
import gradio as gr

def play_game(your_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    if your_choice == computer_choice:
        result = "It's a tie!"
    elif (your_choice == 'rock' and computer_choice == 'scissors') or \
         (your_choice == 'paper' and computer_choice == 'rock') or \
         (your_choice == 'scissors' and computer_choice == 'paper'):
        result = "You win!"
    else:
        result = "Computer wins!"
    
    return f"You choose {your_choice}, computer choose {computer_choice}. {result}"

iface = gr.Interface(play_game, gr.Dropdown(["rock", "paper","scissors"]), "text")
iface.launch(share=True)
