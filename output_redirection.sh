# Pipe stderr into a process
# Now stderr is on 1 and stdout is on 2
{ { echo stdout1 ; echo stdout2 ; echo stderr1 >&2 ; echo stderr2 >&2 ; } 2>&3 | cat >&2 ; } 3>&1 1>&2 | awk 1 ORS='\\n'

# Pipe stderr to a different process and put that output back on stderr
{ { { app 2>&3 | cat >&2 ; } 3>&1 | awk 1 ORS='\\n' ; } 2>&3 | cat >&2 ; } 3>&1


# Then deis could do

app () {
    echo stdout1
    echo stdout2
    echo stderr1 >&2
    echo stderr2 >&2 
}

{ { { app 2>&3 | cat >&2 ; } 3>&1 | awk 1 ORS='\\n' ; } 2>&3 | cat >&2 ; } 3>&1
stdout1
stdout2
stderr1\nstderr2\n
