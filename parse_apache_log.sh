cat_files () {
    while read file ; do
        if [[ $file == *.gz ]] ; then
            gunzip -c $file
        else
            cat $file
        fi
    done
}

ls -1t *_access.log* | \
    head -n 39 | \
    cat_files | \
    awk '$9 == 200 {print $7}' | \
    grep '^/' | \
    cut -d? -f1 | \
    sort | \
    uniq -c | \
    sort -rn
