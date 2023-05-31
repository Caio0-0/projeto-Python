import PySimpleGUI as sg
tamanho = (6,3)
sg.theme('DarkTeal')
layout =[
    [sg.Text("Output")],
    [sg.Button("C",size=(tamanho)),sg.Button("ENTER",expand_x=True,size=(0,3)),sg.Button("+",size=(tamanho))],
    [sg.Button("7",size=(tamanho)),sg.Button("8",size=(tamanho)),sg.Button("9",size=(tamanho)),sg.Button("/",size=(tamanho))],
    [sg.Button("4",size=(tamanho)),sg.Button("5",size=(tamanho)),sg.Button("6",size=(tamanho)),sg.Button("X",size=(tamanho))],
    [sg.Button("1",size=(tamanho)),sg.Button("2",size=(tamanho)),sg.Button("3",size=(tamanho)),sg.Button("-",size=(tamanho))],
    [sg.Button("0",expand_x=True,size=(0,3)),sg.Button(".",size=(tamanho))]
]

window =sg.Window("Calculator",layout)


while True :
    event,value = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()

