delta-dark-on () {
    git config core.pager 'delta --dark --syntax-theme=Dracula'
}

delta-light-on () {
    git config core.pager 'delta --light --syntax-theme=OneHalfLight'
}


delta-dark-on () {
    git config core.pager 'delta --dark --syntax-theme=Dracula'
    export BAT_THEME=Dracula
}

delta-light-on () {
    git config core.pager 'delta --light --syntax-theme=OneHalfLight'
    export BAT_THEME=OneHalfLight
}
