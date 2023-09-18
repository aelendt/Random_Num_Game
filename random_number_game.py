import random
import PySimpleGUI as sg

sg.theme('Dark Grey 13')

ran_num = random.randint(1, 10)
lives = 3

print('Number: ' + str(ran_num))

setup_layout = [
    [sg.Text('Pick a number between 1 and 10. You have three oppuritunities to get the answer.')],
    [sg.Text('What is your guess?'), sg.InputText(key='-GUESS-')],
    [sg.Multiline(size=(50, 10), autoscroll=True, expand_x=True, expand_y=True, key='-OUTPUT-')],
    [sg.Button('Confirm'), sg.Button('Cancel')]
]

window1 = sg.Window('Random Number Game', setup_layout, resizable=True)
loss_window_active = False
win_window_active = False

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
                win_message = ("Congrats you don't suck.")
                win_window_active = True
                break
            else:
                lives -= 1
                window1['-OUTPUT-'].update(f'You suck at this. Lives: {lives}\n', append=True)

                if lives <= 0:
                    loss_message = "You have lost the game. You are the worst."
                    loss_window_active = True
                    break

if loss_window_active:
    loss_layout = [
        [sg.Text(loss_message)],
        [sg.Button('Confirm you Suck')]
    ]
    
    loss_window = sg.Window('Game Result', loss_layout)

    while True:
        event, _ = loss_window.read()
        if event in (sg.WIN_CLOSED, 'Confirm you Suck'):
            break


if win_window_active:
    win_layout = [
        [sg.Text(win_message)],
        [sg.Button('Confirm')]
    ]

    win_window = sg.Window('Game Result', win_layout)

    while True:
        event, _ = win_window.read()
        if event in (sg.WIN_CLOSED, 'Confirm'):
            break


window1.close()
loss_window.close()
win_window.close()


print('Hello').lower()