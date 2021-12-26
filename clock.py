import PySimpleGUI as sg
import requests
from datetime import datetime
#from PIL import Image
import io
import time

#cat_bytes = requests.get("https://placekitten.com/200/300")
#cat_image = Image.open(io.BytesIO(cat_bytes.content))

#image_layout = [sg.Image("cat_image")]
#window = sg.Window("Image", image_layout)
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
