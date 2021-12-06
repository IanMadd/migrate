import os
import git

def pullRepo(filePath, editBranch):
    repo = git.Repo(filePath)
    repo.git.reset('--hard')
    repo.git.clean('-fd')
    repo.git.checkout('main')

    if "forks" in filePath:
        remoteSourceBranch = 'upstream/main'
        repo.remotes.upstream.fetch('main')
        if repo.git.diff(remoteSourceBranch, 'main') != '':
            repo.git.merge(remoteSourceBranch)
            repo.remotes.origin.push('main')

    else:
        remoteSourceBranch = 'origin/main'
        repo.remotes.origin.pull('--ff')

    repo.git.checkout(editBranch)
    repo.git.rebase(remoteSourceBranch)


def newBranch(filePath, branch):
    repo = git.Repo(filePath)
    if branch not in repo.branches:
        repo.git.branch(branch)

