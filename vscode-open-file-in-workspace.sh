
# code executable is slow
/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code ~/src/delta

# URL is fast, but only switches if the argument is a directory
open 'vscode://file//Users/dan/src/delta/'

# Fast, but opens in whatever window (workspace?) is focused by the WM
open 'vscode://file//Users/dan/src/delta/src/delta.rs'

# This is fast
open 'vscode://file//Users/dan/src/delta' && open 'vscode://file//Users/dan/src/delta/src/main.rs'