import random
import PySimpleGUI as sg

sg.theme('Dark Grey 13')

ran_num = random.randint(1, 10)
lives = 3

setup_layout = [
    [sg.Text('Pick a number between 1 and 10. You have three oppuritunities to get the answer.')],
    [sg.Text('What is your guess?'), sg.InputText(key='-GUESS-')],
    [sg.Multiline(size=(50, 10), autoscroll=True, expand_x=True, expand_y=True, key='-OUTPUT-')],
    [sg.Button('Confirm'), sg.Button('Cancel')]
]

window1 = sg.Window('Random Number Game', setup_layout, resizable=True)

while True:
    event, values = window1.read()
    
    if event in (sg.WINDOW_CLOSED, 'Cancel'):
        break
    
    guess = values['-GUESS-']

    if event == 'Confirm':
        if not guess.isdigit() or not (1 <= int(guess) <= 10):
            window1['-OUTPUT-'].update('Please enter a valid number between 1 and 10.\n', append=True)
        else:
            guess = int(guess)
            if guess == ran_num:
                result_message = ("Congrats you don't suck.")
                result_window_active = True
                break
            else:
                lives -= 1
                window1['-OUTPUT-'].update(f'You suck at this. Lives: {lives}\n', append=True)

                if lives <= 0:
                    result_message = "You have lost the game. You are the worst."
                    result_window_active = True
                    break

if result_window_active:
    result_layout = [
        [sg.Text(result_message)],
        [sg.Button('Confirm you Suck')]
    ]

result_window = sg.Window('Game Result', result_layout)

while True:
    event, _ = result_window.read()
    if event in (sg.WIN_CLOSED, 'Confirm you Suck'):
        break


window1.close()
result_window.close()