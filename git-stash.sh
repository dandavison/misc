#!/bin/bash
STASH_DIR=~/tmp/git-stash
mkdir -p "$STASH_DIR"

-git-stash-stash-file() {
    local stash="$1"
    if [[ "$stash" != /* ]]; then
        echo "$STASH_DIR/$stash"
    else
        echo "$stash"
    fi
}

git-stash-save() {
    local stash=$(-git-stash-stash-file "$1")
    git diff HEAD -- $GIT_PATHS >"$stash"
    git apply -R <"$stash"
}

git-stash-apply() {
    git apply <$(-git-stash-stash-file "$1")
}

git-stash-show() {
    delta <$(-git-stash-stash-file "$1")
}

git-diff() {
    git diff $* -- $GIT_PATHS
}
