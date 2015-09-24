ls -1t *_access.log* | head -n 39 | \
    while read file ; do
        if [[ $file == *.gz ]] ; then
            gunzip -c $file
        else
            cat $file
        fi
    done | \
awk '$9 == 200 {print $7}' | grep '^/' | cut -d? -f1 | sort | uniq -c | sort -rn
