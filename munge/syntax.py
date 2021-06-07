from . import misc
import re

def mungeSyntaxBlock(text, start, end):
  syntaxText = text[start:end]
  regexParameters = r"^#+ Parameters"
  notHeadingNotNewline = r"^[^#|\n]"
  newLine = r"^\n"

  textList = syntaxText.splitlines(True)

  foundParameters = False
  foundFirstParameter = False
  wrapLinesCount = 0
  for index, line in enumerate(textList):
    # print(line)
    regexParameter = r"^#+ (\w+)"
    if foundParameters:
      substParameter = "`\\g<1>`"
      regexEmptyLine = r"^ *\n"
      regexNormalLine = r"^"
      substNewLine = ": "
      substWrapLine = "  "
      seeAlsoTheLineRegex = r"^See also the "

      if re.search(regexParameter, line):
        line = re.sub(regexParameter, substParameter, line, 0, re.M)
        foundFirstParameter = True
        # print("this is the output: ")
        # print(output)
        # textList[index] = output
        # print(line)

        regexRequired = r"_\(required\)_"
        substRequired = "| `REQUIRED`"
        line = re.sub(regexRequired, substRequired, line, 0)

        regexOptional = r"_\(optional\)_"
        substOptional = "| `OPTIONAL`"
        textList[index] = re.sub(regexOptional, substOptional, line, 0)

      elif foundFirstParameter:
        if re.search(regexEmptyLine, line):
          wrapLinesCount = 0
        else:
          wrapLinesCount += 1

        if wrapLinesCount == 0:
          continue
        elif wrapLinesCount == 1 and not re.search(seeAlsoTheLineRegex, line):
          textList[index] = re.sub(regexNormalLine, substNewLine, line, 1, re.M)
        else:
          if not re.search(seeAlsoTheLineRegex, line):
            textList[index] = re.sub(regexNormalLine, substWrapLine, line, 1, re.M)

    if re.search(regexParameters, line):
      # print("found parameters:")
      foundParameters = True

  syntaxText = "".join(textList)

  substParameters = "where:"
  syntaxText = re.sub(regexParameters, substParameters, syntaxText, 0, re.M)

  text = text[:start] + syntaxText + text[end:]
  return text

def openSyntaxBlock(text):
  syntaxHeadingMatch = misc.thisH2Match(text, "Syntax")
  if syntaxHeadingMatch:
    syntaxBlockStart = syntaxHeadingMatch.end(0)
    nextH2Dict = misc.findNextH2(text, syntaxBlockStart)
    syntaxBlockEnd = nextH2Dict["matchStart"]
  else:
    syntaxBlockStart = None
    syntaxBlockEnd = None

  return {"start": syntaxBlockStart, "end":syntaxBlockEnd}
