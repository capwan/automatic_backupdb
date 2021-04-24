import time
import pyautogui as gui
from datetime import date

gui.PAUSE = 2
gui.FAILSAFE = False

today = date.today()

foldername = date.today().strftime('%d.%m.%y')

# Moving mouse to "Attendance Management Program" & click
gui.moveTo(80,874, duration=2)
gui.click(80,874)

# Moving mouse to "backup database" and click to button
gui.moveTo(88,186, duration=2)
gui.click(88,186)

# Choose "This PC"
gui.moveTo(580,410, duration=2)
gui.click(580,410)

# Scroll down to devices and drives
gui.moveTo(1066,298, duration=2)
gui.scroll(-250)

# Choose "D" disk and click on it
gui.moveTo(737,432, duration=2)
gui.doubleClick(737,432)

# Choose "NEW" folder and click on it
gui.moveTo(717,263, duration=2)
gui.doubleClick(717,263)

# Choose "CARD_READER_CURRENT" folder and click on it
gui.moveTo(712,256, duration=2)
gui.doubleClick(712,256)

# Choose "CURRENT_WORK" folder and click on it
gui.moveTo(743,263, duration=2)
gui.doubleClick(743,263)

# Choose "CR backups" folder and click on it
gui.moveTo(725,256, duration=2)
gui.doubleClick(725,256)

# Choose "April 2021" folder and click on it
gui.moveTo(720,267, duration=2)
gui.doubleClick(720,267)

# Right-click and create new folder of today's date
gui.moveTo(662,274, duration=2)
gui.rightClick(662,274)

# "New" button
gui.moveTo(888,573, duration=2)
gui.click(888,573)

# "Folder" button
gui.moveTo(1030,577, duration=2)
gui.doubleClick(1030,577)

# Write today's date in the folder name
gui.typewrite(foldername)

# Enter to this folder
gui.moveTo(755,266, duration=2)
gui.doubleClick(755,266)

# Save backup
gui.moveTo(1028,528, duration=2)
gui.click(1028,528)

