import re

def removeSlash(text):
  regex = r"(\\_)"
  subst = "_"
  text = re.sub(regex, subst, text, 0, re.MULTILINE)
  return text

def removeHeadingTitle(text):
  h1HeadingRegex = r"^#\s[\w|\\]+\n\n"
  textSubnOutput = re.subn(h1HeadingRegex, "", text, 1, re.M)
  if textSubnOutput[1] != 1:
    raise Exception('No H1 heading removed')
  else:
    text = textSubnOutput[0]

  return text

def thisH2Match(text, headingString):
  regex = r"^##\s" + headingString
  return re.search(regex, text, re.M)

def findNextH2(text, startIndex=0):
  regex = r"^##\s[\w| ]+\n"
  nextH2Match = re.search(regex, text[startIndex:], re.M)
  if nextH2Match:
    matchStart = startIndex + nextH2Match.start(0)
    matchEnd = startIndex + nextH2Match.end(0)
  else:
    matchStart = len(text)
    matchEnd = matchStart

  matchContent = {"matchObject": nextH2Match, "matchStart": matchStart, "matchEnd": matchEnd}
  return matchContent

def processCodeBlocks(text):
  findIndentCodeRegex = r"^ {4}[\w|\s]"
  unindentCodeRegex = r"^ {4}"
  regularLineRegex = r"^[\n|\r|\w|#]"
  backticksRegex = r"^```\s{0,1}\w{0,}"

  textList = text.splitlines(True)

  editingCodeBlock = False
  loopBreak = 0
  original_text = text
  print("Number of lines: " + str(len(textList)))
  for index,line in enumerate(textList):
    loopBreak += 1
    if loopBreak >= 100:
      break

    foundIndentBlock = re.search(findIndentCodeRegex, line)
    if foundIndentBlock:
      if editingCodeBlock == False:
        textList[index] = "```ruby\n" + re.sub(unindentCodeRegex, "", line)
        editingCodeBlock = True
      else:
        textList[index] = re.sub(unindentCodeRegex, "", line)

    elif not foundIndentBlock and editingCodeBlock == True:
      if re.search(regularLineRegex, line):
        print(line)
        textList[index] = "```\n\n"
        editingCodeBlock = False

  output = "".join(textList)
  print(output)
  return output

