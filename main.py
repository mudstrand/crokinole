from cgitb import text
from tkinter import *
from tkinter.ttk import Separator
from turtle import width
from PIL import ImageTk, Image
import time
from time import strftime
import winsound
import threading
import time

blindLevels = ([100, 200], [200, 400], [300, 600], [500, 1000], [1000, 2000], [2000, 4000], [3000, 6000], [5000, 10000],
               [10000, 20000])
# blindLevels = ([100, 200], [200,400], [300,600], [500,1000])
blindTime = 15 * 60
blindLevel = 0
timerEnabled = False
clockText = "00:00"
blindLevelText = "Blind Level: %d" % (blindLevel + 1)

root = Tk()
root.geometry('450x300')
root.title("Tournament Time")


# root.iconbitmap("Cloudstrand.ico")

# my_img = ImageTk.PhotoImage(Image.open("Cloudstrand.png"))
# my_label = Label(image=my_img)
# my_label.grid(row=6, column=0)

def startClick():
    global timerEnabled
    timerEnabled = True


def pauseClick():
    global timerEnabled
    timerEnabled = False


def exitClick():
    print("thank you for using tournament poker timer")
    exit()


def resetClick():
    global t
    t = blindTime


def buzzer():
    global t
    t = blindTime
    print("buzzer tripped")
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)


def setClockText():
    global clockText
    # current = current_milli_time()
    current = current_seconds_time()
    elapsed = current - clockStart
    mins, secs = divmod(elapsed, 60)
    clockText = '{:02d}:{:02d}'.format(int(mins), int(secs))


def setBlindText():
    global blindText
    blinds = blindLevels[blindLevel]
    # print("blinds: %s" % blinds)
    smallBlind = blinds[0]
    bigBlind = blinds[1]
    blindText = "$" + str(smallBlind) + " / $" + str(bigBlind)


def setBlindLevelText():
    global blindLevelText
    if blindLevel + 1 >= len(blindLevels):
        blindLevelText = "Blind Level: %s%s" % ((blindLevel + 1), "*")
    else:
        blindLevelText = "Blind Level: %d" % (blindLevel + 1)


def updateBlindDisplay():
    global blindText, blindLevel
    # if (blindLevel < len(blindLevels)-1):
    #     blindLevel = blindLevel + 1
    print("blindLevel size: %d" % len(blindLevels))
    print("blindLevel: %d" % blindLevel)
    setBlindText()
    setBlindLevelText()
    blindLevelTextLabel.config(text=blindLevelText)
    blind_label.config(text=blindText)


def changeBlindLevel(amount):
    global blindLevel
    if amount > 0:
        if blindLevel + amount < len(blindLevels):
            blindLevel = blindLevel + amount
    elif amount < 0:
        if blindLevel + amount >= 0:
            blindLevel = blindLevel + amount


def plusClick():
    global blindLevel
    if blindLevel < len(blindLevels):
        print("moving up one blind level")
        changeBlindLevel(1)
        updateBlindDisplay()


def minusClick():
    global blindLevel
    if blindLevel >= 1:
        print("moving down one blind level")
        changeBlindLevel(-1)
        updateBlindDisplay()


def current_seconds_time():
    return round(time.time())


clockStart = current_seconds_time()
programNameLabel = Label(root, text="Tournament Poker Timer", font=('calibri', 20, 'bold'))
copyrightLabel = Label(root, text="Mark Udstrand (c) 2022", font=('calibri', 11))
clockTextLabel = Label(root, text=clockText, font=('calibri', 11))
blindLevelTextLabel = Label(root, text=blindLevelText, font=('calibri', 11))

startButton = Button(root, text="Start Timer", command=startClick, fg='blue', font=('calibri', 14, 'bold'), width=10)
pauseButton = Button(root, text="Pause Timer", command=pauseClick, fg='blue', font=('calibri', 14, 'bold'), width=10)
exitButton = Button(root, text="Exit", command=exitClick, fg='blue', font=('calibri', 14, 'bold'), width=10)
resetButton = Button(root, text="Reset", command=resetClick, fg='blue', font=('calibri', 14, 'bold'), width=10)
plusBlindLevelButton = Button(root, text="+", command=plusClick, font=('calibri', 10), width=1)
minusBlindLevelButton = Button(root, text="-", command=minusClick, font=('calibri', 10), width=1)

setBlindText()
blind_label = Label(root, font=('calibri', 30, 'bold'), text=blindText)
clock_label = Label(root, font=('calibri', 40, 'bold'),
                    background='white',
                    foreground='black')

programNameLabel.grid(row=0, column=0, columnspan=4, pady=10)
# myLabel2.grid(row=5, column=0, columnspan=5, sticky=W+E)

clock_label.grid(row=1, column=0, columnspan=4, pady=10, sticky=W)
blind_label.grid(row=1, column=1, columnspan=4, pady=10, sticky=E)

startButton.grid(row=2, column=0)
pauseButton.grid(row=2, column=1)
resetButton.grid(row=2, column=2)
exitButton.grid(row=2, column=3)

copyrightLabel.grid(row=3, column=0, columnspan=4, pady=10)
clockTextLabel.grid(row=3, column=0, columnspan=4, pady=10, sticky=E)
blindLevelTextLabel.grid(row=3, column=0, columnspan=4, pady=10, sticky=W)
plusBlindLevelButton.grid(row=3, column=0, pady=10, sticky=E)
minusBlindLevelButton.grid(row=3, column=1, pady=10, sticky=W)

t = blindTime


def timerLoop():
    global t, timerEnabled
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    clock_label.config(text=timer)
    clock_label.after(1000, timerLoop)
    setClockText()
    clockTextLabel.config(text=clockText)
    set
    if t <= 0:
        print("next blind level")
        th = threading.Thread(target=buzzer)
        th.start()
        changeBlindLevel(1)
        updateBlindDisplay()
    if timerEnabled:
        t = t - 1


timerLoop()
root.mainloop()
