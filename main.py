import os, munge
from pathlib import Path

repoList = ['../inspec-aws', '../inspec-azure']

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

  ## Miscellaneous
  fileText = munge.misc.removeSlash(fileText)
  fileText = munge.misc.removeEmptySpaces(fileText)
  fileText = munge.misc.processCodeBlocks(fileText)
  fileText = munge.misc.formatLinks(fileText, repo)

  ## Syntax
  syntaxBlock = munge.syntax.openSyntaxBlock(fileText)
  if syntaxBlock['start'] and syntaxBlock['end']:
    fileText = munge.syntax.mungeSyntaxBlock(fileText, syntaxBlock['start'], syntaxBlock['end'])
  else:
    fileOutputLog = munge.output.log('Missing Syntax heading -----> ' + page , fileOutputLog)

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

  return fileText, fileOutputLog

def run():
  for resourceRepo in repoList:
    munge.repo.pullRepo(resourceRepo)
    munge.repo.newBranch(resourceRepo, 'im/hugo')


  ## add standard files "archetypes", "go.mod" to Hugo branch
    docsSubPathList = ["docs-chef-io/resources", "docs-chef-io/archetypes"]
    munge.makeFiles.makeDocsDirs(resourceRepo, docsSubPathList)
    munge.makeFiles.addStandardDocsFiles(resourceRepo)


  ## open each file

  for repo in repoList:
    outputLog = ''
    print(repo)
    inputRepoDocsFilePath = Path(repo) / inputDocsFilePath
    outputRepoDocsFilePath = Path(repo) / outputDocsFilePath

    if not os.path.isdir(outputRepoDocsFilePath):
      os.makedirs(outputRepoDocsFilePath)

    resourcePages = os.listdir(inputRepoDocsFilePath)

    print("\n++++++++++++++++++++++++++++++++++\n\n" + "Repo: " + repo + "\n\n++++++++++++++++++++++++++++++++++\n")
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
