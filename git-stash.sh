#!/bin/bash
STASH_DIR=~/tmp/git-stash
mkdir -p "$STASH_DIR"

git-stash-save() {
    local stash="$STASH_DIR/$1"
    git diff HEAD -- $GIT_PATHS >"$stash"
    git apply -R <"$stash"
}

git-stash-apply() {
    git apply <"$STASH_DIR/$1"
}

git-stash-show() {
    delta <"$STASH_DIR/$1"
}

git-diff() {
    git diff $* -- $GIT_PATHS
}
