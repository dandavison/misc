# extract a column from a tsv with header (alternatively, use xsv)
awk 'BEGIN{FS = "\t"}{if (NR > 1) print $10}'


# Create a directory of links for files that haven't been processed yet
for f in Sylvia_*/*.wav; do n=`sed -nE "s,.+/([0-9]+)\.mp3\.wav,\1,p" <<< $f`; [ -e $n.mp3.BirdNET.selections.txt ] || ln `realpath $f` remaining/ ; done
