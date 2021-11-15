import re
from . import misc


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
    linkRegex = r"(\[[\w| ]+\]\([\w|:|\/|\.|\-]+\))"
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
            parametersText = parametersText[:awsLinkTextStart].rstrip() + '\n\n' + parametersText[nextBlankLineStart:].lstrip()
            pageText = pageText[:parametersTextStart].rstrip() + "\n\n" + parametersText.strip() + "\n\n" + pageText[nextH2Start:].lstrip()

            firstH2 = re.search(firstH2Regex, pageText, re.M)
            firstH2Start = firstH2.start()
            pageText = pageText[:firstH2Start].rstrip() + '\n\n' + awsLinkText.strip() + '\n\n' + pageText[firstH2Start:].lstrip()
            movedLink = True


    return pageText, movedLink