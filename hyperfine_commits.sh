runs=3
infile=/tmp/23c292d3f25c67082a2ba315a187268be1a9b0ab.gitdiff
outfile=hyperfine.json

hyperfine \
    --runs $runs \
    --export-json $outfile \
    --ignore-failure \
    $(find /tmp/delta -type f | sort | head -n 3 | while read executable; do echo -n "'$executable < $infile > /dev/null' " ; done)
