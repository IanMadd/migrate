import os, munge, re
from pathlib import Path

# repoList = ['../inspec-aws', '../inspec-azure']
repoList = ['../forks/inspec-aws', '../forks/inspec-azure']

inputDocsFilePath = "docs/resources/"
outputDocsFilePath = "docs-chef-io/content/inspec/resources"


def mungeFile(filePath):

    page, repo = munge.misc.returnPageAndRepo(filePath)

    fileOutputLog = ''
    fileText = munge.openClose.openFile(filePath)

    ## Sections that need processing:

        ### Azure REST API version, endpoint and http client parameters
        ### azure -> ## Availability
        ### Parameters
        ### Properties
        ### Examples
        ### Matchers
        ### Azure Permissions

    ## Frontmatter
    fileText, returnFrontMatterErrorLogText = munge.frontmatter.fixFrontmatter(fileText)
    if returnFrontMatterErrorLogText != '':
        fileOutputLog = munge.output.log(returnFrontMatterErrorLogText, fileOutputLog)

    ## Title
    removeHeadingTitleText = munge.misc.removeHeadingTitle(fileText)
    if removeHeadingTitleText[1] != 1:
        fileOutputLog = munge.output.log("Title missing -----> " + page, fileOutputLog)
    else:
        fileText = removeHeadingTitleText[0]

    ## Fix headings
    fileText = munge.headings.spacesAroundHeadings(fileText)
    fileText, errorText = munge.headings.correctHeadingOrder(fileText)
    if errorText != '':
        fileOutputLog = munge.output.log("Incorrect Heading levels " + page, fileOutputLog)

    ## Miscellaneous
    fileText = munge.misc.removeSlash(fileText)
    fileText = munge.misc.removeEmptySpaces(fileText)
    fileText = munge.misc.processCodeBlocks(fileText)
    fileText = munge.misc.formatLinks(fileText, repo)

    ## Syntax
    # syntaxBlock = munge.syntax.openSyntaxBlock(fileText)
    # if syntaxBlock['start'] and syntaxBlock['end']:
    #     fileText = munge.syntax.mungeSyntaxBlock(fileText, syntaxBlock['start'], syntaxBlock['end'])
    # else:
    #     fileOutputLog = munge.output.log('Missing Syntax heading -----> ' + page , fileOutputLog)

    ## Installation
    if "inspec-aws" in repo:
        fileText = munge.awsInstall.addAwsInstallText(fileText)
    elif "inspec-azure" in repo:
        fileText = munge.azureInstall.replaceInstallHeadings(fileText)
        fileText = munge.azureInstall.replaceInstallText(fileText)

    ## Azure REST API Version, Endpoint, and HTTP Client Parameters
    if "inspec-azure" in repo:
        fileText = munge.azureParameters.azureCommonParameters(fileText)

    ## Examples
    examplesBlock = munge.examples.openExamples(fileText)
    if examplesBlock['start']:
        fileText = munge.examples.mungeExamples(fileText, examplesBlock['start'], examplesBlock['end'])
    else:
        fileOutputLog = munge.output.log('Missing examples heading -----> ' + page , fileOutputLog)

    ## Parameters

    if "inspec-aws" in repo:
        outputText, movedLink = munge.parameters.moveAWSLink(fileText)
        if movedLink:
            fileText = outputText
        else:
            outputLogText = "Did NOT move link to AWS API documentation in " + str(page)
            fileOutputLog = munge.output.log(outputLogText, fileOutputLog)

    ### Azure Parameters
    fileText = munge.azureParameters.azureCommonParameters(fileText)

    ### AWS Parameters


    ## Properties
    startEnd = munge.properties.openProperties(fileText)
    propertiesOutput = munge.properties.mungeProperties(fileText, startEnd['start'], startEnd['end'])
    if propertiesOutput[1] != '':
        fileOutputLog = munge.output.log('Properties Table Problem -----> ' + page + '\n\n' + propertiesOutput[1], fileOutputLog)
    else:
        fileText = munge.misc.mergeTextCorrectEmptyLines(fileText[:startEnd['start']], propertiesOutput[0], fileText[startEnd['end']:])

    ## AWS Permissions

    if repo == "inspec-aws":
        permissionsReplace = False
        startEnd = munge.permissions.openAwsPermissions(fileText)
        if startEnd['start'] is not None and startEnd['end'] is not None:
            permissionsText = fileText[startEnd['start']: startEnd['end']]
            permissionsOutput, permissionsReplace = munge.permissions.awsPermissions(permissionsText)

            if permissionsReplace:
                fileText = fileText[:startEnd['start']] + permissionsOutput + fileText[startEnd['end']:]
            else:
                fileOutputLog = munge.output.log("AWS Permissions text not replaced in " + str(filePath) + "\n\n", fileOutputLog)
                fileOutputLog = munge.output.log(permissionsText + '\n\n', fileOutputLog)
        else:
            fileOutputLog = munge.output.log("AWS Permissions text not replaced in " + str(filePath) + ". AWS Permissions heading not found.", fileOutputLog)
            fileOutputLog = munge.output.log("AWS Permissions StartEnd " + str(startEnd) + "\n\n", fileOutputLog)
            fileOutputLog = munge.output.log("FileText --->" + fileText + "<-- End FileText\n\n", fileOutputLog)

    ## Azure Permissions
    if repo == "inspec-azure":
        permissionsReplace = False
        startEnd = munge.permissions.openAzurePermissions(fileText)
        if startEnd['start'] is not None and startEnd['end'] is not None:
            permissionsText = fileText[startEnd['start']: startEnd['end']]
            permissionsOutput, permissionsReplace = munge.permissions.azurePermissions(permissionsText)

            if permissionsReplace:
                fileText = fileText[:startEnd['start']] + permissionsOutput + fileText[startEnd['end']:]
            else:
                fileOutputLog = munge.output.log("Azure Permissions text not replaced in " + str(filePath) + "\n\n", fileOutputLog)
                fileOutputLog = munge.output.log(permissionsText + '\n\n', fileOutputLog)
        else:
            fileOutputLog = munge.output.log("Azure Permissions text not replaced in " + str(filePath) + ". Azure Permissions heading not found.\n", fileOutputLog)
            fileOutputLog = munge.output.log("Azure Permission StartEnd: " + str(startEnd) + "\n\n", fileOutputLog)

    return fileText, fileOutputLog

