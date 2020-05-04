# https://stuff-things.net/2018/01/30/building-emacs-25-on-macos-high-sierra/


# brew install autoconf automake texinfo
export PATH="/usr/local/opt/texinfo/bin:$PATH"

# https://www.reddit.com/r/emacs/comments/cdcdwj/how_do_i_maintain_emacs_27/ett4krk?utm_source=share&utm_medium=web2x
git pull && ./autogen.sh && ./configure && make

make configure && ./configure --with-ns --with-json --with-imagemagick && make install

# open nextstep/Emacs.app

# cp nextstep/Emacs.app /Applications


# History of my builds:
# GNU Emacs 27.0.50 (build 3, x86_64-apple-darwin17.7.0, NS appkit-1561.60 Version 10.13.6 (Build 17G65)) of 2018-09-27
