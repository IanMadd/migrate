import re

def spacesAroundHeadings(text):
    textList = text.splitlines(True)
    headingRegex = r"^#{1,6} [\w| |\-|\`|\_|\(|\)|\.]+$"
    emptyLineSpaceRegex = r"^ {0,}\n$"
    emptyLineRegex = r"^\n$"

    for index, line in enumerate(textList):
        if re.search(headingRegex, line, re.M):
            if not re.search(emptyLineRegex, textList[index-1], re.M):
                if re.search(emptyLineSpaceRegex, textList[index-1], re.M):
                    textList[index-1] = '\n'
                else:
                    textList[index] = "\n" + line

            if not re.search(emptyLineRegex, textList[index+1], re.M):
                if re.search(emptyLineSpaceRegex, textList[index+1], re.M):
                    textList[index+1] = '\n'
                else:
                    textList[index] = line + '\n'

    text = "".join(textList)
    return text

def correctHeadingOrder(text):
    previousHeadingLevel = None
    foundH1 = False
    headingRegex = r"^#{1,6} {0,}([\w| |\-|\`|\_|\(|\)|\.]+)$"
    errorText = ''
    codeBlock = False
    fencedCodeBlockRegex = r"^```{1,} {0,}[\w| ]{0,}$"
    h2HeadingList = ["Properties", "Parameters", "Syntax", "Examples", "Matchers", "AWS Permissions", "Azure Permissions"]

    textList = text.splitlines(True)

    for index, line in enumerate(textList):
        fencedCodeBlock = re.search(fencedCodeBlockRegex, line, re.M)

        if codeBlock is False and fencedCodeBlock is not None:
            codeBlock = True

        elif codeBlock is True and fencedCodeBlock is not None:
            codeBlock = False

        if codeBlock is False:
            if (headingMatch := re.search(headingRegex, line, re.M)) is not None:
                headingText = headingMatch.group(1)
                headingLevel = len(line) - len(line.lstrip('#'))
                if headingLevel == 1:
                    if foundH1 == True:
                        errorText += "H1 heading found in wrong place on line " + str(index)
                        continue
                    elif previousHeadingLevel is not None:
                        errorText += "H1 heading found in wrong place on line " + str(index)
                        continue
                    else:
                        foundH1 = True
                        previousHeadingLevel = 1
                        continue

                if headingText in h2HeadingList:
                    if headingLevel != 2:
                        newHeading = '## ' + headingText + '\n'
                        textList[index] = newHeading
                        previousHeadingLevel = 2
                    else:
                        previousHeadingLevel = 2
                        continue
                else:
                    if headingLevel != 3:
                        newHeading = '### ' + headingText + '\n'
                        textList[index] = newHeading
                        previousHeadingLevel = 3
                    else:
                        previousHeadingLevel = 3


    text = "".join(textList)
    return text, errorText
