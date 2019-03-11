import pyautogui
import time

def clickOnNextButton(pos1 = 1029, pos2 = 109):
    pyautogui.click(pos1, pos2, clicks=2)
    time.sleep(.5)

def saveLeftPage(pageNumber, timeSleep):
    # GO TO PDF Button
    pdfButtonPosX, pdfButtonPosY = (585, 230)
    time.sleep(timeSleep)

    # Click on pdfButton
    pyautogui.click(pdfButtonPosX, pdfButtonPosY, clicks=1)
    time.sleep(timeSleep)

    # Click on 'Drucken' Button
    druckenButtonPosX, druckenButtonPosY = (966, 319)
    pyautogui.click(druckenButtonPosX, druckenButtonPosY, clicks=1)
    time.sleep(timeSleep)

    # Click on click on 'save' button
    saveButtonX, saveButtonY = (805, 186)
    pyautogui.click(saveButtonX, saveButtonY, clicks=1)
    time.sleep(2)

    # Change name of file
    testName = pageNumber
    saveAsPosX, saveAsPosY = (960, 119)
    pyautogui.click(saveAsPosX, saveAsPosY, clicks=1)
    pyautogui.typewrite(testName)
    time.sleep(timeSleep)

    # Click save button
    saveButtonX, saveButtonY = (1208, 663)
    pyautogui.click(saveButtonX, saveButtonY, clicks=1)
    time.sleep(timeSleep)

def saveRightPage(pageNumber, timeSleep):
    # GO TO PDF Button
    pdfButtonPosX, pdfButtonPosY = (585, 230)
    time.sleep(timeSleep)

    # Click on pdfButton
    pyautogui.click(pdfButtonPosX, pdfButtonPosY, clicks=1)
    time.sleep(timeSleep)

    # Click on "Rechte Seite"
    rechteSeiteX, rechteSeiteY = (610, 269)
    pyautogui.click(rechteSeiteX, rechteSeiteY, clicks=1)
    time.sleep(timeSleep)

    # Click on 'Drucken' Button
    druckenButtonPosX, druckenButtonPosY = (966, 319)
    pyautogui.click(druckenButtonPosX, druckenButtonPosY, clicks=1)
    time.sleep(timeSleep)

    # Click on click on 'save' button
    saveButtonX, saveButtonY = (805, 186)
    pyautogui.click(saveButtonX, saveButtonY, clicks=1)
    time.sleep(2)

    # Change name of file
    testName = pageNumber
    saveAsPosX, saveAsPosY = (960, 119)
    pyautogui.click(saveAsPosX, saveAsPosY, clicks=1)
    pyautogui.typewrite(testName)
    time.sleep(timeSleep)

    # Click save button
    saveButtonX, saveButtonY = (1208, 663)
    pyautogui.click(saveButtonX, saveButtonY, clicks=1)
    time.sleep(timeSleep)


globalCounter = 1

for pageNum in range(50):
    print(globalCounter)

    
    clickOnNextButton()


    saveLeftPage(" " + str(globalCounter), timeSleep = 1)

    saveRightPage(" " + str(globalCounter  + 1), timeSleep = 1)


    globalCounter = globalCounter + 2


