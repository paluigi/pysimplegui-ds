# Simple self updating clock that displays date and time
# To run this file: python clock.py

import PySimpleGUI as sg
from datetime import datetime

time_text = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
time_layout = [
    [sg.Text(time_text, key="time", font="Arial 24")],
    [sg.Button('Exit')]
]
window = sg.Window("Time", time_layout)

while True:
    event, values = window.read(timeout=10)
    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        break
    new_time_text = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    window["time"].update(new_time_text)

window.close()
