import os
import git

def pullRepo(file_path):
    repo = git.Repo(file_path)
    repo.git.reset('--hard')
    repo.git.clean('-fd')
    repo.git.checkout('main')

    if "forks" in file_path:
        repo.remotes.upstream.fetch('main')
        if repo.git.diff('upstream/main', 'main') != '':
            repo.git.merge('upstream/main')
            repo.remotes.origin.push('main')

    else:
        repo.remotes.origin.pull('--ff')


def newBranch(file_path, branch):
    repo = git.Repo(file_path)
    if branch in repo.branches:
        repo.delete_head(branch, force=True)
    repo.git.branch(branch)
    repo.git.checkout(branch)
