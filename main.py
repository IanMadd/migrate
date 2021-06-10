import os
import git
import sys

from pathlib import Path
import munge.syntax
import munge.examples
import munge.misc
import munge.repo
import munge.openClose
import munge.makeFiles
import munge.frontmatter
import munge.output
import munge.awsInstall
import munge.azureInstall
import munge.azureParameters

repoList = ['../../inspec-aws', '../../inspec-azure']

inputDocsFilePath = "docs/resources/"
outputDocsFilePath = "docs-chef-io/resources"

## Pull in latest changes to master
## checkout new branch "hugo"

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

    inputRepoDocsFilePath = Path(repo) / inputDocsFilePath
    outputRepoDocsFilePath = Path(repo) / outputDocsFilePath

    resourcePages = os.listdir(inputRepoDocsFilePath)

    print("\n++++++++++++++++++++++++++++++++++\n\n" + "Repo: " + repo + "\n\n++++++++++++++++++++++++++++++++++\n")
    for page in resourcePages:
      inputFilePath = inputRepoDocsFilePath / page
      outputFilePath = outputRepoDocsFilePath / page
      if not os.path.isdir(inputFilePath):
        print(page)
        print(inputFilePath)
        fileText = munge.openClose.openFile(inputFilePath)

        ## Sections that need processing:
          ### Frontmatter
          ### Title heading
          ### Azure REST API version, endpoint and http client parameters
          ### azure -> ## Availability
          ### Parameters
          ### Properties
          ### Examples
          ### Matchers
          ### Azure Permissions

        ## Frontmatter
        fileText = munge.frontmatter.fixFrontmatter(fileText)

        ## Title
        fileText = munge.misc.removeHeadingTitle(fileText)

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
          outputLog = munge.output.log('Missing Syntax heading -----> ' + page , outputLog)

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
          outputLog = munge.output.log('Missing examples heading -----> ' + page , outputLog)

        munge.openClose.outputFile(outputFilePath, fileText)

  munge.openClose.outputFile('outputLog.txt', outputLog)

def resetRepos():
  for resourceRepo in repoList:
    munge.repo.pullRepo(resourceRepo)