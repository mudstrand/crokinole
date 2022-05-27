from tkinter import *

redCount5 = 0
redCount10 = 0
redCount15 = 0
redCount20 = 0

blueCount5 = 0
blueCount10 = 0
blueCount15 = 0
blueCount20 = 0

scoreText = "0"
scoreColor = "black"

redButtonText5 = "Five"
redButtonText10 = "Ten"
redButtonText15 = "Fifteen"
redButtonText20 = "Twenty"

root = Tk()
root.geometry('450x300')
root.title("Crokinole Scorer")

def resetClick():
    global redCount5, redCount10, redCount15, redCount20
    global blueCount5, blueCount10, blueCount15, blueCount20

    print("reseting crokinole scorer")
    redCount5 = 0
    redCount10 = 0
    redCount15 = 0
    redCount20 = 0
    blueCount5 = 0
    blueCount10 = 0
    blueCount15 = 0
    blueCount20 = 0
    redButtonTextUpdate5()
    redButtonTextUpdate10()
    redButtonTextUpdate15()
    redButtonTextUpdate20()
    blueButtonTextUpdate5()
    blueButtonTextUpdate10()
    blueButtonTextUpdate15()
    blueButtonTextUpdate20()
    setScoreText()


def redClick5():
    global redCount5
    redCount5 = redCount5 + 1
    redButtonTextUpdate5()
    setScoreText()

def redClick10():
    global redCount10
    redCount10 = redCount10 + 1
    redButtonTextUpdate10()
    setScoreText()

def redClick15():
    global redCount15
    redCount15 = redCount15 + 1
    redButtonTextUpdate15()
    setScoreText()

def redClick20():
    global redCount20
    redCount20 = redCount20 + 1
    redButtonTextUpdate20()
    setScoreText()

def blueClick5():
    global blueCount5
    blueCount5 = blueCount5 + 1
    blueButtonTextUpdate5()
    setScoreText()

def blueClick10():
    global blueCount10
    blueCount10 = blueCount10 + 1
    blueButtonTextUpdate10()
    setScoreText()

def blueClick15():
    global blueCount15
    blueCount15 = blueCount15 + 1
    blueButtonTextUpdate15()
    setScoreText()

def blueClick20():
    global blueCount20
    blueCount20 = blueCount20 + 1
    blueButtonTextUpdate20()
    setScoreText()

def setScoreText():
    global scoreText, scoreColor
    redScore = (redCount5 * 5) + (redCount10 * 10) + (redCount15 * 15) + (redCount20 * 20)
    blueScore = (blueCount5 * 5) + (blueCount10 * 10) + (blueCount15 * 15) + (blueCount20 * 20)
    if redScore > blueScore:
        scoreColor = "red"
        scoreText = redScore - blueScore
    elif blueScore > redScore:
        scoreColor = "blue"
        scoreText = blueScore - redScore
    else:
        scoreColor = "black"
        scoreText = redScore - blueScore

    updateScoreDisplay()

def updateScoreDisplay():
    global scoreText
    # print(f'scoreTest: {scoreText}')
    if scoreColor == 'red':
        scoreTextLabel.config(text=scoreText, fg='red')
    elif scoreColor == 'blue':
        scoreTextLabel.config(text=scoreText, fg='blue')
    elif scoreColor == 'black':
        scoreTextLabel.config(text=scoreText, fg='black')

def redButtonTextUpdate5():
    global redButtonText5
    if redCount5:
        redButtonText5 = f'Five ({redCount5})'
    else:
        redButtonText5 = 'Five'
    redButton5.config(text=redButtonText5)

def redButtonTextUpdate10():
    global redButtonText10
    if redCount10:
        redButtonText10 = f'Ten ({redCount10})'
    else:
        redButtonText10 = 'Ten'
    redButton10.config(text=redButtonText10)

def redButtonTextUpdate15():
    global redButtonText15
    if redCount15:
        redButtonText15 = f'Fifteen ({redCount15})'
    else:
        redButtonText15 = 'Fifteen'
    redButton15.config(text=redButtonText15)

