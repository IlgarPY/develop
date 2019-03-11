#importing modules
import os
import PyPDF2
import re

#defining the direction where pdf files (to be merged) are located
startDir = "/Users/ihuseynov/Documents"
os.chdir(startDir)



fileList=os.listdir(startDir)
fileList.sort()



#A. Zuordnung dr Lehrbriefe


def allocatePdfToTopic(list, item):
    topicListOfPdfs=[]
    for i in range(0,150):
        for file in list:
            iStr=str(i)
            if os.path.splitext(file)[1].upper()==".PDF":
                fileSplited=file.split(" ")
                try:
                    if (fileSplited[0] == item and fileSplited[1]==iStr+".pdf"):
                        topicListOfPdfs.append(file)
                except IndexError:
                    print("ups")
    merger(topicListOfPdfs, item)


def merger(list, item):
    output = PyPDF2.PdfFileWriter()
    for i in list:
        print(i)
        try:
            if os.path.splitext(i)[1].upper()==".PDF":
                pdfDocument=os.path.join(startDir, i)
                input1 =PyPDF2.PdfFileReader(pdfDocument)
                for page in range(input1.getNumPages()):
                    output.addPage(input1.getPage(int(page)))
                outputStream=open("MynewOutput"+item+".pdf", "wb")
                output.write(outputStream)
                outputStream.close()
        except TypeError:
            print("TypeError")


def createListofTopics(list):
    global listOfTopics
    listOfTopics=[]
    for file in list:
        if os.path.splitext(file)[1].upper()==".PDF":
            fileSplited=file.split(" ")
            if fileSplited[0] not in listOfTopics:
                listOfTopics.append(fileSplited[0])
    return listOfTopics

def merge(list):
    print("enter topic")
    eingabe = input()
    allocatePdfToTopic(list, eingabe)
    print("merged finalised")

createListofTopics(fileList)
print(listOfTopics)

for topic in listOfTopics:
    allocatePdfToTopic(fileList, topic)

#merge(fileList)
