#!/bin/bash
# Convert an invocation like
# MathematicaScript -script file
# to use -run
echo \\begin{align*}
/Applications/Mathematica.app/Contents/MacOS/MathematicaScript -noprompt -run < $2
echo \\end{align*}
