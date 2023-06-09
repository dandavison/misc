CAT="bat --style header,grid"

what_i_mean() {
    local wis="$1"
    if [ -e "$wis" ]; then
        echo "$wis"
    else
        local wim=$(which "$wis")
        echo $wim
    fi
}

what_i_mean "$1"
