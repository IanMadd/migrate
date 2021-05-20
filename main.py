import os
import git
from pathlib import Path
from support import syntax
from support import examples
from support import misc
from support import repo
from support import openClose
from support import makeFiles
from support import frontmatter


repoList = ['../../inspec-aws', '../../inspec-azure']

inputDocsFilePath = "docs/resources/"
outputDocsFilePath = "docs-chef-io/resources"

## Pull in latest changes to master
## checkout new branch "hugo"

def run():

  for resourceRepo in repoList:
    repo.pullRepo(resourceRepo)
    repo.newBranch(resourceRepo, 'im/hugo')


  ## add standard files "archetypes", "go.mod" to Hugo branch
    docsSubPathList = ["docs-chef-io/resources", "docs-chef-io/archetypes"]
    makeFiles.makeDocsDirs(resourceRepo, docsSubPathList)
    makeFiles.addStandardDocsFiles(resourceRepo)


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
        fileText = openClose.openFile(inputFilePath)

        fileText = frontmatter.fixFrontmatter(fileText)
        fileText = misc.removeHeadingTitle(fileText)
        fileText = misc.removeSlash(fileText)
        fileText = misc.processCodeBlocks(fileText)

        syntaxBlock = syntax.openSyntaxBlock(fileText)
        fileText = syntax.mungeSyntaxBlock(fileText, syntaxBlock['start'], syntaxBlock['end'])

        openClose.outputFile(outputFilePath, fileText)

def resetRepos():
  for resourceRepo in repoList:
    repo.pullRepo(resourceRepo)