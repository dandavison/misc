# Share shell history across shell processes

_SHRIKE_TARGET=
_SHRIKE_INDEX=0
_SHRIKE_GREP=rg

_shrike_history () {
    tac ~/dandavison7@gmail.com/shell_history/bash_eternal_history_02 | tr -s " " | cut -d " " -f 4-
}

_shrike_hit () {
    _shrike_history | $_SHRIKE_GREP "^$_SHRIKE_TARGET" | sed -n ${_SHRIKE_INDEX}p
}

_shrike_backward () {
    [ -n "$_SHRIKE_TARGET" ] || _SHRIKE_TARGET="$READLINE_LINE"
    ((_SHRIKE_INDEX+=1))
    local hit=$(_shrike_hit)
    READLINE_LINE="$hit"
}

_shrike_forward () {
    [ -n "$_SHRIKE_TARGET" ] && ((_SHRIKE_INDEX>1)) || return
    ((_SHRIKE_INDEX-=1))
    local hit=$(_shrike_hit)
    READLINE_LINE="$hit"
}

bind -x '"\e[5~":_shrike_backward'
bind -x '"\e[6~":_shrike_forward'
