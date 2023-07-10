function hyperlink() {
    local url="$1"
    local text="$2"
    printf '\e]8;;%s\e\\%s\e]8;;\e\\\n' "$url" "$text"
}

function fd() {
    command fd --color=always "$@" \
    | while read colored_path; do
        path=$(readlink -f $(echo -n $colored_path | ansifilter))
        url="vscode-insiders://file/$path"
        hyperlink $url $colored_path
      done
}
