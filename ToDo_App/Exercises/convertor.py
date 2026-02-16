import FreeSimpleGUI as Sg

label =Sg.Text("Converter")
label1 = Sg.Text("Enter Feet")
label2 = Sg.Text("Enter Inches")
input_box1 = Sg.InputText(key="feet")
input_box2 = Sg.InputText(key="Inches")
outcome = Sg.Text("")

Convert_button = Sg.Button("Convert")

window = Sg.Window("Convertor",
                   layout= [[label1,input_box1],[label2,input_box2],[Convert_button,outcome]])

feet =0
inches =0

while True:

    event,values = window.read()
    match event:
        case "Convert":
            inches = int(values["Inches"])
            feet = int(values["feet"])
            total_inches = inches + (feet*12)
            total_cm = total_inches * 2.54
            print(total_cm)
            total_m = total_cm / 100
            outcome.update(f"{total_m} m")









window.close()