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
    regularLineRegex = r"^[\n|\r|\w|#]"
    backticksRegex = r"^```\s{0,1}\w{0,}"
    backtickCodeBlock = False

    textList = text.splitlines(True)

    editingCodeBlock = False
    loopBreak = 0

    for index,line in enumerate(textList):
        loopBreak += 1
        if loopBreak >= 1000:
            break

        ## If a line has a fenced codeblock markers, ie "```", and the script has already matched a fenced codeblock,
        ## then set backtickCodeBlock to False.
        ## That is to say the script has already started processing a fenced codeblock on a previous line and has found the end
        ## of the fenced codeblock.
        if re.search(backticksRegex, line) and backtickCodeBlock == True:
            backtickCodeBlock = False

        ## If it finds backticks code fencing and it hasn't found backtick code fencing on a previous line
        ## set backtickCodeBlock to True to the codeblock isn't processed in the next step.
        if re.search(backticksRegex, line) and backtickCodeBlock == False:
            backtickCodeBlock = True


        if (foundIndentBlock := re.search(findIndentCodeRegex, line)) is not None and backtickCodeBlock == False:
            if editingCodeBlock == False:
                numberOfIndentSpaces = str(len(line) - len(line.lstrip(' ')))
                unindentCodeRegex = r"^ {" + numberOfIndentSpaces + "}"
                textList[index] = "```ruby\n" + re.sub(unindentCodeRegex, "", line)
                editingCodeBlock = True
            else:
                textList[index] = re.sub(unindentCodeRegex, "", line)

        elif not foundIndentBlock and editingCodeBlock == True:
            if re.search(regularLineRegex, line):
                # print(line)
                textList[index] = "```\n" + textList[index]
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
        readmeSubstLink = '[README](https://github.com/inspec/inspec-azure/blob/main/README.md'
    elif "inspec-aws" in repo:
        readmeSubstLink = '[README](https://github.com/inspec/inspec-aws/blob/main/README.md'
    elif "inspec-alicloud" in repo:
        readmeSubstLink = '[README](https://github.com/inspec/inspec-alicloud/blob/main/README.md'

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

def openBlock(text, heading):
    headingMatch = thisH2Match(text, heading)
    if headingMatch:
        blockStart = headingMatch.end(0)
        nextH2Dict = findNextH2(text, blockStart)
        blockEnd = nextH2Dict["matchStart"]
    else:
        blockStart = None
        blockEnd = None

    return {"start": blockStart, "end":blockEnd}
