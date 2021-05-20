import os
from pathlib import Path


def openFile(fullFilePath):
  with open(fullFilePath) as fileObject:
    fileText = fileObject.read()

  return fileText

def outputFile(outputPath, fileText):
  with open(outputPath, 'w') as fileObject:
    fileObject.write(fileText)
