import re
from . import misc, tableToDict, dictToDefinition

def moveAWSLink(pageText):
    movedLink = False
    foundLinkText = False
    # Phrases:
        # - "See also the " - 93 files
                # Example: "For additional information, see the [AWS documentation on AWS EC2 network interface](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface.html)."
        # - "For additional information" - 194 files
        # Some links of text have additional sentences following, so this should grab and move that sentence plus all sentences until the next empty line.
    # Replace with:
    # "For additional information, including details on parameters and properties, see the [blah blah blah documentation](link URL)."
    # And move to page intro section but before next heading
    forAdditionalRegex = r"For additional information, see the "
    seeAlsoRegex = r"See also the "
    substAwsLinkText = "For additional information, including details on parameters and properties, see the "
    linkRegex = r"(\[[\w| |\.|`|:|\(|\)]+\]\([\w|:|\/|\.|\-]+\))"
    seeTheRegex = r"See the (\[[\w| |\.|`|:|\(|\)]+\]\([\w|:|\/|\.|\-]+\)) for additional information."
    blankLineRegex = r"$ {0,}^"
    firstH2Regex = r"^## [\w| ]+\n"

    parametersMatch = misc.thisH2Match(pageText, "Parameters")

    if (parametersMatch := misc.thisH2Match(pageText, "Parameters")) is not None:
        parametersTextStart = parametersMatch.end()
        nextH2 = misc.findNextH2(pageText, parametersTextStart)
        nextH2Start = nextH2['matchStart']
        parametersText = pageText[parametersTextStart:nextH2Start]

        if (forAdditional := re.search(forAdditionalRegex + linkRegex, parametersText)) is not None:
            awsLinkTextStart = forAdditional.start()
            foundLinkText = True

        elif (seeAlso := re.search(seeAlsoRegex + linkRegex, parametersText)) is not None:
            awsLinkTextStart = seeAlso.start()
            foundLinkText = True

        elif (seeTheMatch := re.search(seeTheRegex, parametersText, re.M)) is not None:
            foundLinkText = True
            awsLinkTextStart = seeTheMatch.start()

        if foundLinkText:
            # print("awsLinkTextStart starts here--->")
            # print(parametersText[awsLinkTextStart:])
            nextBlankLine = re.search(blankLineRegex, parametersText[awsLinkTextStart:], re.M)
            # print("From here -->" + parametersText[awsLinkTextStart:] + "<-- to here")
            # print(nextBlankLine)
            nextBlankLineStart = nextBlankLine.start() + awsLinkTextStart
            awsLinkText = parametersText[awsLinkTextStart: nextBlankLineStart]
            awsLinkText = re.sub(forAdditionalRegex, substAwsLinkText, awsLinkText, 1)
            awsLinkText = re.sub(seeAlsoRegex, substAwsLinkText, awsLinkText, 1)
            if (seeTheMatch := re.search(seeTheRegex, parametersText, re.M)) is not None:
                linkText = seeTheMatch.group(1)
                linkText = substAwsLinkText + linkText + '.'
                awsLinkText = re.sub(seeTheRegex, linkText, parametersText, 1, re.M)

            parametersText = parametersText[:awsLinkTextStart].rstrip() + '\n\n' + parametersText[nextBlankLineStart:].lstrip()

            if parametersText.strip() == "":
                print('empty')
                parametersText = "The resource does not require any parameters."
            pageText = pageText[:parametersTextStart].rstrip() + "\n\n" + parametersText.strip() + "\n\n" + pageText[nextH2Start:].lstrip()

            firstH2 = re.search(firstH2Regex, pageText, re.M)
            firstH2Start = firstH2.start()
            pageText = pageText[:firstH2Start].rstrip() + '\n\n' + awsLinkText.strip() + '\n\n' + pageText[firstH2Start:].lstrip()
            movedLink = True

    return pageText, movedLink

def azureCommonParameters(text):
    regexHeading = r"^## Azure REST API [v|V]ersion, [e|E]ndpoint,{0,1} and ((http)|(HTTP)) [c|C]lient [p|P]arameters\n"
    substHeading = "## Azure REST API Version, Endpoint, and HTTP Client Parameters\\n"

    if re.search(regexHeading, text, re.M):
        text = re.sub(regexHeading, substHeading, text, 1, re.M)

        parametersHeading = misc.thisH2Match(text, "Azure REST API Version, Endpoint, and HTTP Client Parameters")
        nextHeading = misc.findNextH2(text, parametersHeading.end())

        text = text[:parametersHeading.end()] + "\n\n{{% inspec_azure_common_parameters %}}\n\n" + text[nextHeading['matchStart']:]

    return text

