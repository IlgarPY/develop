import pyautogui
import time

def clickOnNextButton(pos1 = 845, pos2 = 151):
    pyautogui.click(pos1, pos2, clicks=2)
    time.sleep(.5)

def saveRightPage(pageNumber, timeSleep):
    # GO TO PDF Button
    pdfButtonPosX, pdfButtonPosY = (25, 273)
    time.sleep(timeSleep)

    # Click on pdfButton
    pyautogui.click(pdfButtonPosX, pdfButtonPosY, clicks=2)
    time.sleep(timeSleep)

globalCounter = 1

for pageNum in range(2):
    print(globalCounter)

    saveRightPage(" " + str(globalCounter), timeSleep = 2)

    clickOnNextButton()

    saveLeftPage(" " + str(globalCounter +1), timeSleep = 2)

    saveRightPage(" " + str(globalCounter + 2), timeSleep = 2)

    globalCounter = globalCounter + 2
