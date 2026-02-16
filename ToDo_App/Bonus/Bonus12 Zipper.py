import FreeSimpleGUI as Sg
from ZipCreator import make_archive

label1 =Sg.Text("Select File to Compress")
label2 =Sg.Text("Select Destination Folder")
input_box1 = Sg.InputText(tooltip = "Select File")
input_box2 = Sg.InputText(tooltip = "Destination Folder")
add_button1 =  Sg.FilesBrowse("Choose",key = "Files")
add_button2 =  Sg.FolderBrowse("Choose",key = "Folder")
compress_button = Sg.Button("Compress")
output_label = Sg.Text("",key="output",text_color="green")

window = Sg.Window("File Zipper"
                   ,layout= [[label1,input_box1,add_button1],
                             [label2,input_box2,add_button2],
                             [compress_button,output_label]])

while True:
    event,values = window.read()
    print(event,values)
    filepaths= values["Files"].split(";")
    folder = values["Folder"]
    make_archive(filepaths,folder)
    window["output"].update(value="compression completed")

window.close()