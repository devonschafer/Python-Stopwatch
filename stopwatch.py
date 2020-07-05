from guizero import *
import time
import datetime
import os
import glob
from time import sleep, gmtime, strftime, localtime
import math

size = 20
font = 'Helvetica'
green = 0, 200, 0
blue = 0, 0, 255
orange = 255, 187, 0
grey = 70, 70, 70
dark_grey = 30, 30, 30
white = 255, 255, 240
width = 430
height = 550

def button_boolean():
    if start_end_button.text == 'start':
        start_end_button.text = 'stop'
    elif start_end_button.text == 'resume':
        start_end_button.text = 'stop'
        pause_button.text = 'pause'
    elif start_end_button.text == 'stop':
        start_end_button.text = 'start'

def start():
    if start_end_button.text == 'stop':
        sec_text.value = int(sec_text.value) + 1
        if sec_text.value == str(60):
            sec_text.value = 0
            min_text.value = int(min_text.value) + 1
            if min_text.value == str(60):
                min_text.value = 0
                hour_text.value = int(hour_text.value) + 1
    elif start_end_button.text == 'start':
        sec_text.value = 0
        min_text.value = 0
        hour_text.value = 0

def lap():
    s = sec_text.value
    m = min_text.value
    h = hour_text.value
    l = len(lap_times.items) + 1
    lap_times.append('Lap %s: %s:%s:%s' % (l, h, m, s))
    lap_button.text = 'lap %s' % (l + 1)
            
def reset():
    if pause_button.text == 'pause':
        pause_button.text = 'reset'
        start_end_button.text = 'resume'
    elif pause_button.text == 'reset':
        pause_button.text = 'pause'
        lap_times.clear()
        lap_button.text='lap'
        start_end_button.text = 'start'
    

app = App(title='Stopwatch', width=width, height=height, layout='grid', bg=grey)

box1 = Box(app, layout='grid', grid=[0,0])
box2 = Box(app, layout='grid', grid=[0,1])
box3 = Box(app, layout='grid', grid=[0,2])

hour_text = Text(box1, text='', size=80, grid=[0,0], color=blue)

colonl = Text(box1, text=':', size=50, grid=[2,0], color=blue)

min_text = Text(box1, text='0', size=80, grid=[3,0], color=blue)

colonr = Text(box1, text=':', size=50, grid=[5,0], color=blue)

sec_text = Text(box1, text='0', size=80, grid=[6,0], color=blue)
sec_text.repeat(1000, start)

start_end_button = PushButton(box2, command=button_boolean, text='start', padx=50, pady=10, grid=[0,0])
start_end_button.width=3
start_end_button.height=2
start_end_button.text_color=white
start_end_button.bg=dark_grey

lap_button = PushButton(box2, command=lap, text='lap', padx=60, pady=10, grid=[1,0])
lap_button.width=3
lap_button.height=2
lap_button.text_color=white
lap_button.bg=dark_grey

pause_button = PushButton(box2, command=reset, text='pause', padx=60, pady=10, grid=[2,0])
pause_button.width=3
pause_button.height=2
pause_button.text_color=white
pause_button.bg=dark_grey

lap_times = ListBox(box2, items=[], width=150, height=380, grid=[1,1])
lap_times.bg=white
lap_times.text_font='Helvetica'
lap_times.text_size=12
lap_times.text_color=green








app.display()
