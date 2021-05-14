from . import misc
import re

def mungeSyntaxBlock(text, start, end):
  syntaxText = text[start:end]
  regexParameters = r"^#+ Parameters"
  notHeadingNotNewline = r"^[^#|\n]"
  newLine = r"^\n"
  syntaxText = misc.removeSlash(syntaxText)

  textList = syntaxText.splitlines(True)

  foundParameters = False
  wrapLinesCount = 0
  for index, line in enumerate(textList):
    print(line)
    if foundParameters:
      regexParameter = r"^#+ (\w+)"
      substParameter = "`\\g<1>`"
      regexEmptyLine = r"^ *\n"
      regexNormalLine = r"^"
      substNewLine = ": "
      substWrapLine = "  "

      if re.search(regexParameter, line):
        line = re.sub(regexParameter, substParameter, line, 0, re.M)
        # print("this is the output: ")
        # print(output)
        # textList[index] = output
        # print(line)

        regexRequired = r"_\(required\)_"
        substRequired = "| `REQUIRED`"
        textList[index] = re.sub(regexRequired, substRequired, line, 0)

      else:
        if re.search(regexEmptyLine, line):
          wrapLinesCount = 0
        else:
          wrapLinesCount += 1

        if wrapLinesCount == 0:
          continue
        elif wrapLinesCount == 1:
          textList[index] = re.sub(regexNormalLine, substNewLine, line, 1, re.M)
        else:
          textList[index] = re.sub(regexNormalLine, substWrapLine, line, 1, re.M)

    if re.search(regexParameters, line):
      print("found parameters:")
      foundParameters = True

  syntaxText = "".join(textList)

  substParameters = "where:"
  syntaxText = re.sub(regexParameters, substParameters, syntaxText, 0, re.M)

  text = syntaxText[:start] + syntaxText + syntaxText[end:]
  return text

def openSyntaxBlock(text):
  syntaxHeadingMatch = misc.thisH2Match(text, "Syntax")
  syntaxBlockStart = syntaxHeadingMatch.end(0)
  nextH2Dict = misc.findNextH2(text, syntaxBlockStart)
  syntaxBlockEnd = nextH2Dict["matchStart"]

  return {"start": syntaxBlockStart, "end":syntaxBlockEnd}
