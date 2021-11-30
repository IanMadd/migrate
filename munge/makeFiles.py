import os
import re
from pathlib import Path
from distutils.dir_util import copy_tree
import shutil
from . import openClose

archetypeFile = Path('munge/files/resource_archetype.md')
goModFile = Path('munge/files/go.mod')
docsChefIo = 'docs-chef-io'
outputGoMod = docsChefIo + '/go.mod'
outputArchetype = docsChefIo + '/archetypes/resource.md'

def makeDocsDirs(repo, subPathList):
    for subPath in subPathList:
        path = os.path.join(repo, subPath)
        if not os.path.isdir(path):
            os.makedirs(path)

def addStandardDocsFiles(repo):

    archetypeText = openClose.openFile(archetypeFile)
    goModText = openClose.openFile(goModFile)
    docsChefIoPath = repo + '/docs-chef-io'
    toolsDir = repo + '/docs/tools'

    platform = None
    if 'inspec-aws' in repo:
        platform = 'aws'
    elif 'inspec-azure' in repo:
        print('azure')
        platform = 'azure'
    elif 'inspec-habitat' in repo:
        print('hab')
        platform = 'habitat'
    elif 'inspec-alicloud' in repo:
        print('alicloud')
        platform = 'alicloud'
    else:
        os.error

    if 'forks' in repo:
        org = 'ianmadd'
    else:
        org = 'inspec'

    platformRegex = r"<PLATFORM>"
    orgRegex = r"<ORG>"
    archetypeText = re.sub(platformRegex, platform, archetypeText, 0, re.M)
    goModText = re.sub(platformRegex, platform, goModText, 1, re.M)
    goModText = re.sub(orgRegex, org, goModText, 1)

    outputArchetypePath = Path(repo) / outputArchetype
    outputGoModPath = Path(repo) / outputGoMod

    openClose.outputFile(outputArchetypePath, archetypeText)
    openClose.outputFile(outputGoModPath, goModText)

    ### Move shortcodes from munge/files/REPO/ to repo/docs-chef-io/*

    if platform == 'azure':
        copy_tree('munge/files/inspec-azure/', docsChefIoPath)
    elif platform == 'aws':
        copy_tree('munge/files/inspec-aws/', docsChefIoPath)

    ## Move Vale tools
    copy_tree(toolsDir, docsChefIoPath)

    ## Move vale.ini file
    shutil.copy(repo + "/docs/.vale.ini", docsChefIoPath + '/.vale.ini')