def fixHeadingParameters(text):
    ## Replace parameters that are headings so they're inline code.
    ## Followed by a definition list of each parameter definition.

    textList = text.splitlines(True)
    foundFirstParameter = False
    wrapLinesCount = 0

    for index, line in enumerate(textList):
        headingParameterRegex = r"^#+ ([\w|\\]+)"
        substParameter = "`\\g<1>`"
        regexEmptyLine = r"^ *\n"
        regexNormalLine = r"^"
        substNewLine = ": "
        substWrapLine = "  "
        seeAlsoTheLineRegex = r"^See also the "

        if re.search(headingParameterRegex, line):
            textList[index] = re.sub(headingParameterRegex, substParameter, line, 0, re.M)
            foundFirstParameter = True

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

    parametersText = "".join(textList)

    return parametersText

def processParametersTable(text):
    errorText = ''
    defintionListText = ''
    tableStartEnd = tableToDict.findTableInText(text)
    tableText = text[tableStartEnd['start']:tableStartEnd['end']]

    if tableToDict.goodTable(tableText):
        parametersDict, errorText = tableToDict.convertTableToDict(tableText)
        defintionListText = dictToDefinition.convertDictToDef(parametersDict)
    else:
        errorText = "Bad table in Parameters:\n\n" + tableText

    if errorText == '' and defintionListText != '':
        text = text[:tableStartEnd['start']] + defintionListText + text[tableStartEnd['end']:]

    return text, errorText

def processParametersInlineCode(text):
    textList = text.splitlines(True)
    wrapLinesCount = 0
    inlineParamRegex = r"^`\w+`"
    emptyLineRegex = r"^ {0,}$"
    definitionTextRegex = r"^(\w)"
    multilineDefinitionTextSubst = "  \g<1>"
    firstLineDefinitionTextSubst = ": \g<1>"

    for index, line in enumerate(textList):
        if re.search(inlineParamRegex, line, re.M):
            wrapLinesCount = 0
            continue
        elif re.match(emptyLineRegex, line, re.M):
            wrapLinesCount = 0
        else:
            if wrapLinesCount >= 1:
                textList[index] = re.sub(definitionTextRegex, multilineDefinitionTextSubst, line, 1, re.M)
                wrapLinesCount += 1
            else:
                textList[index] = re.sub(definitionTextRegex, firstLineDefinitionTextSubst, line, 1, re.M)
                wrapLinesCount += 1

    text = "".join(textList)

    return text

def mungeParametersBlock(pageText, start, end):
    errorText = ''
    parametersText = pageText[start:end]
    headingParameterRegex = r"^#+ ([\w|\\]+)"
    tableParametersRegex = r"^ {0,}\|"
    inlineCodeParamRegex = r"^`\w+`"
    noParametersText1 = "This resource does not expect any parameters."
    noParametersText2 = "This resource does not require any parameters."
    noParametersText3 = "The resource does not require any parameters."
    noParametersText4 = "This resource does not accept any parameters."
    noParametersTextList = [noParametersText1, noParametersText2, noParametersText3, noParametersText4]

    if re.search(headingParameterRegex, parametersText, re.M):
        parametersText = fixHeadingParameters(parametersText)

    elif re.search(tableParametersRegex, parametersText, re.M):
        parametersText, errors = processParametersTable(parametersText)
        if errors != '':
            errorText += errors
    elif re.search(inlineCodeParamRegex, parametersText, re.M):
        parametersText = processParametersInlineCode(parametersText)
    else:
        foundNoParametersText = False
        for text in noParametersTextList:
            if text in parametersText:
                parametersText = '\n\nThis resource does not require any parameters.\n\n'
                foundNoParametersText = True
                break

        if not foundNoParametersText:
            errorText += "Didn't find any parameters to modify.\n\n" + parametersText

    pageText = pageText[:start] + parametersText + pageText[end:]

    return pageText, errorText

