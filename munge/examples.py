from . import misc
import re

def mungeExamples(text, start, end):
  examplesText = text[start:end]
  exampleHeadingRegex = r"#+ ([\S| ]+)"
  periodEndOfHeadingRegex = r"\.$"
  emptyLineRegex = r"^\n"
  textList = examplesText.splitlines(True)
  headingLine = False
  for index, line in enumerate(textList):
    if headingLine and not re.match(emptyLineRegex, line):
      textList[index] = "\n" + line
    if (match := re.search(exampleHeadingRegex, line)):
      headingLine = True
      heading = match.group(1)
      if not re.search(periodEndOfHeadingRegex, heading):
        heading = heading + '.'
      textList[index] = "**" + heading + "**\n"
    else:
      headingLine = False

  examplesText = "".join(textList)

  text = text[:start] + examplesText + text[end:]

  return text

