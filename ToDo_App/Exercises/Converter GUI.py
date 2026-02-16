import FreeSimpleGUI as Sg

label1 =Sg.Text("Enter Feet")
input1 = Sg.Input("")
enterInches = Sg.Text("Enter Inches")
InchesInput = Sg.Input("")
Convert = Sg.Button("Convert")



window = Sg.Window("Convertor",[[label1,input1],[enterInches,InchesInput],[Convert]])
window.read()
window.close()