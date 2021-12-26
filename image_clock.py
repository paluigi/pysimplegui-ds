import PySimpleGUIQt as sg
import requests
from PIL import Image
import io
from datetime import datetime

cat_bytes = requests.get("https://placekitten.com/200/300")
cat_image = Image.open(io.BytesIO(cat_bytes.content))
cat_png = io.BytesIO()
cat_image.save(cat_png, format="PNG")
cat_display = cat_png.getvalue()
time_text = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

layout = [
    [sg.Text(time_text, key="time", font="Arial 24")],
    [sg.Image(data=cat_display)],
    [sg.Button('Exit')]
]
window = sg.Window("Clock with cat image", layout)

while True:
    event, values = window.read(timeout=10)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    new_time_text = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    window["time"].update(new_time_text)

window.close()
