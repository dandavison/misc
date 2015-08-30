#!/bin/bash
# Rebase feature branch on top of an empty commit. Useful for opening the first PR in a repo.
# Warning: this destructively rebases your current branch: create a backup branch pointing to the current HEAD first.
# Probably best to make sure you agree with these commands before executing them!

set -e

# This script assumes that the current branch is the one you want to rebase
feature_branch=`git symbolic-ref --short HEAD`
empty_branch=empty

# Create a branch pointing at the first commit in the repo
git checkout -b $empty_branch `git rev-list --all | tail -n1`

# Convert it into an empty commit
git rm `git ls-files`
git commit --allow-empty --amend -m "Empty commit"

# Rebase your feature branch
git checkout $feature_branch
git rebase $empty_branch

# You probably want to rename the empty branch as "master" so that the first PR merges into master.
