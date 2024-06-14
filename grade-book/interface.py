import textwrap
import PySimpleGUI as sg
import database

# Set windows theme, image data for buttons, and termval for term dropdowns
sg.theme('DarkGrey4')
font = ('Courier New', 10)
sg.set_options(font=font)
image_data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\rIDATx\x9cc````\x00\x00\x00\x05\x00\x01\xa5\xf6E@\x00\x00\x00\x00IEND\xaeB`\x82'
termDropDwnVals = ['Select Term','Spring 2024', 'Summer 2024', 'Fall 2024', 'Spring 2025']



# Updates homeWindow display when "Search" button is pressed with Term slected
def termCall(window, term):
    splitTerm = term.split(" ")
    window['-term_hmWd-'].update("Term: " + splitTerm[0] + "\t" + "Year: " + splitTerm[1])
    window['-addBtn_hmWd-'].update(visible=True)
    window['-dltBtn_hmWd-'].update(visible=True)
    classArray = database.getClassArray(splitTerm[1], splitTerm[0])
    
    # Clear if called term is empty
    if not classArray:
        for i in range(1,8):
            target = '-class_' + str(i) + '_hmWd-'
            window[target].update(visible=False)
        return
    
    # Display classes in term
    i = 1
    for cl in classArray: # [0]=class_num, [1]=class_name, [2]=grade
        target = '-class_' + str(i) + '_hmWd-'
        if (cl[2]): 
            text = str(cl[0] + "    " + cl[1] + "    " + cl[2])
            w = 0
            for char in text:
                w = w + sg.Text.char_width_in_pixels(font='Courier 10', character=char)
            window[target].update(visible=True, image_data=image_data,  image_size=(w,8))
            window[target].update(text)
            window[target].Widget.configure(justify='left', height=8)
        else:
            text = str(cl[0] + "    " + cl[1])
            w = 0
            for char in text:
                w +=  sg.Text.char_width_in_pixels(font='Courier 10', character=char)
            window[target].update(visible=True, image_data=image_data,  image_size=(w,8))
            window[target].update(text)
            window[target].Widget.configure(justify='left', height=8)
        i +=1



def create_homeWd():
    # Sets term selection drop down for homeWindow
    termLstHome = sg.Combo(termDropDwnVals, default_value= 'Select Term', k="-termSlc_hmWd-", enable_events=True,  readonly=True)
    # Sets home layout
    layout = [
        [termLstHome, sg.Button('Search', k='-termSrch_hmWd-', image_data=image_data, image_size=(35,9))],
        [sg.HorizontalSeparator()],
        [sg.Text(key='-term_hmWd-'), sg.Push(), sg.Button(image_filename='plusSign.png', k='-addBtn_hmWd-',visible=False, image_subsample=5), sg.Button(image_filename='minusSign.png', k='-dltBtn_hmWd-',visible=False, image_subsample=5)],
        [sg.Button(key='-class_1_hmWd-', image_data=image_data, button_color=('#FCFCFC', '#52524E'), border_width=0, visible=False, image_size=(250,8), mouseover_colors=('#9A9B94', '#52524E'))],
        [sg.Button(key='-class_2_hmWd-', image_data=image_data, button_color=('#FCFCFC', '#52524E'), border_width=0, visible=False, image_size=(250,8), mouseover_colors=('#9A9B94', '#52524E'))],
        [sg.Button(key='-class_3_hmWd-', image_data=image_data, button_color=('#FCFCFC', '#52524E'), border_width=0, visible=False, image_size=(250,8), mouseover_colors=('#9A9B94', '#52524E'))],
        [sg.Button(key='-class_4_hmWd-', image_data=image_data, button_color=('#FCFCFC', '#52524E'), border_width=0, visible=False, image_size=(250,8), mouseover_colors=('#9A9B94', '#52524E'))],
        [sg.Button(key='-class_5_hmWd-', image_data=image_data, button_color=('#FCFCFC', '#52524E'), border_width=0, visible=False, image_size=(250,8), mouseover_colors=('#9A9B94', '#52524E'))],
        [sg.Button(key='-class_6_hmWd-', image_data=image_data, button_color=('#FCFCFC', '#52524E'), border_width=0, visible=False, image_size=(250,8), mouseover_colors=('#9A9B94', '#52524E'))],
        [sg.Button(key='-class_7_hmWd-', image_data=image_data, button_color=('#FCFCFC', '#52524E'), border_width=0, visible=False, image_size=(250,8), mouseover_colors=('#9A9B94', '#52524E'))],    
        ]
    return sg.Window('Grade Book', layout, finalize=True)

def create_addWd(window, term):
    splitTerm = term.split(" ")
    layout = [
        [sg.Text("Class Name:"), sg.Input(enable_events=True, key='-className_addWd-', size=(35,8), expand_x=True)],
        [sg.Text("Class Number:"), sg.Input(enable_events=True, key='-classNum_addWd-', size=(10,8), expand_x=True)],
        [sg.Text("Final Grade (if applicable):"), sg.Input(enable_events=True, key='-finalGrade_addWd-', size=(10,8), expand_x=True)],
        [sg.HorizontalSeparator()],
        [sg.Text("Assignment Group:"), sg.Push(), sg.Text("Weight:", pad=(27,3))],
        [sg.Input(enable_events=True, key='-newCat_1_addWd-', size=(25,1), expand_x=True), sg.Push(), sg.Input(enable_events=True, key='-newWt_1_addWd-', size=(8,1), pad=(0,3)), sg.Text("%", font=('Courier New', 10), pad=(2,3))],
        [sg.Input(enable_events=True, key='-newCat_2_addWd-', size=(25,1), expand_x=True), sg.Push(), sg.Input(enable_events=True, key='-newWt_2_addWd-', size=(8,1), pad=(0,3)), sg.Text("%", font=('Courier New', 10), pad=(2,3))],
        [sg.Input(enable_events=True, key='-newCat_3_addWd-', size=(25,1), expand_x=True, visible=False), sg.Input(enable_events=True, key='-newWt_3_addWd-', size=(8,1), pad=(0,3), visible=False), sg.Text("%", font=('Courier New', 10), visible=False, key='-percent_3_addWd', pad=(2,3))],
        [sg.Input(enable_events=True, key='-newCat_4_addWd-', size=(25,1), expand_x=True, visible=False), sg.Input(enable_events=True, key='-newWt_4_addWd-', size=(8,1), pad=(0,3), visible=False), sg.Text("%", font=('Courier New', 10), visible=False, key='-percent_4_addWd', pad=(2,3))],
        [sg.Input(enable_events=True, key='-newCat_5_addWd-', size=(25,1), expand_x=True, visible=False), sg.Input(enable_events=True, key='-newWt_5_addWd-', size=(8,1), pad=(0,3), visible=False), sg.Text("%", font=('Courier New', 10), visible=False, key='-percent_5_addWd', pad=(2,3))],
        [sg.Input(enable_events=True, key='-newCat_6_addWd-', size=(25,1), expand_x=True, visible=False), sg.Input(enable_events=True, key='-newWt_6_addWd-', size=(8,1), pad=(0,3), visible=False), sg.Text("%", font=('Courier New', 10), visible=False, key='-percent_6_addWd', pad=(2,3))],
        [sg.Input(enable_events=True, key='-newCat_7_addWd-', size=(25,1), expand_x=True, visible=False), sg.Input(enable_events=True, key='-newWt_7_addWd-', size=(8,1), pad=(0,3), visible=False), sg.Text("%", font=('Courier New', 10), visible=False, key='-percent_7_addWd', pad=(2,3))],
        [sg.Input(enable_events=True, key='-newCat_8_addWd-', size=(25,1), expand_x=True, visible=False), sg.Input(enable_events=True, key='-newWt_8_addWd-', size=(8,1), pad=(0,3), visible=False), sg.Text("%", font=('Courier New', 10), visible=False, key='-percent_8_addWd', pad=(2,3))],
        [sg.Button("Insert Class", k='-addBtn_addWd-', image_data=image_data, image_size=(80,9)), sg.Push(), sg.Button("Add Group", k='-addGroup_addWd-', image_data=image_data, image_size=(55,9))]
        ]
    return sg.Window("Add Class: " + splitTerm[0] + " " + splitTerm[1], layout, finalize=True)

# Starts window
homeWd = create_homeWd() 
addWd = None
editWd = None
deleteWd = None

while True:
    window, event, values = sg.read_all_windows()

    if window == sg.WIN_CLOSED:
        break
    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()
        if window == addWd:
            addWd = None
        elif window == editWd:
            editWd = None
        elif window == deleteWd:
            deleteWd = None
    elif event == '-termSrch_hmWd-':
        if values['-termSlc_hmWd-'] != "Select Term":
            termCall(homeWd, (values['-termSlc_hmWd-']))     
    elif event == '-addBtn_hmWd-':
        print (addWd)
        if not addWd:
            addWd = create_addWd(addWd, (values['-termSlc_hmWd-']))
            addWd.move(homeWd.current_location()[0]+20, homeWd.current_location()[1]+20)
    elif event == '-addGroup_addWd-':
        i = 3
        window[-]
    #     if values['-newCat_addWd-'] != "" and values['-newWt_addWd-'] != "":
    #         txt=window['-frameText_addWd-'].get() + values['-newCat_addWd-'] + ":" + values['-newWt_addWd-'] + '%\t'
    #         size = (window['-catFrame_addWd-'].get_size()[0] - 30) / sg.Text.char_width_in_pixels(font = 'Courier 10', character='A')
    #         txt = textwrap.TextWrapper(width=size, break_long_words=False, replace_whitespace=False, drop_whitespace=False).fill(text=txt)
    #         txt = textwrap.dedent(txt)
    #         window['-frameText_addWd-'].update(txt)
            
    #         print(txt)

window.close()

#values['-Text1-'] + values['-newCat_addWd-']