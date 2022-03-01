#!/bin/bash
set -u
STASH=/tmp/git-stash

git-stash-save() {
    git diff HEAD -- $SOURCE_PROJECT_DIR >$STASH
    git apply -R <$STASH
}

git-stash-apply() {
    git apply <$STASH
}

git-stash-show() {
    cat $STASH
}
