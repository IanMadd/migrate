import os
from pathlib import Path
from . import frontmatter

def readFiles(directory, output_dirs):

  filesList = os.listdir(directory)
  n = 0

  for file in filesList:
    fileWithPath = directory / file
    if os.path.isdir(fileWithPath) or file == ".DS_Store":
      continue
    print(file)
    with open(fileWithPath) as fileObject:
      fileText = fileObject.read()

    frontmatter.fixFrontmatter(fileText)

    n+=1
    if n > 0:
      break
    print(n)

def outputFile(directory, file):
  fileWithPath = Path(directory / file)

  with open(fileWithPath, 'w') as fileObject:
    fileObject.write(fileText)