def run():
    outputLog = ''
    for resourceRepo in repoList:
        munge.repo.pullRepo(resourceRepo)
        munge.repo.newBranch(resourceRepo, 'im/hugo')


    ## add standard files "archetypes", "go.mod" to Hugo branch
        docsSubPathList = ["docs-chef-io/resources", "docs-chef-io/archetypes"]
        munge.makeFiles.makeDocsDirs(resourceRepo, docsSubPathList)
        munge.makeFiles.addStandardDocsFiles(resourceRepo)


    ## open each file

    for repo in repoList:
        outputLog += "\n++++++++++++++++++++++++++++++++++\n\nRepo: " + repo + "\n\n++++++++++++++++++++++++++++++++++\n\n"
        print(repo)
        inputRepoDocsFilePath = Path(repo) / inputDocsFilePath
        outputRepoDocsFilePath = Path(repo) / outputDocsFilePath

        if not os.path.isdir(outputRepoDocsFilePath):
            os.makedirs(outputRepoDocsFilePath)

        resourcePages = os.listdir(inputRepoDocsFilePath)

        print("\n++++++++++++++++++++++++++++++++++\n\nRepo: " + repo + "\n\n++++++++++++++++++++++++++++++++++\n\n")
        for page in resourcePages:
            print(page)
            inputFilePath = inputRepoDocsFilePath / page
            outputFilePath = outputRepoDocsFilePath / page
            if not os.path.isdir(inputFilePath):
                print(page)
                print(inputFilePath)

                fileText, fileOutputLog = mungeFile(inputFilePath)
                outputLog += str(inputFilePath) + '\n' + fileOutputLog + '\n\n'

                munge.openClose.outputFile(outputFilePath, fileText)

    munge.openClose.outputFile('outputLog.txt', outputLog)

def resetRepos():
    for resourceRepo in repoList:
        munge.repo.pullRepo(resourceRepo)
