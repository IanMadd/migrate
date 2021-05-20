import os
import re
from pathlib import Path
from . import openClose

archetypeFile = Path('munge/files/resource_archetype.md')
goModFile = Path('munge/files/go.mod')
outputGoMod = 'docs-chef-io/go.mod'
outputArchetype = 'docs-chef-io/archetypes/resource.md'


def makeDocsDirs(repo, subPathList):
  for subPath in subPathList:
    path = os.path.join(repo, subPath)
    os.makedirs(path)

def addStandardDocsFiles(repo):

  archetypeText = openClose.openFile(archetypeFile)
  goModText = openClose.openFile(goModFile)

  platform = None
  if 'inspec-aws' in repo:
    platform = 'aws'
  elif 'inspec-azure' in repo:
    print('azure')
    platform = 'azure'
  elif 'inspec-habitat' in repo:
    print('hab')
    platform = 'habitat'
  else:
    os.error

  regex = r"<PLATFORM>"
  archetypeText = re.sub(regex, platform, archetypeText, 0, re.M)
  goModText = re.sub(regex, platform, goModText, 1, re.M)

  outputArchetypePath = Path(repo) / outputArchetype
  outputGoModPath = Path(repo) / outputGoMod

  openClose.outputFile(outputArchetypePath, archetypeText)
  openClose.outputFile(outputGoModPath, goModText)

