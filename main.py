from pathlib import Path
from support import syntax
from support import examples
from support import git


repoList = ['../../inspec-aws/', '../../inspec-azure/', '../../inspec-habitat/']

inputFilePath = "docs/resources/"
outputFilePath = "docs-chef-io/resources"

for repo in repoList:
  git.pullRepo(repo)
