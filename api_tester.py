# Little GUI application to test API endpoints
# And display API responses
# Run this with: python api_tester.py

import PySimpleGUIQt as sg
import requests
import json

action_list =["GET", "POST"]  # Also DELETE, PUT, and UPDATE could be added

layout = [
    [sg.Text("Endpoint"), sg.Input(size=(30, 1), key="endpoint", default_text="https://api.publicapis.org/random")],
    [sg.Text("Parameters"), sg.Input(size=(30, 1), key="params", default_text="\"auth\": \"null\"")],
    [sg.Text("Parameters need to be inserted this way: \"key1\": \"string\", \"key2\": 11, ...")],
    [
        sg.Text("Call type"),
        sg.Listbox(
            action_list, select_mode="LISTBOX_SELECT_MODE_SINGLE",
            auto_size_text=True, key="action")
    ],
    [sg.Text("call")],
    [sg.Text("", key="call")],
    [sg.Text("Response")],
    [sg.Text("", key="response_status")],
    [sg.Text("", key="response_content")],
    [sg.Button('OK'), sg.Button('Exit')]
]

window = sg.Window("API tester", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == "OK":
        if values.get("action") == ["GET"]:
            params = json.loads("{{{}}}".format(values.get("params")))
            result = requests.get(values.get("endpoint"), params=params)
            window["response_status"].update(result.status_code)
            window["response_content"].update(result.text)
            window["call"].update(result.url)

window.close()
