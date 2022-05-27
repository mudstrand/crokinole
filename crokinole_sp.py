import PySimpleGUI as sg

layout = [
    [sg.Text('Text', enable_events = True, key = '-TEXT-'), sg.Spin(['item1', 'item2'])],
    [sg.Button('Button', key = '-BUTTON1-')],
    [sg.Input(key = '-INPUT-')],
    [sg.Text('Test'), sg.Button('Test Button', key = '-BUTTON2-')]
]

window = sg.Window('crokinole', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == '-TEXT-':
        print('text was pressed')
    if event == '-BUTTON1-':
        print(values['-INPUT-'])
        window['-TEXT-'].update(values['-INPUT-'])
    if event == '-BUTTON2-':
        print('button 2 pressed')

window.close()