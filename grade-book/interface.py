import PySimpleGUI as sg
import database

# updates home on term search
def termCall(window, term):
    txt = term.split(" ")
    window['-TERM-'].update("Term: " + txt[0] + "      " + "Year: " + txt [1])


# Set theme and set var for buttons
sg.theme('DarkGrey4')
image_data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\rIDATx\x9cc````\x00\x00\x00\x05\x00\x01\xa5\xf6E@\x00\x00\x00\x00IEND\xaeB`\x82'

# Sets menubar
menuBar = [
        ['File', ['Insert'],],
        ['Edit', ['Class', 'Grade'],],
        ]

# Sets term selection drop down
termVals = ['Select Term','Spring 2024', 'Summer 2024', 'Fall 2024', 'Spring 2025']
termLst = sg.Combo(termVals, enable_events=True,  readonly=True, default_value= 'Select Term', k="-termSelection-")

# Sets home layout
homeLayout = [
    [sg.Menu(menuBar)],
    [termLst, sg.Button('Search', image_data=image_data, image_size= (35,9))],
    [sg.HorizontalSeparator()],
    [sg.Text(key='-TERM-')],
    ]

# Starts window
window = sg.Window('Grade Book', homeLayout, size=(500,500))

while True:
    event,values=window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
            break
    if event == 'Search':
        if values['-termSelection-'] != "Select Term":
            termCall(window, (values["-termSelection-"]))
    if event == 'Insert':
        print ("hello")

window.close()

# [sg.Menu(menuBar,)],
#     [termLst, sg.Button('Search', image_data=image_data, image_size= (35,9))],
#     [sg.HorizontalSeparator()],
#     [sg.Text(key='-TERM-')],