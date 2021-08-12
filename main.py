import time
import pyautogui as gui
from datetime import date
import tkinter as tk
from tkinter import Button

root = tk.Tk()
root.title("Automatic Backup Database") # program title
root.geometry('300x200') # size of program

btn = Button(root,
        text="Run",
        width=40, height=10,
        bg="white", fg="green",command = root.quit)


btn.pack(padx=100, pady=60)
root.mainloop()


gui.PAUSE = 2
gui.FAILSAFE = False

today = date.today()

foldername = date.today().strftime('%d.%m.%Y')

# Moving mouse to "Attendance Management Program" & click
gui.moveTo(81,1057, duration=2)
gui.click(81,1057)

# Moving mouse to "backup database" and click to button
gui.moveTo(74,186, duration=2)
gui.click(74,186)

# Choose "This PC"
gui.moveTo(724,446, duration=2)
gui.click(724,446)

# Scroll down to devices and drives
gui.moveTo(1231,309, duration=2)
gui.scroll(-250)

# Choose "D" disk and click on it
gui.moveTo(911,542, duration=2)
gui.doubleClick(911,542)

# Choose "NEW" folder and click on it
gui.moveTo(862,304, duration=2)
gui.doubleClick(862,304)

# Choose "CARD_READER_CURRENT" folder and click on it
gui.moveTo(885,303, duration=2)
gui.doubleClick(885,303)

# Choose "CURRENT_WORK" folder and click on it
gui.moveTo(870,299, duration=2)
gui.doubleClick(870,299)

# Choose "CR backups" folder and click on it
gui.moveTo(846,381, duration=2)
gui.doubleClick(846,381)

# Choose "August 2021" folder and click on it
gui.moveTo(851,322, duration=2)
gui.doubleClick(851,322)

# Create New folder
gui.moveTo(1121,256, duration=2)
gui.click(1121,256)

# Write today's date in the folder name
gui.typewrite(foldername)
gui.press('enter')

# Enter to this folder
gui.press('enter')

# Save backup
gui.moveTo(1193,609, duration=2)
gui.doubleClick(1193,609)
