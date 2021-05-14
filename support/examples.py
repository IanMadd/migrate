from . import misc
import re

def openExamples(text):
  blockHeadingText = "Examples"
  examplesHeadingMatch = misc.thisH2Match(text, blockHeadingText)
  examplesBlockStart = examplesHeadingMatch.end(0)
  nextH2Dict = misc.findNextH2(text, examplesBlockStart)
  examplesBlockEnd = nextH2Dict["matchStart"]

  return {"start": examplesBlockStart, "end": examplesBlockEnd}

def mungeExamples(text, start, end):
  examplesText = text[start:end]
  examplesText = misc.removeSlash(examplesText)
  examplesText = misc.processCodeBlocks(examplesText)
  exampleHeadingRegex = r"#+ ([\S| ]+)"
  periodEndOfHeading = r"\.$"

  textList = examplesText.splitlines(True)

  for index, line in enumerate(textList):
    if (match := re.search(exampleHeadingRegex, line)):
      heading = match.group(1)
      if not re.search(periodEndOfHeading, heading):
        heading = heading + '.'
      textList[index] = heading

  examplesText = "".join(textList)

  text = text[:start] + examplesText + text[end:]

  return text

