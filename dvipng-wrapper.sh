log=/tmp/dvipng.log
__dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
. /Users/dan/src/misc/trace.sh
exec /usr/local/texlive/2018/bin/x86_64-darwin/dvipng $@
