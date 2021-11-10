import re

def removeSlash(text):
  regex = r"\\_"
  subst = "_"
  result = re.sub(regex, subst, text, 0, re.MULTILINE)
  return result

def removeHeadingTitle(text):
  h1HeadingRegex = r"^#\s[\w|\\]+\n{1,2}"
  textSubnOutput = re.subn(h1HeadingRegex, "", text, 1, re.M)

  return textSubnOutput

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
  # print("Number of lines: " + str(len(textList)))
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
        # print(line)
        textList[index] = "```\n\n"
        editingCodeBlock = False

  output = "".join(textList)
  # print(output)
  return output


def removeEmptySpaces(text):
  regex = r"^ +\n"
  subst = "\n"
  textList = text.splitlines(True)
  for index,line in enumerate(textList):
    textList[index] = re.sub(regex, subst, line, 0)

  text = "".join(textList)
  return text

def formatLinks(text, repo):

  ## Handle links to README pages in repo
  readmeLinkRegex = r'\[README\]\(\.\./\.\./README\.md'
  if "inspec-azure" in repo:
    readmeSubstLink = '[README](https://github.com/inspec/inspec-azure/blob/master/README.md'
  elif "inspec-aws" in repo:
    readmeSubstLink = '[README](https://github.com/inspec/inspec-aws/blob/master/README.md'

  text = re.sub(readmeLinkRegex, readmeSubstLink, text, 0, re.M)

  ## Handle all links that don't start with "http"
  localFileRegex = r"\]\(([^(http)][\w|\.|\#]+)\)"
  localFileSubst = "]({{< relref \"\\g<1>\" >}})"
  text = re.sub(localFileRegex, localFileSubst, text, 0, re.M)

  return text

def mergeTextCorrectEmptyLines(upperText, insertText, lowerText):
  upperText = upperText.rstrip() + '\n\n'
  lowerText = '\n\n' + lowerText.lstrip()
  insertText = insertText.strip()

  return upperText + insertText + lowerText

def returnPageAndRepo(fullPageFilePath):
  filePathSplit = str(fullPageFilePath).split('/')
  page = filePathSplit[-1]

  for section in filePathSplit:
    if 'inspec-' in section:
      repo = section
      break

  return page, repo
