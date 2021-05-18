import os
import git

def pullRepo(file_path):
  repo = git.Repo(file_path)
  repo.git.reset('--hard')
  repo.git.clean('-fd')
  repo.git.checkout('master')
  repo.remotes.origin.pull('--ff')


def newBranch(file_path, branch):
  repo = git.Repo(file_path)
  if branch in repo.branches:
    repo.delete_head(branch)
  repo.git.branch(branch)
  repo.git.checkout(branch)