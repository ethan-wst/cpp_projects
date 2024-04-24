import PySimpleGUI as sg
import database

# Set windows theme, image data for buttons, and termval for term dropdowns
sg.theme('DarkGrey4')
image_data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\rIDATx\x9cc````\x00\x00\x00\x05\x00\x01\xa5\xf6E@\x00\x00\x00\x00IEND\xaeB`\x82'
termVals = ['Select Term','Spring 2024', 'Summer 2024', 'Fall 2024', 'Spring 2025']

# Updates homeWindow display when "Search" button is pressed with Term slected
def termCall(window, term):
    txt = term.split(" ")
    window['-TERM-'].update("Term: " + txt[0] + "      " + "Year: " + txt [1])
    mycursor = database.gradeData
    results = database.getClassArray(txt[1], txt[0])

    i = 1
    for r in results:
        target = '-CLASS' + str(i) + '-'
        if (r[2]): window[target].update(str(r[0]) + "    " + r[1] + "    " + r[2])
        else : window[target].update(str(r[0]) + "    " + r[1])
        i +=1


# Defines insertPopUp window
def insertWindow ():
    termLstInsert = sg.Combo(termVals, size=(15,1), enable_events=True,  readonly=True, default_value= 'Select Term', k="-termSelectionIns-")
    inslayout = [[sg.Text('Class Term:', size=(13,1)), termLstInsert],
              [sg.Text('Class Number:', size=(13,1)), sg.Input(key='-classNumIn-', size=(20,1))], 
              [sg.Text('Class Name:', size=(13,1)), sg.Input(key='-classNameIn-', size=(20,1))],
              [sg.Button('Insert', image_data=image_data, image_size= (35,9))]]   
    return sg.Window('Insert Class', inslayout, finalize=True)

def gradeWindow():
    
    return sg.Window('Insert Grade', grdlayout, finalize=True)



# Sets menubar for homeWindow
menuBar = [['Insert', ['Class', 'Grade'],],]
# Sets term selection drop down for homeWindow
termLstHome = sg.Combo(termVals, enable_events=True,  readonly=True, default_value= 'Select Term', k="-termSelectionHome-")
# Sets home layout
homeLayout = [
    [sg.Menu(menuBar)],
    [termLstHome, sg.Button('Search', image_data=image_data, image_size= (35,9))],
    [sg.HorizontalSeparator()],
    [sg.Text(key='-TERM-')],
    [sg.Text(key='-CLASS1-')],
    [sg.Text(key='-CLASS2-')],
    [sg.Text(key='-CLASS3-')],
    [sg.Text(key='-CLASS4-')],
    [sg.Text(key='-CLASS5-')]
    ]

# Starts window

homeWindow = sg.Window('Grade Book', homeLayout, size=(500,250), finalize=True)
insertPopUp = None
gradePopUp = None

while True:
    window, event, values=sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()
        if window == insertPopUp:
            insertPopUp = None
        elif window == homeWindow:
            break
    elif event == 'Search':
        if values['-termSelectionHome-'] != "Select Term":
            termCall(homeWindow, (values["-termSelectionHome-"]))
    elif event == 'Class' and not insertPopUp:
        insertPopUp = insertWindow()
    elif event == 'Grade' and not gradePopUp:
        gradeWindow = gradeWindow()
    elif event == 'Insert':
        if values['-classNumIn-'] != "" and values['-classNameIn-'] != "" and values['-termSelectionIns-'] != "Select Term":
            txt = values['-termSelectionIns-'].split(" ")
            database.addClass(values['-classNumIn-'], values['-classNameIn-'], txt[1], txt[0])
window.close()

# [sg.Menu(menuBar,)],
#     [termLst, sg.Button('Search', image_data=image_data, image_size= (35,9))],
#     [sg.HorizontalSeparator()],
#     [sg.Text(key='-TERM-')],