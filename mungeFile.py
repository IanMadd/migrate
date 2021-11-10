import sys, os, munge
from main import mungeFile

inputFilePath = sys.argv[1]

page, repo = munge.misc.returnPageAndRepo(inputFilePath)

outputDocsDirPath = "docs-chef-io/content/inspec/resources"
outputRepoDocsDirPath = '../' + repo + '/' + outputDocsDirPath
outputRepoDocsFilePath = outputRepoDocsDirPath + '/' + page


if not os.path.isdir(outputRepoDocsDirPath):
    os.makedirs(outputRepoDocsDirPath)

print('This is the input file path: ' + inputFilePath)
print('This is the output file path: ' + outputRepoDocsFilePath)


fileText, fileOutputLog = mungeFile(inputFilePath)

munge.openClose.outputFile(outputRepoDocsFilePath, fileText)
munge.openClose.outputFile('outputLog.txt', fileOutputLog)