def redButtonTextUpdate20():
    global redButtonText20
    if redCount20:
        redButtonText20 = f'Twenty ({redCount20})'
    else:
        redButtonText20 = 'Twenty'
    redButton20.config(text=redButtonText20)

def blueButtonTextUpdate5():
    global blueButtonText5
    if blueCount5:
        blueButtonText5 = f'Five ({blueCount5})'
    else:
        blueButtonText5 = 'Five'
    blueButton5.config(text=blueButtonText5)

def blueButtonTextUpdate10():
    global blueButtonText10
    if blueCount10:
        blueButtonText10 = f'Ten ({blueCount10})'
    else:
        blueButtonText10 = 'Ten'
    blueButton10.config(text=blueButtonText10)

def blueButtonTextUpdate15():
    global blueButtonText15
    if blueCount15:
        blueButtonText15 = f'Fifteen ({blueCount15})'
    else:
        blueButtonText15 = 'Fifteen'
    blueButton15.config(text=blueButtonText15)

def blueButtonTextUpdate20():
    global blueButtonText20
    if blueCount20:
        blueButtonText20 = f'Twenty ({blueCount20})'
    else:
        blueButtonText20 = 'Twenty'
    blueButton20.config(text=blueButtonText20)


redButton5 = Button(root, text="Five", command=redClick5, fg='red', font=('calibri', 14, 'bold'), width=10)
redButton10 = Button(root, text="Ten", command=redClick10, fg='red', font=('calibri', 14, 'bold'), width=10)
redButton15 = Button(root, text="Fifteen", command=redClick15, fg='red', font=('calibri', 14, 'bold'), width=10)
redButton20 = Button(root, text="Twenty", command=redClick20, fg='red', font=('calibri', 14, 'bold'), width=10)

redButton5.grid(row=3, column=0)
redButton10.grid(row=3, column=1)
redButton15.grid(row=3, column=2)
redButton20.grid(row=3, column=3)

blueButton5 = Button(root, text="Five", command=blueClick5, fg='blue', font=('calibri', 14, 'bold'), width=10)
blueButton10 = Button(root, text="Ten", command=blueClick10, fg='blue', font=('calibri', 14, 'bold'), width=10)
blueButton15 = Button(root, text="Fifteen", command=blueClick15, fg='blue', font=('calibri', 14, 'bold'), width=10)
blueButton20 = Button(root, text="Twenty", command=blueClick20, fg='blue', font=('calibri', 14, 'bold'), width=10)

blueButton5.grid(row=4, column=0)
blueButton10.grid(row=4, column=1)
blueButton15.grid(row=4, column=2)
blueButton20.grid(row=4, column=3)

scoreTextLabel = Label(root, text=scoreText, font=('calibri', 28))

resetButton = Button(root, text="Reset", command=resetClick, fg='black', font=('calibri', 14, 'bold'), width=10)

red5 = Button(root, text="5", command=redClick5, fg='red', font=('calibri', 14, 'bold'), width=10)
red10 = Button(root, text="10", command=redClick10, fg='red', font=('calibri', 14, 'bold'), width=10)
red15 = Button(root, text="15", command=redClick15, fg='red', font=('calibri', 14, 'bold'), width=10)
red20 = Button(root, text="20", command=redClick20, fg='red', font=('calibri', 14, 'bold'), width=10)

blue5 = Button(root, text="5", command=blueClick5, fg='blue', font=('calibri', 14, 'bold'), width=10)
blue10 = Button(root, text="10", command=blueClick10, fg='blue', font=('calibri', 14, 'bold'), width=10)
blue15 = Button(root, text="15", command=blueClick15, fg='blue', font=('calibri', 14, 'bold'), width=10)
blue20 = Button(root, text="20", command=blueClick20, fg='blue', font=('calibri', 14, 'bold'), width=10)

resetButton.grid(row=1, column=3)

scoreTextLabel.grid(row=1, column=0, columnspan=2, pady=10, sticky=W)

root.mainloop()