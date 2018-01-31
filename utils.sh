git-repo-from-mercurial-repo () {
    git init
    hg status --all | grep -v '^I ' | cut -c '3-' | xargs git add
}
