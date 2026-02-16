import FreeSimpleGUI as sg
from zip_extractor import extract_archive

sg.theme('Black')

label1 = sg.Text('Select Archive')
input1 = sg.Input()
label2 = sg.Text('Select Destination')
input2 = sg.Input()
choose_button = sg.FileBrowse('Choose',key= 'archive')
choose_button2 = sg.FolderBrowse('Destination',key='folder')

extract_button = sg.Button('Extract',key='Extract')
output_label = sg.Text('',key='output',text_color='green')
exit_button = sg.Button('Exit',key='Exit')

window = sg.Window("Archive Extractor",
                   layout=[[label1,input1,choose_button],
                   [label2,input2,choose_button2],
                   [extract_button,output_label],
                           [exit_button]])


while True:
    event, values = window.read()

    match event:
        case "Extract":
            archive_path = values['archive']
            destination_directory = values['folder']
            extract_archive(archive_path, destination_directory)
            window["output"].update(value='Extraction Completed')
        case "Exit":
            break
window.close()
