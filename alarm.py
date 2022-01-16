# Simple repeating alarm
# To run this file: python alarm.py

from tkinter import Message
import PySimpleGUI as sg
from datetime import datetime, time, timedelta


class TimeLeft():
    def __init__(self, tot_seconds) -> None:
        self.hours = int(max(0, tot_seconds//3600))
        self.minutes = int(max(0, (tot_seconds - (self.hours * 3600))//60))
        self.seconds = int(max(0, (tot_seconds - (self.hours * 3600) - (self.minutes * 60))))


time_now = datetime.now()
last_reset = datetime.now()
interval = timedelta(minutes=120)
time_left_obj = TimeLeft((interval - (time_now - last_reset)).seconds)
time_left = time(hour=time_left_obj.hours, minute=time_left_obj.minutes, second=time_left_obj.seconds)
water_counter = 0
time_layout = [
    [sg.Text("Time to next glass of water:", font="Arial 24")],
    [sg.Text(time_left.strftime("%H:%M:%S"), key="time", font="Arial 24")],
    [sg.Text("", key="alarm", font="Arial 24")],
    [sg.Button('I am drinking water!', key="reset")],
    [sg.Text("Water glasses drinked today: {}".format(water_counter), key="water", font="Arial 24")],
    [
        sg.Text("Time between water glasses: {} minutes".format(interval.seconds//60), key="interval"),
        sg.Button("Change interval", key="change_interval")
    ],
    [sg.Button('Exit')]
]
window = sg.Window("Time", time_layout)

while True:
    event, values = window.read(timeout=10)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == "reset":
        last_reset = datetime.now()
        water_counter += 1
    time_now = datetime.now()
    time_left_obj = TimeLeft((interval - (time_now - last_reset)).seconds)
    time_left = time(hour=time_left_obj.hours, minute=time_left_obj.minutes, second=time_left_obj.seconds)
    window["time"].update(time_left.strftime("%H:%M:%S"))
    window["water"].update("Water drinked today: {}".format(water_counter))
    if time_now - last_reset > interval:
        window["alarm"].update("DRINK WATER!!!")
    else:
        window["alarm"].update("")
    if event == "change_interval":
        interval_input = sg.PopupGetText(message="Insert new interval in minutes (min: 1, max: 1439")
        try:
            interval = timedelta(minutes=max(1, int(interval_input)))
            window["interval"].update("Time between water glasses: {} minutes".format(interval.seconds//60))
        except:
            sg.PopupError("Invalid Input!\nPlease only use digits\nInput a number between 1 and 1439.")

window.close()
