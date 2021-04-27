import time
import pyautogui as gui
from datetime import date

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
gui.moveTo(901,494, duration=2)
gui.doubleClick(901,494)

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
gui.moveTo(890,306, duration=2)
gui.doubleClick(890,306)

# Choose "April 2021" folder and click on it
gui.moveTo(869,305, duration=2)
gui.doubleClick(869,305)

# Right-click and create new folder of today's date
gui.moveTo(829,540, duration=2)
gui.rightClick(829,540)

# "New" button
gui.moveTo(1095,746, duration=2)
gui.click(1095,746)

# "Folder" button
gui.moveTo(1207,753, duration=2)
gui.doubleClick(1207,753)

# Write today's date in the folder name
gui.typewrite(foldername)
gui.press('enter')

# Enter to this folder
gui.moveTo(861,538, duration=2)
gui.doubleClick(861,538)

# Save backup
gui.moveTo(1181,606, duration=2)
gui.doubleClick(1181,606)

