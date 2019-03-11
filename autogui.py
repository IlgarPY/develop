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

    # Click on rechte Seite
    rechteSeiteX, rechteSeiteY = (95, 313)
    pyautogui.click(rechteSeiteX, rechteSeiteY, clicks=1)
    time.sleep(timeSleep)

    # Click on 'Drucken' Button
    druckenButtonPosX, druckenButtonPosY = (403, 354)
    pyautogui.click(druckenButtonPosX, druckenButtonPosY, clicks=1)
    time.sleep(timeSleep)

    # Click on click on 'save' button
    saveButtonX, saveButtonY = (490, 213)
    pyautogui.click(saveButtonX, saveButtonY, clicks=1)
    time.sleep(2)

    # Change name of file
    testName = pageNumber
    saveAsPosX, saveAsPosY = (716, 127)
    pyautogui.click(saveAsPosX, saveAsPosY, clicks=1)
    pyautogui.typewrite(testName)
    time.sleep(timeSleep)

    # Click save button
    saveButtonX, saveButtonY = (869, 284)
    pyautogui.click(saveButtonX, saveButtonY, clicks=1)
    time.sleep(timeSleep)


def saveLeftPage(pageNumber, timeSleep):
    # GO TO PDF Button
    pdfButtonPosX, pdfButtonPosY = (23, 273)
    time.sleep(timeSleep)

    # Click on pdfButton
    pyautogui.click(pdfButtonPosX, pdfButtonPosY, clicks=2)
    time.sleep(timeSleep)

    # Click on "linke Seite"
    linkeSeiteX, linkeSeiteY = (70, 259)
    pyautogui.click(linkeSeiteX, linkeSeiteY, clicks=1)
    time.sleep(timeSleep)

    # Click on 'Drucken' Button
    druckenButtonPosX, druckenButtonPosY = (403, 354)
    pyautogui.click(druckenButtonPosX, druckenButtonPosY, clicks=1)
    time.sleep(timeSleep)

    # Click on click on 'save' button
    saveButtonX, saveButtonY = (490, 213)
    pyautogui.click(saveButtonX, saveButtonY, clicks=1)
    time.sleep(2)

    # Change name of file
    testName = pageNumber
    saveAsPosX, saveAsPosY = (716, 127)
    pyautogui.click(saveAsPosX, saveAsPosY, clicks=1)
    pyautogui.typewrite(testName)
    time.sleep(timeSleep)

    # Click save button
    saveButtonX, saveButtonY = (869, 284)
    pyautogui.click(saveButtonX, saveButtonY, clicks=1)
    time.sleep(timeSleep)




globalCounter = 1

for pageNum in range(220):
    print(globalCounter)

    saveRightPage(" " + str(globalCounter), timeSleep = 2)

    clickOnNextButton()

    saveLeftPage(" " + str(globalCounter +1), timeSleep = 2)

    saveRightPage(" " + str(globalCounter + 2), timeSleep = 2)

    clickOnNextButton()

    saveLeftPage(" " + str(globalCounter +3), timeSleep = 2)

    globalCounter = globalCounter + 4
