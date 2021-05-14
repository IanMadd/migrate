import os
import git

def pullRepo(file_path):
  repo = git.Repo(file_path)
  repo.git.checkout('master')
  repo.remotes.origin.pull('--ff')


def newBranch(repo, branch):
  repo = git.Repo(repo)
  repo.git.branch(branch)
  repo.git.checkout(branch)