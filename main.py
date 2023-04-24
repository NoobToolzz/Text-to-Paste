import os
import sys
import time
import requests
import webbrowser

from datetime import datetime
from pystyle import Center, Colorate, Colors, Write

__author__ = 'Bloody#6850' # Don't change this.

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    os.system('pause >nul')

def check_for_changes():
    if __author__ != '\u0042\u006c\u006f\u006f\u0064\u0079\u0023\u0036\u0038\u0035\u0030': # Checks if you changed the __author__ text field
        Write.Print("Bro stop skidding", Colors.red_to_yellow, interval=0.008)
        pause()
        exit

banner = """

╔╦╗┌─┐─┐ ┬┌┬┐  ┌┬┐┌─┐  ╔═╗┌─┐┌─┐┌┬┐┌─┐
 ║ ├┤ ┌┴┬┘ │    │ │ │  ╠═╝├─┤└─┐ │ ├┤ 
 ╩ └─┘┴ └─ ┴    ┴ └─┘  ╩  ┴ ┴└─┘ ┴ └─┘
                                          
"""

now = datetime.now()
timenow = now.strftime("%H:%M:%S")

cls()
check_for_changes()
print(Colorate.Horizontal(Colors.purple_to_blue, Center.Center(banner)))
text = Write.Input(f"[{timenow}] | Enter Text: ", Colors.purple_to_blue, interval=0.008).replace(" ", "%20")
# text = text.replace(" ", "%20")
time.sleep(2)


process = """
  _____                      __  _               
 / ___/__ ___  ___ _______ _/ /_(_)__  ___ _     
/ (_ / -_) _ \/ -_) __/ _ `/ __/ / _ \/ _ `/ _ _ 
\___/\__/_//_/\__/_/  \_,_/\__/_/_//_/\_, (_|_|_)
                                     /___/       
"""

process_done = """
   ______                           __           __
  / ____/__  ____  ___  _________ _/ /____  ____/ /
 / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ _ \/ __  / 
/ /_/ /  __/ / / /  __/ /  / /_/ / /_/  __/ /_/ /  
\____/\___/_/ /_/\___/_/   \__,_/\__/\___/\__,_/                                              

"""

cls()
print(Colorate.Horizontal(Colors.purple_to_blue, Center.Center(process)))
Write.Print(f'[{timenow}] | Checking Paste response...\n', Colors.green_to_blue, interval=0.008)

time.sleep(2)

# Generationg part
paste = requests.get("https://paste-pgpj.onrender.com") # Getting Paste status.
if paste.status_code == 200:
    Write.Print(f'[{timenow}] | Paste Response: 200 (OK)\n', Colors.green_to_blue, interval=0.008)
elif paste.status_code == 404:
    Write.Print(f'[{timenow}] | Paste Response: 404\n', Colors.red_to_blue, interval=0.008)
    Write.Print(f'[{timenow}] | Unable to generate\nPress any key to exit', Colors.red_to_yellow, interval=0.008)
    pause()
    exit

time.sleep(1)
Write.Print(f'[{timenow}] | Generating Paste . . .', Colors.purple_to_blue, interval=0.008)
time.sleep(2)
cls()

# Done
print(Colorate.Horizontal(Colors.purple_to_blue, Center.Center(process_done)))

paste_text = (f"https://paste-pgpj.onrender.com/?p={text}")
Write.Print(f"[{timenow}] | Generated!\nLink: {paste_text}\n", Colors.green_to_blue, interval=0.008)
Write.Print(f"[{timenow}] | Press any key to open in browser.", Colors.purple_to_blue, interval=0.008)
pause()

# If you press a key after that pause it will take 3 seconds to open the paste into the browser
cls()
Write.Print(f"[{timenow}] | Link: {paste_text}\n", Colors.green_to_blue, interval=0)
Write.Print(f"[{timenow}] | Opening in browser in 3 seconds...\r", Colors.rainbow, interval=0.008)
time.sleep(1)

# cls()
Write.Print(f"[{timenow}] | Opening in browser in 2 seconds...\r", Colors.rainbow, interval=0.008)
time.sleep(1)

# cls()
Write.Print(f"[{timenow}] | Opening in browser in 1 seconds...\n", Colors.rainbow, interval=0.008)
time.sleep(1)

webbrowser.open(paste_text)
Write.Print(f"[{timenow}] | Opened in browser!\nPress any key to exit . . .", Colors.green_to_blue, interval=0.008)
pause()

cls()    
Write.Print(f"[{timenow}] | Exiting . . .", Colors.red_to_blue, interval=0.008)
exit