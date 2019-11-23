log=/tmp/dvisvgm.log

date >> $log
echo '----------------------------' >> $log
echo '$PWD: ' $PWD >> $log
echo '$(pwd): ' $(pwd) >> $log
echo '$0: ' $0 >> $log
echo '$@: ' $@ >> $log
echo >> $log
exec /usr/local/texlive/2018/bin/x86_64-darwin/dvisvgm $@
