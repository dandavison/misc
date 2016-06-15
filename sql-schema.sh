psql -U django -d $dbname -c '\d' | grep table | cut -d'|' -f2 | \
    while read table ; do psql -U django -d $dbname -c "\d $table" ; done
