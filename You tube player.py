#MUSIC PLAYING INTERFACE
#The webbrowser module opens a web page in your default browser
import webbrowser
from tkinter import *

def open_youtube():
    url = "https://www.youtube.com/playlist?list=PLUCtMEAV4Ixv3VL9vPkeladPgZi7B3JOt"  # Replace with the specific video URL if needed
    webbrowser.open(url, new=1)

window = Tk()
window.title("Open YouTube")
window.geometry("300x100")

button = Button(text="Open YouTube", command=open_youtube)
button.pack()

window.mainloop()

#DAILY CHECKUP
#sends good morning text everyday at a specific time with a link to A-mazing
